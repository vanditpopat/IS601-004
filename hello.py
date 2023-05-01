import sys
print(type("Hello"))

"""
multiline comment

"""

age = 20

if age>=21:
    print("Can Drink")
elif age>=18:
    print("Is an adult")
else:
    print("Kid")

#a = sys.maxsize

#print(f"{a} {type(a)}")
a = 1
b = 0
for i in range(10):
    if i % 2 == 0 : 
        b+=1

print(f"b is {b}")
