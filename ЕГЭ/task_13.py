import ipaddress


ip = '192.214.116.184'
for mask in range(33):
    network = ipaddress.ip_network(f'{ip}/{mask}', 0)
    if f'{network.network_address:b}'.count('1') % 5 == 0:
        print(f"{network}")
