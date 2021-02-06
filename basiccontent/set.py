"""
    Set is the unique list
    always add/return the unique value
    s = set()

    s.add(value)
    s.remove(value)
"""

a = set({1, 2, 3, 4})
a.add(5)
a.add(6)
a.remove(2)

b = set ({1, 2, 3, 5, 7})

print(a, b, " : ", a.union(b))

print(a.union(b))
print(a.intersection(b))
