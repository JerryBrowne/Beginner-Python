def get_input_from_user():
    num1 = input("Number 1: ")
    num2 = input("Number 2: ")

    num1 = int(num1)
    num2 = int(num2)

    operator = input("Operator: ")

    return num1, num2, operator

def perform_calculation(num1, num2, operator):
    if operator == "+":
        print(num1 + num2)

    elif operator == "-":
        print(num1 - num2)

    elif operator == "*":
        print(num1 * num2)

    elif operator == "/":
        print(num1 / num2)

        

number1, number2, op = get_input_from_user()
perform_calculation(number1, number2, op)



