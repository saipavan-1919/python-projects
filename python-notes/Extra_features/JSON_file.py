"""
    JSON files:
        JSON stands for JavaScript object notation
        A JSON file stores data in key-value pairs and arrays; the software it was made for then accesses the data. 
        JSON allows developers to store various data types as human-readable code, with the keys serving as names and the values containing related data.
        * Data is in key/value pairs
        * Data is separated by commas
        * Curly braces hold objects
        * Square brackets hold arrays
        * key should be enclosed in the double quotes

        ex:
            {
                "name":"sai",
                "age":23,
                "sports":["cricket", "badminton"]
            }
        * A JSON file is similar to the dictionaty data type in the pyhton
        * json.load method returns the json data as a dictionary object in python.
        * so that we can access the data in the json file with dictionary notation
"""

import json

# we can open the json file using the open function
f = open("sample.json",'r')

# json.load method returns the data in the json file as a dictionary
# so we can access the data in the json file using dictionary notation
data = json.load(f)
print(type(data))
print(data["sports"][1])
a = data["sports"][0]
print(type(a))
print(type(data["sports"]))

# we need to close the file after using it
f.close()
