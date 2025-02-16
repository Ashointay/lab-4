import json  

file = open("sample-data.json", "r")  
data = json.load(file)  
file.close()  

print("Interface Status")  
print("=" * 80)  

header_dn = "DN"  
header_description = "Description"  
header_speed = "Speed"  
header_mtu = "MTU"  

column_width_dn = 50  
column_width_description = 20  
column_width_speed = 7  
column_width_mtu = 6  

print(header_dn.ljust(column_width_dn) + " " + header_description.ljust(column_width_description) + " " + header_speed.ljust(column_width_speed) + " " + header_mtu.ljust(column_width_mtu))  

print("-" * 80)  

for item in data["imdata"]:  
    attributes = item["l1PhysIf"]["attributes"]  

    dn = attributes["dn"]  

    if "descr" in attributes:  
        description = attributes["descr"]  
    else:  
        description = ""  

    if "speed" in attributes:  
        speed = attributes["speed"]  
    else:  
        speed = "inherit"  

    mtu = attributes["mtu"]  

    print(dn.ljust(column_width_dn) + " " + description.ljust(column_width_description) + " " + speed.ljust(column_width_speed) + " " + mtu.ljust(column_width_mtu))  
