n=[1,2,3,4,5,6,7,8,9,10]
print("List",n)
sum_4=sum(n[-4:])
print("sum of last 4 no:",sum_4)
diff= max(n)-min(n)
print("diffrence btw max and min:",diff)
num = n[3] // 3
n.insert(5, num)
print(n)