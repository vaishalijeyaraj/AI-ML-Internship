
student = {"name": "Anu", "age": 20, "course": "AI & DS"}
print(student["name"])
print(student.get("grade", "Not assigned"))
student["grade"] = "A"
student["age"] = 21
student.pop("course")
print(student.keys())
print(student.values())
print(student.items())
for key, value in student.items():
    print(key, "=>", value)

