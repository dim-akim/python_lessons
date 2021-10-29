import csv


primary_types = {}
needed_year = '2015'
with open('Crimes.csv') as file:
    reader = csv.reader(file)
    print(next(reader))
    for row in reader:
        if needed_year in row[2]:
            type = row[5]
            if type not in primary_types:
                primary_types[type] = 0
            primary_types[type] += 1

key_max = max(primary_types, key=primary_types.get)
print(primary_types)
print(key_max, primary_types[key_max])
