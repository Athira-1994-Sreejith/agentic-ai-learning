employee = {
    "name": "Sreejith M V",
    "age": 36,
    "experience": 15,
    "designation": "Software Engineer",
    "location": "Bangalore",
}

print(employee["name"]);
print(employee.get("location"));


employee["location"] = ["Chennai"]
employee["location"].append("Bangalore")


print(employee)




for key, value in employee.items():
    print(f"{key}: {value}")