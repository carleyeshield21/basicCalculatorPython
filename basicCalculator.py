def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return (n1 - n2)

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return (n1 / n2)

operation = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    num1 = int(input('Type the first number\n'))

    should_continue = True
    while should_continue:
        for operator in operation:
            print(operator)
        operation_symbol = input('Pick an operation from above: ')
        num2 = int(input('Type the second number\n'))

        calc_function = operation[operation_symbol]
        result = calc_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {result}')

        next_choice = input(f"Type 'y' to continue calculating with {result}, press Enter to make a new calculation or 'n' to exit:\n")

        if next_choice == 'y':
            num1 = result
        elif next_choice == 'n':
            should_continue = False
            break
        else:
            calculator()
            # break
calculator()