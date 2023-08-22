import random 
# in this line we get an input from the user
user = input('"r" for rock, "p" for paper and "s" for scissors: ')
# In this line, we assign a random value to the variable named computer. 
computer = random.choice(["r","p","s"])
if user == computer: 
    print("Your choice is same  as computer ")
elif (user != computer):
    if (user =="r" and computer =="p") or (user =="p" and computer =="s") \
          or (user=="s" and computer =="r" ):
        print(f"your choice is ' {user} ' and computer random value is ' {computer} '  ")
        print("YOU ARE LOST")
    else : 
        print(f"your choice is {user} and computer random value is {computer}.  ")
        print("YOU ARE WON ")
    