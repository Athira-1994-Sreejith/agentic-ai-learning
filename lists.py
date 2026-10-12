fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit.upper())
print(fruits[-1])
print(fruit.upper())
print(fruits[0])  # Output: apple
fruits.append("orange") 
print(fruits) # Output: None
print(len(fruits))  # Output: 3
  # Output: ['apple', 'banana', 'cherry', 'orange']