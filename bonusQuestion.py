
import random
user =input("Enter any six digit number\n")
match=0
ans='y'
num = input(random.randint(100000,999999))
line=str(num)
while line!=user:
        num = (input(random.randint(100000,999999)))
        line = str(num)
        match == match + 1
print("You string",num," got matched in ",match,"time's")
