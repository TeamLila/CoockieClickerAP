from BaseClasses import Location

#Selfnote: if any Numbers get Depricated, DO NOT REUSE THEM
class IdDefinitions():
    BASE_ID = 2026_000_000
    UNIT_ID = BASE_ID + 100_000

class CookieClickerLocation(Location):
    game = "Cookie Clicker"


location_table = {
    # name : id (THATS IT FOR NOW)
    "Buy 1 Cursor": IdDefinitions.UNIT_ID + 1,
    "Buy 1 Grandma": IdDefinitions.UNIT_ID + 2,
    "Buy 1 Farm": IdDefinitions.UNIT_ID + 3,
    "Buy 1 Mine": IdDefinitions.UNIT_ID + 4,
    "Buy 1 Factory": IdDefinitions.UNIT_ID + 5,
    "Buy 1 Bank": IdDefinitions.UNIT_ID + 6,
    "Buy 1 Temple": IdDefinitions.UNIT_ID + 7,
    "Buy 1 Wizzard Tower": IdDefinitions.UNIT_ID + 8,
    "Buy 1 Shipment": IdDefinitions.UNIT_ID + 9,
    "Buy 1 Alchemy Lab": IdDefinitions.UNIT_ID + 10,
    "Buy 1 Portal": IdDefinitions.UNIT_ID + 11,
    "Buy 1 Time Machien": IdDefinitions.UNIT_ID + 12,
    "Buy 1 Antimatter Condenser": IdDefinitions.UNIT_ID + 13,
    "Buy 1 Prism": IdDefinitions.UNIT_ID + 14,
    "Buy 1 Chance Maker": IdDefinitions.UNIT_ID + 15,
    "Buy 1 Fractal Engine": IdDefinitions.UNIT_ID + 16,
    "Buy 1 Javascript Console": IdDefinitions.UNIT_ID + 17,
    "Buy 1 Idleverse": IdDefinitions.UNIT_ID + 18,
    "Buy 1 Cortex Baker": IdDefinitions.UNIT_ID + 19,
    "Buy 1 You": IdDefinitions.UNIT_ID + 20
}