try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError as e:
    print("Error:", e)
    print("Invalid input! Please enter a valid integer.")

try:
    num1= int(input("Enter first number: "))
    num2= int(input("Enter second number: "))
    print(f"You entered: {num1} and {num2}")
    print(num1/num2)

except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("cannot be divided by zero")

try:
    dress = ["shirt", "pant", "t-shirt", "jeans"]
    print(dress[4])
except IndexError as e:
    print("Error:", e)
    print("Index out of range! Please enter a valid index.")

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

print(divide_numbers(10, 2))  # Output: 5.0
print(divide_numbers(10, 0))  # Output: Error message and None
print(divide_numbers(0, 5))  # Output: 2.0