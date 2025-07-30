import os
import threading
from typing import List
import json

import requests
from bs4 import BeautifulSoup

from filters import (
    COLOUR_FILTER,
    EXTRAS_FILTER,
    FUEL_FILTER,
    GEARBOX_FILTER,
    MODEL_FILTER,
    TRIM_FILTER,
)
from notification import send_notification

## CONFIGURATION
BASE_URL = "https://www.dacia.co.uk"
PRODUCT_ID_FILE = "checked_ids.txt"
CHECK_INTERVAL = int(os.getenv("DACIA_CHECK_INTERVAL", 1800))


def _create_filter_string() -> str:
    query_strings = []
    if len(MODEL_FILTER) > 0:
        query_strings.append(
            f"model.code={'%2C'.join([m.value for m in MODEL_FILTER])}"
        )
    if len(FUEL_FILTER) > 0:
        query_strings.append(
            f"energy.group={'%2C'.join([f.value for f in FUEL_FILTER])}"
        )
    if len(GEARBOX_FILTER) > 0:
        query_strings.append(
            f"transmission.group={'%2C'.join([g.value for g in GEARBOX_FILTER])}"
        )
    if len(COLOUR_FILTER) > 0:
        query_strings.append(
            f"colorMarketing.group={'%2C'.join([c.value for c in COLOUR_FILTER])}"
        )

    filter_url = f"{BASE_URL}/new-stock.html?{'&'.join(query_strings)}"
    return filter_url

def _sanitise_json(raw_json: str) -> str:
    # Remove Javascript wrapper
    clean_json = raw_json.replace('window.APP_STATE=JSON.parse("', '')
    clean_json = clean_json.replace('");', '')
    # Remove double quote escaping
    clean_json = clean_json.replace('\\"', '"')
    # Remove double-escaped quote (eg 19" alloy)
    clean_json = clean_json.replace('\\\\"', '\\"')
    return clean_json


def _load_product_ids() -> List[str]:
    checked_ids = []
    if os.path.isfile(PRODUCT_ID_FILE):
        with open(PRODUCT_ID_FILE, "r") as file:
            checked_ids = [line.strip() for line in file]
    return checked_ids


def _record_product_id(new_product_id: str) -> None:
    with open(PRODUCT_ID_FILE, "a") as file:
        file.write(f"{new_product_id}\n")


def website_checker():
    print("Starting new check")
    threading.Timer(CHECK_INTERVAL, website_checker).start()
    cars_raw = requests.get(_create_filter_string()).content
    cars_parsed = BeautifulSoup(cars_raw, "html.parser")
    cars_data = cars_parsed.find_all("script")
    cars_json = json.loads(_sanitise_json(cars_data[3].text))
    cars_list = cars_json['page']['data']['content']['contentZone']['slice143v0']['data']['data']
    print(f"Found {len(cars_list)} vehicles available")

    checked_cars = _load_product_ids()
    for vehicle in cars_list:
        product_id = vehicle['productId']
        vehicle_url = f"https://www.dacia.co.uk/new-stock/car-details.html?productId={product_id}"
        # Skip this vehicle if we've already checked it out
        if product_id in checked_cars:
            continue
        # Skip this vehicle if the trim level doesn't match
        vehicle_trim = vehicle['version']['label'].split(" ")[0]
        if len(TRIM_FILTER) > 0 and vehicle_trim not in [t.value for t in TRIM_FILTER]:
            continue

        print(f"Checking new car ({product_id})")

        # Look at the extras for this vehicle to see what's attached
        vehicle_options = vehicle['options']
        vehicle_extras = vehicle['equipments']
        vehicle_extras_list = [e['label'] for e in vehicle_options + vehicle_extras]

        vehicle_matches = []
        for extra in EXTRAS_FILTER:
            match = any(extra.value["search_string"] in s for s in vehicle_extras_list)
            vehicle_matches.append(match)
            print(f"{'[YES]' if match else '[NO]'} {extra.value['name']}")

        if False not in vehicle_matches:
            print("DREAM CAR FOUND")
            print(f"{BASE_URL}{vehicle_url}")
            send_notification(
                f"There is a car that matches your criteria\n{BASE_URL}{vehicle_url}"
            )

        # Record this vehicle so we can skip it next time
        _record_product_id(new_product_id=product_id)


website_checker()
