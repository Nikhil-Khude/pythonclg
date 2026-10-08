text="Hey i am Nikhil"
#comman string funtion
#1.strip spaces from both end
print("remove spaces :",text.strip())

#2.convert to lowercase
print("lower case :",text.lower())

#3.convert to uppercase
print("upper case :",text.upper())

#4.cspitilize first letter of each word
print("capitilize first letter :",text.title())

#5.title case (capitilize each word)
print("title case :",text.title())

#6.count occurrences of substring
print("letter o occurs :",text.count("i"),"time")

#7.find the position of a substring (-1 if you not found)
print("position of Nikhil :",text.find("nikhil"))

#8.replace a substring  with another substring
print("replace 'nikhil'with 'nikil' :",text.replace("Nikhil", "nikil"))


#9.check if the string starts or end with certain substring
print("start with 'Hey' :",text.startswith("Hey"))
print("end with 'Nikhil' :",text.endswith("Nikhil"))
