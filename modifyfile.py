filename = input("Enter filename: ")
filepointer = open(filename, 'r') #'r' stands for reading
# read each line into the list
lines = list(filepointer)

line_no = int(input("which line to delete?"))
del lines[line_no] #remove something from the list by index [line_no]

filepointer.close()

filepointer = open(filename, 'w')
for l in lines:
    filepointer.write(l)
filepointer.close()