###
# Get the standard description of a characteritistic based on UUID
###
def getCharacteristicDescription(uuid):
  characteristicDescriptions = {
    '00002A00-0000-1000-8000-00805F9B34FB':'Device Name',
    '00002A01-0000-1000-8000-00805F9B34FB':'Appearance',
    '00002A02-0000-1000-8000-00805F9B34FB':'Peripheral Privacy Flag',
    '00002A03-0000-1000-8000-00805F9B34FB':'Reconnection Address',
    '00002A04-0000-1000-8000-00805F9B34FB':'Peripheral Preferred Connection Parameters',
    '00002A05-0000-1000-8000-00805F9B34FB':'Service Changed',
    '00002A06-0000-1000-8000-00805F9B34FB':'Alert Level',
    '00002A07-0000-1000-8000-00805F9B34FB':'Tx Power Level',
    '00002A08-0000-1000-8000-00805F9B34FB':'Date Time',
    '00002A09-0000-1000-8000-00805F9B34FB':'Day of Week',
    '00002A0A-0000-1000-8000-00805F9B34FB':'Day Date Time',
    '00002A0C-0000-1000-8000-00805F9B34FB':'Exact Time 256',
    '00002A0D-0000-1000-8000-00805F9B34FB':'DST Offset',
    '00002A0E-0000-1000-8000-00805F9B34FB':'Time Zone',
    '00002A0F-0000-1000-8000-00805F9B34FB':'Local Time Information',
    '00002A11-0000-1000-8000-00805F9B34FB':'Time with DST',
    '00002A12-0000-1000-8000-00805F9B34FB':'Time Accuracy',
    '00002A13-0000-1000-8000-00805F9B34FB':'Time Source',
    '00002A14-0000-1000-8000-00805F9B34FB':'Reference Time Information',
    '00002A16-0000-1000-8000-00805F9B34FB':'Time Update Control Point',
    '00002A17-0000-1000-8000-00805F9B34FB':'Time Update State',
    '00002A18-0000-1000-8000-00805F9B34FB':'Glucose Measurement',
    '00002A19-0000-1000-8000-00805F9B34FB':'Battery Level',
    '00002A1C-0000-1000-8000-00805F9B34FB':'Temperature Measurement',
    '00002A1D-0000-1000-8000-00805F9B34FB':'Temperature Type',
    '00002A1E-0000-1000-8000-00805F9B34FB':'Intermediate Temperature',
    '00002A21-0000-1000-8000-00805F9B34FB':'Measurement Interval',
    '00002A22-0000-1000-8000-00805F9B34FB':'Boot Keyboard Input Report',
    '00002A23-0000-1000-8000-00805F9B34FB':'System ID',
    '00002A24-0000-1000-8000-00805F9B34FB':'Model Number String',
    '00002A25-0000-1000-8000-00805F9B34FB':'Serial Number String',
    '00002A26-0000-1000-8000-00805F9B34FB':'Firmware Revision String',
    '00002A27-0000-1000-8000-00805F9B34FB':'Hardware Revision String',
    '00002A28-0000-1000-8000-00805F9B34FB':'Software Revision String',
    '00002A29-0000-1000-8000-00805F9B34FB':'Manufacturer Name String',
    '00002A2A-0000-1000-8000-00805F9B34FB':'IEEE 11073-20601 Regulatory Certification Data List',
    '00002A2B-0000-1000-8000-00805F9B34FB':'Current Time',
    '00002A2C-0000-1000-8000-00805F9B34FB':'Magnetic Declination',
    '00002A31-0000-1000-8000-00805F9B34FB':'Scan Refresh',
    '00002A32-0000-1000-8000-00805F9B34FB':'Boot Keyboard Output Report',
    '00002A33-0000-1000-8000-00805F9B34FB':'Boot Mouse Input Report',
    '00002A34-0000-1000-8000-00805F9B34FB':'Glucose Measurement Context',
    '00002A35-0000-1000-8000-00805F9B34FB':'Blood Pressure Measurement',
    '00002A36-0000-1000-8000-00805F9B34FB':'Intermediate Cuff Pressure',
    '00002A37-0000-1000-8000-00805F9B34FB':'Heart Rate Measurement',
    '00002A38-0000-1000-8000-00805F9B34FB':'Body Sensor Location',
    '00002A39-0000-1000-8000-00805F9B34FB':'Heart Rate Control Point',
    '00002A3F-0000-1000-8000-00805F9B34FB':'Alert Status',
    '00002A40-0000-1000-8000-00805F9B34FB':'Ringer Control Point',
    '00002A41-0000-1000-8000-00805F9B34FB':'Ringer Setting',
    '00002A42-0000-1000-8000-00805F9B34FB':'Alert Category ID Bit Mask',
    '00002A43-0000-1000-8000-00805F9B34FB':'Alert Category ID',
    '00002A44-0000-1000-8000-00805F9B34FB':'Alert Notification Control Point',
    '00002A45-0000-1000-8000-00805F9B34FB':'Unread Alert Status',
    '00002A46-0000-1000-8000-00805F9B34FB':'New Alert',
    '00002A47-0000-1000-8000-00805F9B34FB':'Supported New Alert Category',
    '00002A48-0000-1000-8000-00805F9B34FB':'Supported Unread Alert Category',
    '00002A49-0000-1000-8000-00805F9B34FB':'Blood Pressure Feature',
    '00002A4A-0000-1000-8000-00805F9B34FB':'HID Information',
    '00002A4B-0000-1000-8000-00805F9B34FB':'Report Map',
    '00002A4C-0000-1000-8000-00805F9B34FB':'HID Control Point',
    '00002A4D-0000-1000-8000-00805F9B34FB':'Report',
    '00002A4E-0000-1000-8000-00805F9B34FB':'Protocol Mode',
    '00002A4F-0000-1000-8000-00805F9B34FB':'Scan Interval Window',
    '00002A50-0000-1000-8000-00805F9B34FB':'PnP ID',
    '00002A51-0000-1000-8000-00805F9B34FB':'Glucose Feature',
    '00002A52-0000-1000-8000-00805F9B34FB':'Record Access Control Point',
    '00002A53-0000-1000-8000-00805F9B34FB':'RSC Measurement',
    '00002A54-0000-1000-8000-00805F9B34FB':'RSC Feature',
    '00002A55-0000-1000-8000-00805F9B34FB':'SC Control Point',
    '00002A56-0000-1000-8000-00805F9B34FB':'Digital',
    '00002A58-0000-1000-8000-00805F9B34FB':'Analog',
    '00002A5A-0000-1000-8000-00805F9B34FB':'Aggregate',
    '00002A5B-0000-1000-8000-00805F9B34FB':'CSC Measurement',
    '00002A5C-0000-1000-8000-00805F9B34FB':'CSC Feature',
    '00002A5D-0000-1000-8000-00805F9B34FB':'Sensor Location',
    '00002A5E-0000-1000-8000-00805F9B34FB':'PLX Spot-Check Measurement',
    '00002A5F-0000-1000-8000-00805F9B34FB':'PLX Continuous Measurement',
    '00002A60-0000-1000-8000-00805F9B34FB':'PLX Features',
    '00002A63-0000-1000-8000-00805F9B34FB':'Cycling Power Measurement',
    '00002A64-0000-1000-8000-00805F9B34FB':'Cycling Power Vector',
    '00002A65-0000-1000-8000-00805F9B34FB':'Cycling Power Feature',
    '00002A66-0000-1000-8000-00805F9B34FB':'Cycling Power Control Point',
    '00002A67-0000-1000-8000-00805F9B34FB':'Location and Speed',
    '00002A68-0000-1000-8000-00805F9B34FB':'Navigation',
    '00002A69-0000-1000-8000-00805F9B34FB':'Position Quality',
    '00002A6A-0000-1000-8000-00805F9B34FB':'LN Feature',
    '00002A6B-0000-1000-8000-00805F9B34FB':'LN Control Point',
    '00002A6C-0000-1000-8000-00805F9B34FB':'Elevation',
    '00002A6D-0000-1000-8000-00805F9B34FB':'Pressure',
    '00002A6E-0000-1000-8000-00805F9B34FB':'Temperature',
    '00002A6F-0000-1000-8000-00805F9B34FB':'Humidity',
    '00002A70-0000-1000-8000-00805F9B34FB':'True Wind Speed',
    '00002A71-0000-1000-8000-00805F9B34FB':'True Wind Direction',
    '00002A72-0000-1000-8000-00805F9B34FB':'Apparent Wind Speed',
    '00002A73-0000-1000-8000-00805F9B34FB':'Apparent Wind Direction',
    '00002A74-0000-1000-8000-00805F9B34FB':'Gust Factor',
    '00002A75-0000-1000-8000-00805F9B34FB':'Pollen Concentration',
    '00002A76-0000-1000-8000-00805F9B34FB':'UV Index',
    '00002A77-0000-1000-8000-00805F9B34FB':'Irradiance',
    '00002A78-0000-1000-8000-00805F9B34FB':'Rainfall',
    '00002A79-0000-1000-8000-00805F9B34FB':'Wind Chill',
    '00002A7A-0000-1000-8000-00805F9B34FB':'Heat Index',
    '00002A7B-0000-1000-8000-00805F9B34FB':'Dew Point',
    '00002A7D-0000-1000-8000-00805F9B34FB':'Descriptor Value Changed',
    '00002A7E-0000-1000-8000-00805F9B34FB':'Aerobic Heart Rate Lower Limit',
    '00002A7F-0000-1000-8000-00805F9B34FB':'Aerobic Threshold',
    '00002A80-0000-1000-8000-00805F9B34FB':'Age',
    '00002A81-0000-1000-8000-00805F9B34FB':'Anaerobic Heart Rate Lower Limit',
    '00002A82-0000-1000-8000-00805F9B34FB':'Anaerobic Heart Rate Upper Limit',
    '00002A83-0000-1000-8000-00805F9B34FB':'Anaerobic Threshold',
    '00002A84-0000-1000-8000-00805F9B34FB':'Aerobic Heart Rate Upper Limit',
    '00002A85-0000-1000-8000-00805F9B34FB':'Date of Birth',
    '00002A86-0000-1000-8000-00805F9B34FB':'Date of Threshold Assessment',
    '00002A87-0000-1000-8000-00805F9B34FB':'Email Address',
    '00002A88-0000-1000-8000-00805F9B34FB':'Fat Burn Heart Rate Lower Limit',
    '00002A89-0000-1000-8000-00805F9B34FB':'Fat Burn Heart Rate Upper Limit',
    '00002A8A-0000-1000-8000-00805F9B34FB':'First Name',
    '00002A8B-0000-1000-8000-00805F9B34FB':'Five Zone Heart Rate Limits',
    '00002A8C-0000-1000-8000-00805F9B34FB':'Gender',
    '00002A8D-0000-1000-8000-00805F9B34FB':'Heart Rate Max',
    '00002A8E-0000-1000-8000-00805F9B34FB':'Height',
    '00002A8F-0000-1000-8000-00805F9B34FB':'Hip Circumference',
    '00002A90-0000-1000-8000-00805F9B34FB':'Last Name',
    '00002A91-0000-1000-8000-00805F9B34FB':'Maximum Recommended Heart Rate',
    '00002A92-0000-1000-8000-00805F9B34FB':'Resting Heart Rate',
    '00002A93-0000-1000-8000-00805F9B34FB':'Sport Type for Aerobic and Anaerobic Thresholds',
    '00002A94-0000-1000-8000-00805F9B34FB':'Three Zone Heart Rate Limits',
    '00002A95-0000-1000-8000-00805F9B34FB':'Two Zone Heart Rate Limit',
    '00002A96-0000-1000-8000-00805F9B34FB':'VO2 Max',
    '00002A97-0000-1000-8000-00805F9B34FB':'Waist Circumference',
    '00002A98-0000-1000-8000-00805F9B34FB':'Weight',
    '00002A99-0000-1000-8000-00805F9B34FB':'Database Change Increment',
    '00002A9A-0000-1000-8000-00805F9B34FB':'User Index',
    '00002A9B-0000-1000-8000-00805F9B34FB':'Body Composition Feature',
    '00002A9C-0000-1000-8000-00805F9B34FB':'Body Composition Measurement',
    '00002A9D-0000-1000-8000-00805F9B34FB':'Weight Measurement',
    '00002A9E-0000-1000-8000-00805F9B34FB':'Weight Scale Feature',
    '00002A9F-0000-1000-8000-00805F9B34FB':'User Control Point',
    '00002AA0-0000-1000-8000-00805F9B34FB':'Magnetic Flux Density - 2D',
    '00002AA1-0000-1000-8000-00805F9B34FB':'Magnetic Flux Density - 3D',
    '00002AA2-0000-1000-8000-00805F9B34FB':'Language',
    '00002AA3-0000-1000-8000-00805F9B34FB':'Barometric Pressure Trend',
    '00002AA4-0000-1000-8000-00805F9B34FB':'Bond Management Control Point',
    '00002AA5-0000-1000-8000-00805F9B34FB':'Bond Management Feature',
    '00002AA6-0000-1000-8000-00805F9B34FB':'Central Address Resolution',
    '00002AA7-0000-1000-8000-00805F9B34FB':'CGM Measurement',
    '00002AA8-0000-1000-8000-00805F9B34FB':'CGM Feature',
    '00002AA9-0000-1000-8000-00805F9B34FB':'CGM Status',
    '00002AAA-0000-1000-8000-00805F9B34FB':'CGM Session Start Time',
    '00002AAB-0000-1000-8000-00805F9B34FB':'CGM Session Run Time',
    '00002AAC-0000-1000-8000-00805F9B34FB':'CGM Specific Ops Control Point',
    '00002AAD-0000-1000-8000-00805F9B34FB':'Indoor Positioning Configuration',
    '00002AAE-0000-1000-8000-00805F9B34FB':'Latitude',
    '00002AAF-0000-1000-8000-00805F9B34FB':'Longitude',
    '00002AB0-0000-1000-8000-00805F9B34FB':'Local North Coordinate',
    '00002AB1-0000-1000-8000-00805F9B34FB':'Local East Coordinate',
    '00002AB2-0000-1000-8000-00805F9B34FB':'Floor Number',
    '00002AB3-0000-1000-8000-00805F9B34FB':'Altitude',
    '00002AB4-0000-1000-8000-00805F9B34FB':'Uncertainty',
    '00002AB5-0000-1000-8000-00805F9B34FB':'Location Name',
    '00002AB6-0000-1000-8000-00805F9B34FB':'URI',
    '00002AB7-0000-1000-8000-00805F9B34FB':'HTTP Headers',
    '00002AB8-0000-1000-8000-00805F9B34FB':'HTTP Status Code',
    '00002AB9-0000-1000-8000-00805F9B34FB':'HTTP Entity Body',
    '00002ABA-0000-1000-8000-00805F9B34FB':'HTTP Control Point',
    '00002ABB-0000-1000-8000-00805F9B34FB':'HTTPS Security',
    '00002ABC-0000-1000-8000-00805F9B34FB':'TDS Control Point',
    '00002ABD-0000-1000-8000-00805F9B34FB':'OTS Feature',
    '00002ABE-0000-1000-8000-00805F9B34FB':'Object Name',
    '00002ABF-0000-1000-8000-00805F9B34FB':'Object Type',
    '00002AC0-0000-1000-8000-00805F9B34FB':'Object Size',
    '00002AC1-0000-1000-8000-00805F9B34FB':'Object First-Created',
    '00002AC2-0000-1000-8000-00805F9B34FB':'Object Last-Modified',
    '00002AC3-0000-1000-8000-00805F9B34FB':'Object ID',
    '00002AC4-0000-1000-8000-00805F9B34FB':'Object Properties',
    '00002AC5-0000-1000-8000-00805F9B34FB':'Object Action Control Point',
    '00002AC6-0000-1000-8000-00805F9B34FB':'Object List Control Point',
    '00002AC7-0000-1000-8000-00805F9B34FB':'Object List Filter',
    '00002AC8-0000-1000-8000-00805F9B34FB':'Object Changed',
    '00002AC9-0000-1000-8000-00805F9B34FB':'Resolvable Private Address Only',
    '0':'default'
  }

  description = characteristicDescriptions.get(uuid.upper(), "Characteristic description not found.")
  return description

