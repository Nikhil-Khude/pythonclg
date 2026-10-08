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

#10.split the string starts list by delimiter
print("simple split",text.split())

#11.join a list of strings with a seprator
words=["hello","i", "am","nikhil"]
print("join the word :"," ".join(words))

#12.count the vowels in the string
vowels="aeiou"
vowel_count=sum(1 for char in text if char in vowels)
print("number of vowels :",vowel_count)


#13.using opreatres with strings
txt="hello"
txt1="hi"

#reapeat the string 3 times and give a space in between
print("reapeat string :",(txt+" ")*3)

#15.split the string in 2 part and print
txt3=input("enetr the word :")
print(txt3.find("a")) 
print(txt3.replace("a","n"))

#16.sorted list of charter in the string
print("sorted list of char :",sorted(txt3))


#17.take input from users and find alphabetic char in the string and replace with new

txt5="nikhilkhude"
p1,sep,p2=txt5.partition("k")
parts=[p1,sep+p2]
print("spilt string :",parts)

#funtions
#length
numbers=[1,2,3,4,5,6,7,8,9]
print("no of item in list are :",len(numbers))

#sum
print("sum of numbers :",sum(numbers))

#sorting
print("list in asending oredr :",sorted(numbers))
print("list in desending order :",sorted(numbers ,reverse=True))