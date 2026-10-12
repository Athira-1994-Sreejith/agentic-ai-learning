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

def fiz_buz(j,a=3,b=5):
    for i in range(1,j+1):
        if i % a == 0 and i % b == 0:
            print("FizzBuzz")
        elif i % a == 0:
            print("Fizz")
        elif i % b == 0:
            print("Buzz")
        else:
            print(i)

fiz_buz(30,3,5)
fiz_buz(30, 4, 6)