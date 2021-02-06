"""
file = open("rakib.txt", "w")

char = file.write("Hello world")
print(char)

file.close()

file = open("rakib.txt", "a")

char = file.write("\nHello world")
print(char)

file.close()
"""

file = open("rakib.txt", "r+")
text = ""

if file.read() == "":
    text = "Hello world"
else:
    text = "\nHello world"

print(file.read() == "", text)

file.write(text)
file.close()
