def f(x, y, z):
    return x + y + z

result = f(1, 2, 3)
print(result)

def f():
    z = 1 + 1

result = f()
print(result)

def f(x=2):
    return x**x
print(f())
print(f(4))

def add_it(x, y=10):
    return x + y

result = add_it(2)
print(result)

x = 100

def f():
    global x
    x += 1
    print(x)

f()


def even_odd():
    n = input("type a number:")
    n = int(n)
    if n % 2 == 0:
        print("even")
    else:
        print("odd")

even_odd()
even_odd()
even_odd()

age = input("Enter your age:")
int_age = int(age)
if int_age < 21:
    print("You are young!")
else:
    print("Wow, you are old!")

try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    print(a/b)
except (ZeroDivisionError,
        ValueError):
    print("Invalid input")
    
    
