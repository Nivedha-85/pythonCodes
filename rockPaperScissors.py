import random
user = input("Whats your choice? 'r'for rock,'p'for paper,'s'for scissors")
comp = random.choice['r','p','s']
if user == comp:
    print('Its a tie'+"U0001F923")
elif user=='r' and (comp=='p' or comp=='s') and (user=='p' and comp=='r') and (user=='s' and comp=='p'):
    print("You won!wohoo")
else:
    print("Try again next time.You lost!")#+emoji.emojize(":zipper_mouth_face:"))