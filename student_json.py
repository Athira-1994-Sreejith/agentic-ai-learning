import json

students = ["Archana", "Athira", "Sreejith"]

with open("students.json", "w") as f:
    json.dump(students, f)

with open("students.json", "r") as f:
    data = json.load(f)

for name in data:
    print(name)

students = ["Archana", "Athira", "Sreejith"]

with open("students.txt", "w") as f:
    for name in students:
        f.write(name + "\n")

with open("students.txt", "r") as f:
    for line in f:
        print(line.strip())

with open("students.txt", "a") as f:
       f.write("Anu\n")
     