import random

a =[1,2,3,4]

print(a[random.randint(0, 3)])

if a[1] or a[3]:
    print(True)
elif a[0] or a[2]:
    print(False)