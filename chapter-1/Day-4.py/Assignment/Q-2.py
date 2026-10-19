f = open("Day-1/data.txt", "r")

lines = f.readlines()

print("Total number of lines:", len(lines))
print("2nd line:", lines[1], end="")
print("4th line:", lines[3], end="")

f.close()