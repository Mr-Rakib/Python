"""
list = [1,2,3,4,5,6,7,8,9,10]

print("print the list")
for item in list:
    print(item, end=" ")

examList = [int, float, 1,20,66,90, 'Hello', "Rakib", {'rakib': {'id': 1, 'username' : 'rakibhasan'} }]
print("\nprint exam list")
for item in examList:
    print(item)

print("\nprint in a range till 6 ")
for i in range(6):
    print(i, end=" ")

print("\nprint in a range 2-9 ")
for i in range(2,9):
    print(i, end= " ")

print("\nprint in a range 0-10 with increment 2")
for i in range(0, 10, 2):
    print(i, end=" ")

for x in [0, 10, 2]:
    print(x)
"""

print("\nprint in a range till 6 ")
for i in range(6):
    if i == 2:
        continue
    print(i)
else:
    print("Finally finished!")


print("\nprint in a range till 6 ")
for i in range(10):
    if i == 8:
        break
    print(i)

