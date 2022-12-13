import os
f = open("names.txt", "w")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("names.txt", "r")
print(f.read())
#os.remove("demofile2.txt")