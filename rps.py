import random
user = input("Whats your choice? 'r'for rock,'p'for paper,'s'for scissors\n")
comp = random.choice(['r','p','s'])
print("You chose:"+user)
print("Computer chose:"+comp)
print()
if user == comp:
    print('Its a tie'+"\U0001F923")
elif user=='r' and comp=='s' and (user=='p' and comp=='r') and (user=='s' and comp=='p'):
    print("You won!wohoo")
else:
    print("Try again next time.You lost!"+"\U0001F600")#+emoji.emojize(":zipper_mouth_face:"))