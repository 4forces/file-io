#open the file for the reading
filepointer = open("data.txt") # cursor that points to data.txt and opens it
for line in filepointer:
    print(line.strip())
