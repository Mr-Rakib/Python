"""
    default
    custom
    main
    doc string
"""


def Addition(a, b):
    """This function return the addition of two number"""
    return a + b


print(Addition(1, 3))
print(Addition.__doc__)

for index in range(10):
    print(index, index**2, "=", Addition(index, index**2))