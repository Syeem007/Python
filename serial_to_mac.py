import re

# Enter the serial number of the switch
serial_number = input("Enter the serial number of the Cisco Nexus switch: ")

# Extract the last four characters of the serial number
last_four_chars = serial_number[-4:]

# Convert the last four characters to hexadecimal format
hex_chars = ''.join([hex(ord(c))[2:].zfill(2) for c in last_four_chars])

print()

# Format the MAC address using the OUI prefix and the hexadecimal characters
mac_address = "AC16:B234:" + hex_chars[0:2] + ":" + hex_chars[2:4] + ":" + hex_chars[4:]

# Print the MAC address
print("The MAC address of the switch is:", mac_address)
