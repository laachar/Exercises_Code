import subprocess

#return all the available network
networks = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])

decoded_networks = networks.decode('ascii')

print(decoded_networks)
