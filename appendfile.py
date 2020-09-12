filename = input("Enter the filename: ")
filepointer = open(filename, 'a') #a is referring to append mode

line = input("Enter text, type !q to quit: ")
while line != "!q":
    filepointer.write(line+"\n")
    line = input("Enter text, type !q to quit: ")
filepointer.close()