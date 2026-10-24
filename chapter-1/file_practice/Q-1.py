f=open("text1.txt","r")
data=f.read()
print(data)


f.seek(0)
line1=f.readline()
print(line1)

with open("text1.txt","w") as f:
    f.write("learning python from apna collage")


with open("text1.txt","r")as f:
    print(f.read())


with open("text1.txt","a")as f:
    f.write("\n start learning javascript also")


with open("text1.txt","r")as f:
    print(f.read())

with open("text1.txt","r+")as f:
    f.write("hii")
    print(f.read())

import os
os.remove("text1.txt")

