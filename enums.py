from enum import Enum


class Model(Enum):
    # Filter: model.code=DU3
    # Multiple: model.code=DU3%2CBD1
    Bigster = "BD1"
    Duster = "DU3"
    Jogger = "RI1"
    Sandero = "BI1"
    Spring = "S1E"


class Fuel(Enum):
    # Filter: energy.group=HEV
    # Multiple: energy.group=HEV%2CMILDHYBRID
    BiFuel = "ICEBIFUELLPG"
    Electric = "ELECTRIC"
    Hybrid = "HEV"
    Mild = "MILDHYBRID"
    Petrol = "ESS"


class Gearbox(Enum):
    # Filter: transmission.group=AUTOMATIC
    # Multiple: transmission.group=AUTOMATIC%2CMANUAL
    Automatic = "AUTOMATIC"
    Manual = "MANUAL"


class Colour(Enum):
    # Filter: colorMarketing.hexaCode=000000
    # Multiple: colorMarketing.hexaCode=000000%2C008000
    Black = "BLACK"
    Blue = "BLUE"
    Green = "GREEN"
    Grey = "GREY"
    Orange = "ORANGE"
    Red = "RED"
    Sandstone = "BROWN"
    White = "BLANC%2CWHITE"


class Trim(Enum):
    Expression = "expression"
    Extreme = "extreme"
    Journey = "journey"


class Extras(Enum):
    Sunroof = {
        "name": "Panoramic Sunroof",
        "search_string": "Panoramic opening sunroof",
    }
    TwoTone = {"name": "Two Tone Black Roof", "search_string": "tone Black roof"}
