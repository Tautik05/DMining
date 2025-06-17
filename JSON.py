#1Parse a JSON string and access nested values
import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)

print(person_dict)
print(person_dict['languages'])
#2

import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)
print(y)


#3
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#4Convert Python object with multiple data types to JSON
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))
#5 print with indent , seperator, sort the keys.
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print(json.dumps(x, indent=4, sort_keys=True))

#6 Reading JSON from a File using json.load()
#Create the file student.json , 
#enter the required input in the file:
"""{
  "name": "Asha",
  "roll": 101,
  "marks": [88, 91, 95],
  "passed": true
}"""
#save it in the same folder as python code
#source code for 6 starts here:
import json
with open("student.json", "r") as f:
    student = json.load(f)
print("Student's Marks:", student["marks"])

#7 Writing JSON to a File using json.dump()
import json

person_dict = {
    "name": "Bob",
    "languages": ["English", "French"],
    "married": True,
    "age": 32
}

with open("person.txt", "w") as json_file:
    json.dump(person_dict, json_file)
    
#8 Access nested key ‘salary’, ‘bonus’ and calculate total salary
data = {
    "SAIL": {
        "Employees": {
            "name": "DIPAK",
            "payable": {
                "salary": 50000,
                "bonus": 10000
            }
        }
    }
}

salary = data["SAIL"]["Employees"]["payable"]["salary"]
bonus = data["SAIL"]["Employees"]["payable"]["bonus"]
total_salary = salary + bonus

print(f"Salary: {salary}")
print(f"Bonus: {bonus}")
print(f"Total Salary (including Bonus): {total_salary}")


