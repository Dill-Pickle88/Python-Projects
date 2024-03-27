def num_Sqr(x):
    """
    returns a number sqaured
    :param x: int/float
    """
    return x ** 2

print(num_Sqr(6.2))

def my_String(string):
    """
    prints the string that is passed
    as a param
    :param string: str
    """
    print(string)

print(my_String("test"))


def params(a, b, c, x=5, y=10):
    """
    returns the sum of all the values of each parameter passed
    :param a, b, c, x, y: int
    x and y have optional params
    """
    return a + b + b + x + y

print(params(10, 20, 30))

def int_fuc(x):
    """
    returns an int divded by 2
    :param x: int
    """
    return int(x) / 2

def second_int_func(y):
    """
    returns a int multipled by 4
    :param y: int
    """
    return int(y) * 4

result = int_fuc(4)
print(second_int_func(result))

def covert_to_float(string):
    """
    converts a string parameter to a floating number
    :param string: string
    accounts for values errors
    """
    try:
        return float(string)
    except (ValueError):
        print("Sorry not a value number")

result = covert_to_float("Not a number")
print(result)
