import ipaddress


network = ipaddress.ip_network('172.16.77.26/23', 0)
# addr = ipaddress.ip_address('172.16.77.26')
iface = ipaddress.ip_interface('172.16.77.26/255.255.254.0')

for addr in network:
    print(f'{addr:b}')
