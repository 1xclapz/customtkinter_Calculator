def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    num1 = float(input("First number: "))
    op = input("Operator (+ - * /): ")
    num2 = float(input("Second number: "))

    if op == "+":
        print(addition(num1, num2))
    elif op == "-":
        print(subtraction(num1, num2))
    elif op == "*":
        print(multiplication(num1, num2))
    elif op == "/":
        print(division(num1, num2))
    else:
        print("Unknown operator")