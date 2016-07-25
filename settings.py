import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 500

# The maximum rent you want to pay per month.
MAX_PRICE = 1400

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'vancouver'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = ["van", "nvn", "bnc", "rds", "pml", "rch"]

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
        "VAN": [
        [49.198177,-123.023068],
        [49.313037,-123.274155],
    ],
	"BBY/NW": [
        [49.180637,-122.891689],
        [49.295133,-123.02465],
    ],
	"COQ": [
        [49.218461,-122.624853],
        [49.351592,-122.893344],
    ],
	"RCH": [
        [49.086123,-122.95711],
        [49.200102,-123.279812],
    ]
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = ["none"]

## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = 1.5 # kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
TRANSIT_STATIONS = {
    "Yaletown | Z1": [49.27455,-123.1219],
    "Waterfront | Z1": [49.285833,-123.111667],
    "VCC-Clark | Z1": [49.265753,-123.078825],
    "VCC | Z1": [49.28202,-123.11875],
    "Stadium-Chinatown | Z1": [49.279444,-123.109444],
    "Rupert | Z1": [49.260833,-123.032778],
    "Renfrew | Z1": [49.258889,-123.045278],
    "Olympic | Z1": [49.266389,-123.115833],
    "Oakridge | Z1": [49.233056,-123.116667],
    "Nanaimo | Z1": [49.248184,-123.05564],
    "Marine_Drive | Z1": [49.209722,-123.116944],
    "Science_World | Z1": [49.273114,-123.100348],
    "Langara | Z1": [49.226389,-123.116111],
    "King_Edward | Z1": [49.249167,-123.115833],
    "Joyce-Collingwood | Z1": [49.23835,-123.031704],
    "Granville | Z1": [49.28275,-123.116639],
    "Commercial-Broadway | Z1": [49.2625,-123.068889],
    "Burrard | Z1": [49.285616,-123.120157],
    "Broadway-City_Hall | Z1": [49.262778,-123.114444],
    "29th_Ave | Z1": [49.244084,-123.045931],
    "Sperling | Z2": [49.25914,-122.96391],
    "Sapperton | Z2": [49.22443,-122.88964],
    "Royal_Oak | Z2": [49.220004,-122.988381],
    "Richmond-Brighouse | Z2": [49.168056,-123.136389],
    "Production_Way | Z2": [49.25337,-122.91815],
    "Patterson | Z2": [49.22967,-123.012376],
    "New_West |Z2": [49.201354,-122.912716],
    "Metrotown | Z2": [49.225463,-123.003182],
    "Lougheed | Z2": [49.24846,-122.89702],
    "Lansdowne | Z2": [49.174722,-123.136389],
    "Lake_City_Way | Z2": [49.25458,-122.93903],
    "Holdom | Z2": [49.26469,-122.98222],
    "Gilmore | Z2": [49.26489,-123.01351],
    "Edmonds | Z2": [49.212054,-122.959226],
    "Columbia | Z2": [49.20476,-122.906161],
    "Bridgeport | Z2": [49.195556,-123.126111],
    "Brentwood | Z2": [49.26633,-123.00163],
    "Braid | Z2": [49.23322,-122.88283],
    "Aberdeen | Z2": [49.183889,-123.136389],
    "22nd_St | Z2": [49.2,-122.949167]
}

## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'apa'

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 20 * 60 # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#housing"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass
