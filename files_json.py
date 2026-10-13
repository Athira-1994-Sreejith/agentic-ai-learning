
with open("notes.txt", "w") as f:
    f.write("This is a sample note\n")
    f.write("This is another line in the note.\n")

with open("notes.txt", "r") as f:
    content = f.read()
    print(content)