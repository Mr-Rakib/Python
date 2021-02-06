"""
    Conditions
      *  if/else:
      *  if/elif/else
      * if (value in [list]) return true
      * if (value not in [list]) return true
"""
name = input("Enter your name : ")
age = input("Enter your age : ")

if(type(float(age)) == float):

    if(type(float(age)) != 'float'):
        print("Name : ", name)
    if ( float(age) < 18 ):
        print("You are teen")
    elif (float(age)>=18 and float(age)<= 30 ):
        print("Your are an adult")
    else:
        print("You are a too much adult/old")
else :
    print("Invalid age")

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(5 in list)
print(15 in list)
