from xml.etree import ElementTree


def scores(element, level=1):
    colors[element.attrib['color']] += level
    for child in element:
        scores(child, level + 1)

data = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
root = ElementTree.fromstring(data)
colors = {
    'red': 0,
    'green': 0,
    'blue': 0
}
scores(root)
print(*(colors[i] for i in colors))
