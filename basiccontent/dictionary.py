"""
    dictionary: (key, value) pair
    can access the value by O(1) -> time complexity

    dictionary.copy() : copy the dictionary and save to the other location
    dictionary.keys() : return all the keys into the dictionary
    dictionary.values() : return all the values into the dictionary
    dictionary.get(key) : return the value from the dictionary according to the value
    dictionary.update({key:value}) : update/add into the dictionary
    del dictionary[key] : delete the (key, value) pair from dictionary
    dictionary.pop(key) : delete the (key, value) pair from dictionary
    dictionary.clear();
"""

#empty dictionary
dictionary= {
    1: "Md Rakibul Hasan",
    2: "Md Anwar Hossen",
    "queen": "Fahima Ritu",
    "next queen" : "Farhana Bristy",
    "king": "Rakib Hasan"
}
print(type(dictionary))
print(dictionary)
rakib = {"2016000000009":
             {
                 "name": "Md Rakibul Hasan",
                 "age": 20,
                 "gender" : "male"
             }
         }

dictionary.update(rakib)

print(dictionary["2016000000009"])
print(dictionary["2016000000009"]["name"])

dictionary.pop("2016000000009")
del dictionary["next queen"]

print(dictionary)
print(dictionary["king"])
print(dictionary["queen"])
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
