# Import required modules/packages/library
from pprint import pprint
# creat the outher list for all devices
devices = []
# open the file and read the list of devices info
file = open('devices-04.txt', 'r')
for line in file:
    # Get sevice info into list
    device_info_list = line.strip().split(',')
    # Put device information into dictionary for this one device
    device_info = {} # Creat the inner dictionary of device info
    device_info['name'] = device_info_list[0]
    device_info['os-type'] = device_info_list[1]
    device_info['ip'] = device_info_list[2]
    device_info['username'] = device_info_list[3]
    device_info['password'] = device_info_list[4]
    # Display what we have read and built so far
    print('Read device information: ', device_info)
    # Now append our device and its info onto our 'devices' list
    devices.append(device_info)
# Display a blank line to make easier to read
print('')
# Display a tirle
print('Input converted to a list containing disctionaries:')

# Diaplay the list with nice formatting
pprint(devices)
# Close the file
file.close()
