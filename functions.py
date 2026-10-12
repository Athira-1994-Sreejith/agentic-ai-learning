def greet(name):
    print(f"Hello, {name}")

greet("Athira")
greet("Sreejith")


def add(a,b):
    return a+b

result =add(5,10)
print(result)

def even(num):
    return  num % 2 == 0
        

print(even(4))  # True
print(even(5))  # False


def reverse_string(s):
    return s[::-1]

reverse = reverse_string("Athira")
print(reverse)  # Output: "arihA"

def fizz_buzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizz_buzz(30)