###
# Get the standard description of a service based on UUID.
###
def getServiceDescription(uuid):
  serviceDescriptions = {
    '00001811-0000-1000-8000-00805F9B34FB':'Alert Notification Service',
    '00001815-0000-1000-8000-00805F9B34FB':'Automation IO',
    '0000180F-0000-1000-8000-00805F9B34FB':'Battery Service',
    '00001810-0000-1000-8000-00805F9B34FB':'Blood Pressure',
    '0000181B-0000-1000-8000-00805F9B34FB':'Body Composition',
    '0000181E-0000-1000-8000-00805F9B34FB':'Bond Management',
    '0000181F-0000-1000-8000-00805F9B34FB':'Continuous Glucose Monitoring',
    '00001805-0000-1000-8000-00805F9B34FB':'Current Time Service',
    '00001818-0000-1000-8000-00805F9B34FB':'Cycling Power',
    '00001816-0000-1000-8000-00805F9B34FB':'Cycling Speed and Cadence',
    '0000180A-0000-1000-8000-00805F9B34FB':'Device Information',
    '0000181A-0000-1000-8000-00805F9B34FB':'Environmental Sensing',
    '00001800-0000-1000-8000-00805F9B34FB':'Generic Access',
    '00001801-0000-1000-8000-00805F9B34FB':'Generic Attribute',
    '00001808-0000-1000-8000-00805F9B34FB':'Glucose',
    '00001809-0000-1000-8000-00805F9B34FB':'Health Thermometer',
    '0000180D-0000-1000-8000-00805F9B34FB':'Heart Rate',
    '00001823-0000-1000-8000-00805F9B34FB':'HTTP Proxy',
    '00001812-0000-1000-8000-00805F9B34FB':'Human Interface Device',
    '00001802-0000-1000-8000-00805F9B34FB':'Immediate Alert',
    '00001821-0000-1000-8000-00805F9B34FB':'Indoor Positioning',
    '00001820-0000-1000-8000-00805F9B34FB':'Internet Protocol Support',
    '00001803-0000-1000-8000-00805F9B34FB':'Link Loss',
    '00001819-0000-1000-8000-00805F9B34FB':'Location and Navigation',
    '00001807-0000-1000-8000-00805F9B34FB':'Next DST Change Service',
    '00001825-0000-1000-8000-00805F9B34FB':'Object Transfer',
    '0000180E-0000-1000-8000-00805F9B34FB':'Phone Alert Status Service',
    '00001822-0000-1000-8000-00805F9B34FB':'Pulse Oximeter',
    '00001806-0000-1000-8000-00805F9B34FB':'Reference Time Update Service',
    '00001814-0000-1000-8000-00805F9B34FB':'Running Speed and Cadence',
    '00001813-0000-1000-8000-00805F9B34FB':'Scan Parameters',
    '00001824-0000-1000-8000-00805F9B34FB':'Transport Discovery',
    '00001804-0000-1000-8000-00805F9B34FB':'Tx Power',
    '0000181C-0000-1000-8000-00805F9B34FB':'User Data',
    '0000181D-0000-1000-8000-00805F9B34FB':'Weight Scale',
    '0':'default'
  }
  description = serviceDescriptions.get(uuid.upper(), "Service description not found.")
  return description


