# imports from installed libraries
import sys, binascii
from gattlib import GATTRequester

# imports from own scripts
sys.path.insert(0, '../util/')
from gattConversions import getCharacteristicPermissions, getCharacteristicDescription, getServiceDescription
from scanner import getAdvAFromScan

if __name__ == '__main__':

  AdvA = getAdvAFromScan()

  requester = GATTRequester(AdvA, False)
  #requester = GATTRequester(AdvA)

  print("Connecting...")
  sys.stdout.flush()
  requester.connect(True)

  # request service discovery from slave
  primary = requester.discover_primary()

  # request characteristic discovery from slave
  declarators = requester.discover_characteristics()

  #requester.disconnect()

  print ""
  primaryFormatted = {}
  print "gatttool services output:"
  for prim in primary:
    primaryFormatted["ServiceDescription"] = getServiceDescription(prim.get("uuid"))
    primaryFormatted["EndHandle"] = hex(prim.get("end"))
    primaryFormatted["StartHandle"] = hex(prim.get("start"))
    primaryFormatted["UUID"] = prim.get("uuid")
    print primaryFormatted


  print ""
  print "characteristics output:"
  declaratorsFormatted = {}
  valueFormatted = {}
  extendedFormatted = {}
  extendedProperties = False
  lastHandleProcessed = 0x00
  j = 0x00

  for chars in declarators:

    #check to see if extended descriptors present from last interation
    if extendedProperties:
      print "Extended properties descriptors:"

      # determine how many potential handles we have to loop through
      count = hex(chars.get("handle")) - lastHandleProcessed
      # bug --> we are not ignoring service handles here

      if count < 2:
        print "Extended properties not present. BLE device does not conform to standard."

      else:

        for x in range(1,count-1):
          extendedFormatted["Handle"]= hex(chars.get("value_handle")+x)

          try:
            val = requester.read_by_handle( chars.get("value_handle")+x )[0]
            hexval = binascii.hexlify(val)
            extendedFormatted["HexValue"] = hexval
            extendedFormatted["ASCII"] = val
          except:
            extendedFormatted["HexValue"] = "666666"
            extendedFormatted["ASCII"] = "Error reading handle."

          print extendedFormatted          
      

    #chraracteristic declarator
    declaratorsFormatted["_DeclaratorHandle"] = hex(chars.get("handle"))
    declaratorsFormatted["Permissions"] = getCharacteristicPermissions(chars.get("properties"))
    declaratorsFormatted["Description"] = getCharacteristicDescription(chars.get("uuid"))

    #print type(chars.get("value_handle")[0])
    #characteristic value
    #print requester.read_by_handle( hex(chars.get("value_handle") & 0xffff) )[0]
    #print requester.read_by_handle(0x16)[0]
    j = int(chars.get("value_handle")) & 0xffff
    #print requester.read_by_handle(j)[0]
    valueFormatted["_Handle"] = hex(chars.get("value_handle"))
    try:
      val = requester.read_by_handle(j)[0]
      hexval = binascii.hexlify(val)
      valueFormatted["HexValue"] = hexval
      valueFormatted["ASCII"] = val
    except:
      #print sys.exc_info()[0]
      valueFormatted["HexValue"] = "666666"
      valueFormatted["ASCII"] = "Error reading handle."

    #print what you have so far
    print declaratorsFormatted
    print valueFormatted

    #we need to get the extend properties in the next iteration
    if "extended properties" in declaratorsFormatted:
      extendedProperties = True
      lastHandleProcessed = chars.get("value_handle")
