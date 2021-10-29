import re
import requests


pattern = r"<a.*href=[\"\'](?:[\w]*://)?([\w\-\.]*)"
base_url = input()
site = requests.get(base_url).text

links = list(set(re.findall(pattern, site)))

links.sort()

for link in links:
    if link != '..':
        print(link)
