# 112.208.0.0
# 255.255.128.0

# 01110000.11010000.00000000.00000000
# 11111111.11111111.10000000.00000000

from ipaddress import *

total = 0
for addr in ip_network('112.208.0.0/255.255.128.0'):
    ip2 = f'{addr:b}'
    if ip2.count('1') % 11 == 0:
        print(ip2)
        total += 1

print(total)
