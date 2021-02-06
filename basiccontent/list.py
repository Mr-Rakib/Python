"""
    List data structure in Python

    ** Both are change the original value of the list
        list.reverse()
        list.sort()

    ** Use slicing for not-change the main value
        list[::-1] -> reverse
        list[0] -> get the first value
        list[::]/ list[:]/ list, list[0:], list[:len(list)] -> for access the hole list

    ** functions:
        max(list)
        min(list)
        len(list)
        list.append(10) -> add to the end
        list.insert(index, value) -> add to the index
        list.remove(value) -> remove value from the list
        list.pop() -> remove the last element from the list

    **
    Mutable - List [1,2,3]
    Immutable - Tuple (1,2,3)
        - when it just 1 value use extra ', ' here : ex:- (1,)
"""

#List

list = [1,2,3,4,5,6,7,8,9,10];
print(list)
print(list[::-1])
print(list[::-1][1])
list.append(11)
print(list[::-1])
print(list.insert(1, 10))
print(list[::])
list.remove(9);
print(list[::])
list.pop()
print(list[::])

#tuple -> immutable: can not change the value
tuple = (1,2,3,4,5)
print(tuple[::2])
print(tuple[::-1])