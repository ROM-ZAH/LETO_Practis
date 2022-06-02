a = input()
k = 0
s = a.split(";")
for i in range(len(s)):
    if s[i].isdigit(): 
        if int(s[i]) % 2 == 0:
            if k == 0: 
                print(f'{s[i]}', end="")
                k = 1
            else:
                print(f',{s[i]}', end="")
for i in range(len(s)):
    if s[i].isdigit(): 
        if int(s[i]) % 3 == 0:
            if k == 0: 
                print(f'{s[i]}', end="")
                k = 15
            else:
                print(f',{s[i]}', end="")
for i in range(len(s)):
    if not s[i].isdigit():
        if len(s[i]) > 4:
            if k == 0: 
                print(f'{s[i]}', end="")
                k = 1
            else:
                print(f',{s[i]}', end="")
