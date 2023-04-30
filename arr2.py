a = [1,2,3,4,5,6,1,6,9,34,545,220,545,220,34,34,3]
c = {}
d = [x*2 for x in a]
for i in a:
    if i in c.keys():
        c[i] +=1
    else:
        c[i] = 1
    
print(f"{d}")