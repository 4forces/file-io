#open the file for the reading
filename = input("please provide filename: ")
filepointer = open(filename) # cursor that points to (file) and opens it
for line in filepointer:
    print(line.strip())
