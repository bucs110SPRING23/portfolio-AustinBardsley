def multiplication(x,y):
    """
    multiplies two numbers
    args: x,y
    return: int 
    """
    total = 0
    for i in range(x):
        total += y
    return total

def exponentiation(x,y):
    """
    takes x to the power of y
    args: x,y
    return: int
    """
    total = 1
    for i in range(y):
        total *= x
    return total

def square(x):
    """
    squares x
    args: x
    return: int
    """
    return x*x


def main():
    result = (multiplication(7,5))
    print(result)
    result = exponentiation(3,4)
    print(result)    
    result = (square(25))
    print(result)

main()