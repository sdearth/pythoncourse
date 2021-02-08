from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(logo)
    num1 = float(input("what's the first number? "))
    should_continue = True
    result = num1

    while should_continue:
        operation = input(f"Which operation ({', '.join(operations.keys())})? ")
        num2 = float(input("What's the next number? "))
        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        num1 = result
        if input(f"press y to continue calculating with {result}, or n to exit: ") == 'y':
            num1 = result
        else:
            if input(f"press y to start a new calculation, or n to quit the program: ") == 'y':
                calculator()
            else:
                should_continue = False

calculator()