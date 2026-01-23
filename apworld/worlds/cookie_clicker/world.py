from worlds.AutoWorld import World
from BaseClasses import Region
from .locations import CookieClickerLocation, location_name_to_id
from .items import item_name_to_id
from .options import CookieClickerOptions


#Main Class
class CookieClickerWorld(World):
    #what is it internaly called?
    game = "cookie_clicker"
    
    #define the id's
    location_name_to_id = location_name_to_id
    item_name_to_id = item_name_to_id
    
    #Define options
    options_dataclass = CookieClickerOptions
    
    topology_present = False
    
    def create_regions(self):
        menu_region = Region("Menu", self.player, self.multiworld)

        for name, loc_id in self.location_name_to_id.items():
            from BaseClasses import Location
            menu_region.locations.append(Location(self.player, name, loc_id, menu_region))

        self.multiworld.regions.append(menu_region)