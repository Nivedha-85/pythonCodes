string = input()
count=0
final_s=''
for i in string:
    if(i == '-'):
        count+=1
    else:
        final_s+=i
print("-"*count,final_s)