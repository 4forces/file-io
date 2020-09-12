filename = input("Enter filename: ")
filepointer = open(filename, 'r') #'r' stands for reading
# read each line into the list
lines = list(filepointer) #this open file and stores it in ram

line_no = int(input("which line to delete?"))
del lines[line_no] #remove something from the list by index [line_no]

filepointer.close() #to close the file which open in line 4

filepointer = open(filename, 'w') #this step and for loop is to write to the file 
for l in lines:
    filepointer.write(l)
filepointer.close()