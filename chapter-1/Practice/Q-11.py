text=input("enter a text:-")
total=0
for ch in text:
    if ch in "aeiou":
        total+=1
        print(ch,end=" ")
print(total)