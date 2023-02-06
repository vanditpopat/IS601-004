x = 0
a = [1,2,3,4,"5",6,1.5]

for i in a:
    if type(i) == str:
        x+=int(i)
    elif type(i) == float:
        x+=i
    else:
        x+=i

print(f"x is {x}")