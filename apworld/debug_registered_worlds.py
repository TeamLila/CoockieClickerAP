# debug_registered_worlds.py
import sys
# ensure project root is on path
sys.path.insert(0, ".")

# Import the AutoWorld registry and print what it contains
try:
    from worlds.AutoWorld import AutoWorldRegister
except Exception as e:
    print("Failed importing worlds.AutoWorld:", e)
    raise

print("AutoWorldRegister attributes:")
for attr in ("world_types", "worlds_by_name"):
    print(f" - {attr} in AutoWorldRegister? {'yes' if hasattr(AutoWorldRegister, attr) else 'no'}")

print("\nRegistered world types (keys):")
wt = getattr(AutoWorldRegister, "world_types", None)
if not wt:
    print("  <no registered world types>")
else:
    for k, v in wt.items():
        print("  key:", k, "class:", v, "options_dataclass:", getattr(v, "options_dataclass", None))
