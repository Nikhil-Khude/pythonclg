f = open("Day-1/data.txt", "r")

content = f.read()
words = content.split()

print("Total number of words:", len(words))

unique_words = set(words)
print("Unique words:", unique_words)

f.close()

unique_words = list(dict.fromkeys(words))
print("Unique words:", unique_words)