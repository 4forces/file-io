import csv
import json

filepointer = open('test.csv')
csvfile = csv.reader(filepointer, delimiter=",")
data = {}

next(csvfile) #skip the first (header) row
for row in csvfile:
    employee = {
        'isbn': row[0],
        'title': row[1],
        'author': row[2]
    }
    data[row[0]] = employee

print(data)

json_string = json.dumps(data) # dump to data

print(data)