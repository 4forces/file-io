filepointer = open("numbers.txt") #cursor that points to data.txt and opens it
total = 0 #initialise total = 0
for line in filepointer: #this step iterates thru each line in numbers.txt
    total += int(line) # total = total + line | note that line has to be integer-ed first
print("the total is", total)