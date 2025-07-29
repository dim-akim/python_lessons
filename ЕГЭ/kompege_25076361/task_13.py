from ipaddress import *


network = ip_network('158.214.121.40/255.255.255.224', strict=False)
print(network)
