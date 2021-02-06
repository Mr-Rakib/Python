"""
x = 0
while x <= 10:
    print(x)
    x+=1
#-------------------
x = 0
while x <= 10:
    if x == 3:
        x += 1
        continue

    print(x)
    x += 1
#-----------------
x = 0
while x <= 100:
    if x <= 15 or x >= 30:
        x += 1
        continue
    print(x)
    x += 1
#----------------
x = 0
while x <= 100:
    if 15 <= x <= 30:
        x += 1
        continue
    print(x)
    x += 1
#----------------
"""
x = 0
while x <= 100:
    if x == 30:
        break
    print(x)
    x += 1
