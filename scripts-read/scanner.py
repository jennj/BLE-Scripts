import sys
from gattlib import DiscoveryService

service = DiscoveryService("hci0")
possibleTargets = list()

###
# Scan for advertising packets and get AdvAs
###
def doDiscovery():
  global possibleTargets

  # check 5 times for advertising devices
  for x in range(0,10):

    # use gattlib to scan for possible target advertisers
    devices = service.discover(2)

    # loop through scan results
    for dev in devices.items():

      # check to see if the detected device is not already in our list
      if dev not in possibleTargets:
        # not in the list, add it!
        possibleTargets.append(dev)
        # my dev is an immutable list *menna frenna*
        if len(dev[1].strip()) == 0:
          name ="No name provided."
        else:
          name = dev[1]
        # add device to the device selection menu
        print str(len(possibleTargets)) + " " + dev[0] + " " + name

###
# Scan for a longer time because the first scan did not provide correct AdvAs
###
def doMoreDiscovery():

  global possibleTargets

  del possibleTargets[:]

  counter = 0

  # lets loop 5 or so times, that will be be 25 scans (will take a bit)
  print "Scanning 25 more times, please be patient..."
  while counter < 5:
    doDiscovery()
    counter += 1
    #print str( counter*5 ) + " scans completed."
  print ""
  print "25 scans completed."

###
# Provide a list of the targets for selection and get user selection
###
def getTargetDeviceIndex(isFirstRound):
  global possibleTargets
  result = list()

  print ""
  if not isFirstRound:
    print "Second round of discovery completed."
  print "Select the number of a target device (1-"+str(len(possibleTargets))+") and press <ENTER>."
  if isFirstRound:
    print "Press any other key and <ENTER> to continue looking for devices."
  print "Press <CTRL>-C to end the program."

  key = raw_input()

  try:
    key = int(key)
    result.append(True)
  except ValueError:
    result.append(False)

  result.append(key)

  return result

###
# Basic scanner
###
def scan():
  global possibleTargets
  # perform first round of target device discovery --> This should be successful if the device is close by
  print ""
  print "Scanning to discover possible target devices. Please wait for 30 seconds..."
  doDiscovery()

  if len(possibleTargets) == 0:
    # oops... first round of device discovery not successful
    print "First round of device discovery not successful.  Scanning again."
    doMoreDiscovery()
    if len(possibleTargets) == 0:
      print "Scanned 30 times total, and found no devices in range."
      print "Please check your Bluetooth adapter & your target BLE device to make sure they are working properly."
      sys.exit()


###
# Scan and select AdvA
###
def getAdvAFromScan():
  global possibleTargets

  scan()

  key = getTargetDeviceIndex(True)

  if not key[0]:
    doMoreDiscovery()
    key = getTargetDeviceIndex(False)
    if not key[0]:
      print "Invalid input. Program exiting."
      sys.exit()

  #print ""
  #print possibleTargets[key[1]-1][0]
  return possibleTargets[key[1]-1][0]


###
# main
###
if __name__ == '__main__':
  #perform a simple scan for advertising devices
  scan()



