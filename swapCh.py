def swap1(user_input,ch1,ch2):
    res=''
    if user_input!=None:
        res=user_input.replace(ch1,'*').replace(ch2,ch1).replace("*",ch2)
    return res
user_input=input()
ch1 ,ch2 = map(str,input().split())
print(swap1(user_input,ch1,ch2))