###
#  Get the list of permissions for a characteristic based on the permissions code (00-FF)
###
def getCharacteristicPermissions(perm):

  # possible permissions for a value
  permissions = [
    "broadcast",
    "read",
    "write w/o response",
    "write",
    "notify",
    "indicate",
    "signed writes",
    "extended properties"]

  #container for permissions to be returned
  vals = list()

  #check to see if passed value is integer
  try:
    permValue=int(perm)
  except ValueError:
    vals.append("No permissions for unexpected value: "+str(perm))
    permValue=0

  # check each bit for 1, if yes, append permission to list
  for x in range (1,9):
    if ( permValue & (1<<x) ):
      vals.append(permissions[x])
  return vals


###
# main (test cases)
###
if __name__ == '__main__':
# char 00002a00-0000-1000-8000-00805F9B34FB
# service 00001800-0000-1000-8000-00805F9B34FB

  # tests to see if lookups are working
  print getCharacteristicDescription("00002a00-0000-1000-8000-00805F9B34FB")
  print getServiceDescription("00001800-0000-1000-8000-00805F9B34FB")
  print getCharacteristicDescription("10002a00-0000-1000-8000-00805F9B34FB")
  print getServiceDescription("10001800-0000-1000-8000-00805F9B34FB")
  print getCharacteristicPermissions(2)
  print getCharacteristicPermissions("x")
