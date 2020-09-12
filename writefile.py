#open the file `info.txt` in the `write mode`
#1. if the file does not exist, Python will create it
#2. if the file already exists, Python will overwrite it (and hence original data will be gone)
filepointer = open('info.txt', 'w')
filepointer.write("chicken thigh\n")
filepointer.write("Fresh Milk\n")
filepointer.write("Toilet Roll\n")
filepointer.close()
