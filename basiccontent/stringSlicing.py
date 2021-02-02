"""
    String Slicing
    string[init:last:increment]
    default:
        init : 0
        last : len(string)
        increment: 1

    reverse :
        string [::-1]
    full
        string[::]

    default function -> return boolean
        .isalpha()
        .endswith('someString')

        others
            .count('character/string')
            .capitalize()
            .find('is')
            .lower()
            .upper()
            .replace("is", "are")
"""

string = "Hello, I am Md. Rakibul Hasan. Doing the real job to develop scalable web application"
print("Length: ", len(string))
print(string[0::])
print(string[0:10:1])
print(string[0:10:2])
print(string[0:85])
print(string[:85])


print(string[::-1])
print(string[-4:])
print(string[-4:-2])

print("Is alpha numeric: ", string.isalnum())
print("Total a: ", string.count('a'))
print("Total number of r/R: ", string.count('r')+string.count('R'))

print(string.capitalize())
print(string.lower())
print(string.upper())
print(string.lower().islower())

print(string.lower().replace("r", "EEEE"))

print(string.replace("l", "e"))