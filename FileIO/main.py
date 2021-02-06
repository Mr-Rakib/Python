"""
    r - read mode - default
    w - write mode
    x - create file if not exist
    a - append to the file
    t - text mode - default
    b - binary mode
    + - read and update

    file.read() -> read the hole file as a text
    file.readLine() -> read by line
    file.readLines()
    file.open()
    file.close()
"""
file = open("student.json")
file2 = open("rakib.txt")
# content = file.read(100) read the 100 character
# content = file.read()

for index in file:
    print(index)


file.close()
file2.close()

file = open("student.json")
file2 = open("rakib.txt")

print(file2.readline())
print(file.readlines())
