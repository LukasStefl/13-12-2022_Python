import os
f = open("names.txt", "rt")


d = f.read()
w = d.split()

for x in w:
    w.count("/a/")
    w.count("/b/")
    w.count("/c/")
    w.count("/d/")



print(w.count("/a/"))
print(w.count("/b/"))
print(w.count("/c/"))
print(w.count("/d/"))