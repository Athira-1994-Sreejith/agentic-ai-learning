import json

employee = {
    "name": "John Doe",
    "experience": 5,
    "skills": ["Python", "JavaScript", "SQL"]
}

with open("employee.json", "w") as f:
    json.dump(employee, f)

with open("employee.json", "r") as f:
    loaded_employee = json.load(f)
    print(loaded_employee)


print("Employee Name:", loaded_employee["name"])
print("skills:", loaded_employee["skills"][0])