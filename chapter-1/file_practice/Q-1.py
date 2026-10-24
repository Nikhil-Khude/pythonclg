f=open("text1.txt","r")
data=f.read()
print(data)


f.seek(0)
line1=f.readline()
print(line1)