from AutoWorld import World
from BaseClasses import Region
from .locations import CookieClickerLocation, location_table


class CookieClickerWorld(World):
    game = "Cookie Clicker"

    def create_regions(self):
        region = Region("Menu", self.player, self.multiworld)

        for name, loc_id in location_table.items():
            region.locations.append(
                CookieClickerLocation(self.player, name, loc_id, region)
            )

        self.multiworld.regions.append(region)
