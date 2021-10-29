import re
import requests


pattern = r"<a.*href=\"(.*)\">"
link1, link2 = input(), input()
site = requests.get(link1)
link_found = False
links = re.findall(pattern, site.text)
for link in links:
    try:
        page = requests.get(link)
        if link2 in page.text:
            link_found = True
            break
    except:
        pass

print('Yes' if link_found else 'No')
