import csv

filepointer = open('test.csv')
csvfile = csv.reader(filepointer, delimiter=",")
next(csvfile) #skip the first (header) row
for row in csvfile:
    print("ISBN:", row[0])
    print("Title:", row[1])
    print("Author:", row[2])
    print()