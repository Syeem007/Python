import schedule
import time
from netmiko import ConnectHandler
import datetime
import ftplib


def backup():
    # Device connection details
    device = {
        'host': 'device_ip',
        'username': 'user',
        'password': 'password',
        'device_type': 'cisco_nxos'
    }

    # Connect to the device
    net_connect = ConnectHandler(**device)

    # Get the running configuration
    running_config = net_connect.send_command('show run')

    # Create a timestamp for the backup file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # Create the backup file
    with open(f'running_config_{timestamp}.txt', 'w') as f:
        f.write(running_config)

    # FTP Server connection details
    ftp_server = 'ftp.server.com'
    ftp_user = 'ftp_user'
    ftp_pass = 'ftp_password'

    # Connect to FTP server
    ftp = ftplib.FTP(ftp_server)
    ftp.login(ftp_user, ftp_pass)
    ftp.cwd('/backup')

    # upload the backup file
    with open(f'running_config_{timestamp}.txt', 'rb') as f:
        ftp.storbinary(f"STOR running_config_{timestamp}.txt", f)

    # close the FTP connection
    ftp.quit()


# Schedule the backup to run every day at 1:00 AM
schedule.every().day.at("01:00").do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)
