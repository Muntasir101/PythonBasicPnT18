# function definition
def function1():
    print("Function1 called")  # function body


function1()  # calling function


# function with single parameter
def greet(name):
    print(f"Hi {name}")


greet("Green")


# function with multiple parameters
def summation(number1, number2):
    print("Sum:", number1 + number2)


summation(20, 10)  # function calling with arguments


def subtraction(number1, number2):
    return number1 - number2


result = subtraction(30, 20)
# print(result)
print(subtraction(30, 20))


# function with default parameters
def multiplication(number1=10, number2=20):
    return number1 * number2


print(multiplication(50, 10))

