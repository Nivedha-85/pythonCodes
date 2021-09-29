en = input()
de = input()
enc = []
de  =[]
for i in en:
    enc.append((chr(ord(i)+5)))
for i in range(len(enc)):
    print(enc[i])