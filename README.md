# Dacia Stock

A Python tool for constantly checking the Dacia new cars website with a set of filters applied to notify if your perfect 
car is available. It will then send a Discord notification to a preset webhook URL to your server.

## Motivation
> So why the hell did you build this, SplinterHead?

I ordered a Bigster when they were new, but the lead time was 4 months. I wrote this tool to check for cancellations in 
case I could get my hands on a vehicle with the same specs any earlier

## Configuration
### Discord 
First, set up a Discord Webhook to receive notifications.

This is done in the `Server Settings` > `Integrations` > `Webhooks`

Add a new webhook and make sure to `Copy Webhook URL` once it's configured

### Dacia Stock
Now we need to configure which vehicles and preferences to filter o

The included `filters.py` is set to look for Dacia Bigsters in Blue, with Automatic, Hybrid engines. It is also set to 
find cars that have both the Two-Tone paint and the sunroof. 

If this oddly-specific filter is not what you are looking for, then change the criteria of the filters. All available
options can be seen in `enums.py` and will hopefully be self-explanatory.

As this tool has been created to look at the Bigster, the available optional extras only apply to that model. Please create
a PR if more optional extras are discovered for the other models.

#### Example:
```python
MODEL_FILTER = [Model.Bigster, Model.Duster]
COLOUR_FILTER = [Colour.White]
```
_This will return all Bigsters and Dusters that are White_

**There is no sanity check yet**
```python
MODEL_FILTER = [Model.Spring]
COLOUR_FILTER = [Colour.Green]
```
_This will return nothing as Green is not an option for Dacia Spring models_

### Environment Variables
* `DISCORD_WEBHOOK_URL`: URL for sending a notification to Discord
* `DACIA_CHECK_INTERVAL`: [Optional] How frequently the tool will check the Dacia website. Default to 1800 (30 mins)

## Running
This can be run as a standalone Python script:

```
export DISCORD_WEBHOOK_URL=<URL>
python main.py
```

Or it can be run as a Docker container:

```docker run -e "DISCORD_WEBHOOK_URL=<URL> splinterhead27/dacia-stock-check```

Or it can be run with Docker Compose:

```yaml
services:
  dacia_stock:
    image: splinterhead27/dacia-stock-check
    container_name: dacia-stock-check
    environment:
      DISCORD_WEBHOOK_URL: <URL>
```
