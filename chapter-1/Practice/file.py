file=open("data.txt","r")

f=open("data.txt","r")
print(f.read())
f.close

f=open("data.txt","r")
print(f.readline())
f.close

f=open("data.txt","r")
print(f.readlines())
f.close

f = open("data.txt", "w")
f.write("hello python")
f.close

f=open("data.txt","w")
f.writelines(["hello\n","python\n","MCA"])
f.close
