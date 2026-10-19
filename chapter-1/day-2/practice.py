#write a program to guess anumber
import random
num=random.randint(1,10)
while True:
    guess=int(input("enter the no of guess :"))
    if guess==num:
        print("correct,you guess correct number")
        break
    if guess<num:
        print("too low, try again")
    elif guess>num:
        print("too high,try again")
