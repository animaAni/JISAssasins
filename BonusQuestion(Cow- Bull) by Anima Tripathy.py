import random
num=random.randint(1000,9999)
line=str(num)
print("Random number:",line)
user =input("Enter any four digit number\n")
print("User Input:",user)
cow=0
bull=0
for x in range(4):
    if line[x]==user[x]:
        cow=cow+1
    else:
        bull=bull+1
print ("Num of cows:",cow)
print ("Num of bulls:",bull)
