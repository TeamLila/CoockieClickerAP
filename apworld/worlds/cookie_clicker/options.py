from dataclasses import dataclass
from Options import PerGameCommonOptions, Toggle, Range

#SHOWCASE CLASSES HOW TO DEFINE
class DummyToggleClass(Toggle):
    display_name = "Toggle Testing Class (does nothing)"

class StartingCookieCount(Range):
    display_name = "Starting Cookies"
    range_start = 0
    range_end = 1_000_000_000
    default = 0


#Option Class: for later
@dataclass
class CookieClickerOptions(PerGameCommonOptions):
    Dummy_Toggle: DummyToggleClass
    Starting_Cookies: StartingCookieCount


