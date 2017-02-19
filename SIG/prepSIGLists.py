#expect comma-delimited file with the columns: description,className,id,status
#data comes from https://www.bluetooth.com/specifications/gatt
#output used in gattConversions.py script

#fname = "chars.csv"
fname = "services.csv"

print "{"

with open(fname) as f:
  for lines in f:
    #line = f.readline().strip().split(",")
    line = lines.strip().split(",")
    print "    '0000"+line[2][2:]+"-0000-1000-8000-00805F9B34FB':'"+line[0]+"',"
    del line[:]

print "    '0':'default'"
print "  }"    
