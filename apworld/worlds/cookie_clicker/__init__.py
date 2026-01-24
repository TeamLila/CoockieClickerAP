from ..AutoWorld import World
from BaseClasses import Region, Location

from .locations import CookieClickerLocation, location_name_to_id
from .items import item_name_to_id
from .options import CookieClickerOptions

def ShowcaseProgress(Text: str):
    for _ in range(0, 5):
        print("-----------------------------------------------")
    print(Text)
    for _ in range(0, 5):
        print("-----------------------------------------------")

ShowcaseProgress("Loading Class...")
#Main Class
class CookieClickerWorld(World):
    #what is it internaly called?
    ShowcaseProgress("Defining name")
    game = "cookie_clicker"
    
    ShowcaseProgress("defining id's")
    #define the id's
    location_name_to_id = location_name_to_id
    item_name_to_id = item_name_to_id
    
    ShowcaseProgress("Defining options")
    #Define options
    options_dataclass = CookieClickerOptions
    topology_present = False
    
    ShowcaseProgress("Defining region")
    def create_regions(self):
        menu_region = Region("Menu", self.player, self.multiworld)

        for name, loc_id in self.location_name_to_id.items():
            from BaseClasses import Location
            menu_region.locations.append(Location(self.player, name, loc_id, menu_region))

        self.multiworld.regions.append(menu_region)

ShowcaseProgress("Class Loaded without errors")