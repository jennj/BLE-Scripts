# imports from installed libraries
import sys
from gattlib import GATTRequester

# imports from own scripts
sys.path.insert(0, '../util/')
from gattConversions import getCharacteristicPermissions, getCharacteristicDescription, getServiceDescription
from scanner import getAdvAFromScan

if __name__ == '__main__':

  AdvA = getAdvAFromScan()

  requester = GATTRequester(AdvA, False)

  print("Connecting...")
  sys.stdout.flush()
  requester.connect(True)

  primaryFormatted = {}
  primary = requester.discover_primary()
  print "gatttool services output"
  for prim in primary:
    primaryFormatted["ServiceDescription"] = getServiceDescription(prim.get("uuid"))
    primaryFormatted["EndHandle"] = hex(prim.get("end"))
    primaryFormatted["StartHandle"] = hex(prim.get("start"))
    primaryFormatted["UUID"] = prim.get("uuid")
    print primaryFormatted

  characteristicsFormatted = {}
  characteristics = requester.discover_characteristics()
  for chars in characteristics:
    characteristicsFormatted["DeclaratorHandle"] = hex(chars.get("handle"))
    characteristicsFormatted["CharacteristicHandle"] = hex(chars.get("value_handle"))
    characteristicsFormatted["Permissions"] = getCharacteristicPermissions(chars.get("properties"))
    characteristicsFormatted["Description"] = getCharacteristicDescription(chars.get("uuid"))
    characteristicsFormatted["UUID"] = chars.get("uuid")
    print characteristicsFormatted

