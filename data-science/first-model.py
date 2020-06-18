import pandas

trips = pandas.read_excel('trips_data.xlsx')

graph = trips.vacation_preference.value_counts().plot(kind='bar')
graph.figure
