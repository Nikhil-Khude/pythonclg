#Write a program to read a file and count how many vowels are present in its content
f = open("Day-1/data.txt", "r")
content=f.read()

count = 0
for ch in content:
    if ch.lower() in "aeiou":
        count += 1

print("Total vowels:", count)

f.close()