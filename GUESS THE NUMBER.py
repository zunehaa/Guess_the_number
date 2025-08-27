import random
randomnum=random.randint(1,100)
print("-----------------------")
print("|   GUESS THE NUMBER  |")
print("-----------------------")
print("YOU HAVE 10 CHANCES TO GUESS A NUMBER.\nGOOD LUCK!!!")
for i in range(1,11):
    a=int(input("ENTER A NUMBER: "))
    if(a==randomnum):
        print("YEAH!!!! YOU GUSSED IT RIGHT..")
        break
    elif(a>randomnum):
        print("TRY A SMALLER NUMBER..")
    elif(a<randomnum):
        print("TRY A GREATER NUMBER..")
else:
    print("YOUR CHANCES ARE GONE. THE NUMBER WAS",randomnum)
