name = input("Enter your name: ")
rev_text = ""
for ch in name:
  rev_text = ch+ rev_text
print(rev_text)
print(name[::3])
print(name[::-3])


word = "Python"
print(word[0])
print(word[-1])     # last character (negative index pinnil ninnu)
print(word[1:4])
print(word[::-1])