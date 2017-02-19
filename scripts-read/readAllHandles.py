# imports from installed libraries
import sys, binascii
from gattlib import GATTRequester

# imports from own scripts
sys.path.insert(0, '../util/')
from gattConversions import getCharacteristicDescription, getServiceDescription
from scanner import getAdvAFromScan


if __name__ == '__main__':

  AdvA = getAdvAFromScan()

  requester = GATTRequester(AdvA)
  invalidHandles = list()

  for x in range(0x00,0xffff):
    if x%1000 == 0:
      print "................................................Handle Counter at: "+str(hex(x))
    try:
      val = requester.read_by_handle(x)[0]
      hexval = binascii.hexlify(val)

      # example service value (sv): 0018
        # service uuid = sv[2:][0:2]
      # example characteristic declarator value (cdv): 020300002a
        # cdv[0:2] = permissions
        # cdv[4:6]+cdv[2:4] = characteristic value
        # cdv[8:10]+cdv[6:8] = characteristic UUID (short form)

      # parse service descriptor
      if len(hexval) == 4:
        lookup = getServiceDescription("0000"+hexval[2:]+hexval[0:2]+"-0000-1000-8000-00805F9B34FB")
        if lookup != "Service description not found.":
          val = "Service: " + lookup

      # parse characteristic declarator 
      if len(hexval) == 10:
        lookup = getCharacteristicDescription("0000"+hexval[8:]+hexval[6:8]+"-0000-1000-8000-00805F9B34FB")
        if lookup != "Characteristic description not found.":
          val = "Characteristic:" + lookup

      print str(hex(x))
      print "  " + hexval + " , " + val

    except:
      invalidHandles.append(x)
