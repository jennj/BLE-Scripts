from PyBT import gatt
from PyBT import roles 
from scapy.all import HCI_Cmd_LE_Set_Advertising_Data, HCI_Cmd_LE_Set_Advertise_Enable

##############
# This is not a functioning script.  
# It advertises :), 
# but it does not seem to accept connections :\. 
#######

###
# Create the GATT db
##
attrdb = gatt.Attribute_DB()

#0x1  0018 , Service: Generic Access
attrdb.primary("1800")

#0x2  0203 00 002a , Characteristic:Device Name
# char declaration
attrdb.characteristic("2a00", gatt.GATT_PROP_READ)

#0x3  4769676173657420472d746167 , Gigaset G-tag
# char value
attrdb.attribute("2a00", gatt.GATT_PERMIT_READ, "Gigaset G-tag")

#0x4  020500012a , Characteristic:Appearance
# char declaration
attrdb.characteristic("2a01", gatt.GATT_PROP_READ)

#0x5  0000 ,
# char value
attrdb.attribute("2a01", gatt.GATT_PERMIT_READ, '\x00\x00')

# Add the handles (can be see in the 
attrdb.refresh_handles()

###
# Debug.
##
# check to see that the values are the same as the original device
for x in attrdb.attributes: 
  print x

###
# Create a peripheral with the GATT
##
periph = roles.LE_Peripheral(attrdb, 0, False, None)


#set_advertising_params(self, adv_type, channel_map=0, interval_min=0, interval_max=0, daddr='00:00:00:00:00:00', datype=0)
periph.stack.set_advertising_params(0x0,0x7,0x0800,0x0800,'00:00:00:00:00:00',0x0)

#enable advertising 0x01 on, 0x00 off
periph.stack.set_advertising_enable(1)

#set the advertsing data
# length 0x00-0x1f
# value [Vol 3] Part C, Section 11. -> 31 octets
# status Part D, Error Codes on page 370
advert = '\x03\xFF\x80\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

#start advertising
periph.stack.set_advertising_data(advert)

# Not sure what this does, but it didn't make it connectable
# periph.run()


###
# Original captured values
##
#0x1  0018 				, Service: Generic Access
#0x2  0203 00 002a 			, Characteristic:Device Name
#0x3  4769676173657420472d746167 	, Gigaset G-tag
#0x4  020500012a 			, Characteristic:Appearance
#0x5  0000 				,
#0x6  0a0700022a 			, Characteristic:Peripheral Privacy Flag
#0x7  00 				,
#0x8  020900042a 			, Characteristic:Peripheral Preferred Connection Parameters
#0x9  c8003f0104005802
# the handles are not contiguous!
#0xc  0118
#0xd  220e00052a
#0xe  0100ffff
#0xf  0000
