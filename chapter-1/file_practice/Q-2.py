with open("Qtext1.txt","w")as f:
    f.write(" hii everyone \n we learning file i/o \n using java")
    f.write("\n i like programing in java")

with open("Qtext1.txt","r")as f:
    data=f.read()
    print(data)

with open("Qtext1.txt","r")as f:
    data=f.read()
    new_data=data.replace("java","python")
    print(new_data)

word="learning"
with open("Qtext1.txt","r")as f:
    data=f.read()
    if (data.find(word) !=-1):
        print("found")
    else:
        print("Not Found")

def find():
    word="learning"
    line_no=1
    with open("Qtext1.txt","r")as f:
        for line in f:
            if word in line:
                print(line_no)
                return
            line_no+=1
    return -1
print(find())

