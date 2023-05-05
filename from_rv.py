#!/usr/bin/env python

from __future__ import absolute_import, division, print_function

import netmiko

# List of addresses to target, using a list instead of dictionary allow me to reduce typing
devices = """
192.168.4.1	

""".strip().splitlines()
# Dictionary for authentication
device_type = "cisco_ios"
username = ""
password = ""
# Using the netmiko module to run these tasks
netmiko_exceptions = (
    netmiko.ssh_exception.NetMikoTimeoutException,
    netmiko.ssh_exception.NetMikoAuthenticationException,
    AttributeError,
)
command = """
#*********************************
#Config for the Nexus 7k
#*********************************
config terminal
scheduler job name Backup-Daily
  copy running-config tftp://192.168.2.38/$(SWITCHNAME)-config.txt vrf default vdc-all
  copy bootflash:/vlan.dat tftp://192.168.2.38/$(SWITCHNAME)-vlan.dat vrf default

exit
config terminal
  scheduler schedule name written-nightly
    time daily 23:30
    job name save-config
exit
config terminal
  scheduler schedule name Backup-Daily
    time start now repeat 24:0
    job name Backup-Daily
end
""".strip().splitlines()

# Creating a loop to target all the devices and sending 1 command and also allow me to skip failed devices
for device in devices:
    try:
        print("~" * 79)
        connection = netmiko.ConnectHandler(
            ip=device, device_type=device_type, username=username, password=password
        )
        print("Connecting to ", device)
        print(connection.send_config_set("show clock"))
        connection.disconnect()
    except netmiko_exceptions as e:
        print("Connection failed to ", device, e)
