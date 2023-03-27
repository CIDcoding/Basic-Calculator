#from art import logo


def add(n1, n2):
    ''' Addition '''
    return n1 + n2


def subtract(n1, n2):
    ''' subtraction '''
    return n1 - n2


def multiply(n1, n2):
    ''' multiplication '''
    return n1 * n2


def divide(n1, n2):
    ''' division '''
    return n1 / n2


''' dictionary with operation symbols'''
op = {}
op['+'] = add
op['-'] = subtract
op['*'] = multiply
op['/'] = divide


def calculator():
    #print(logo)

    ''' ask user for input '''
    num_1 = float(input('What is the first number?: '))
    # num_2 = int(input('What is the second number? '))

    ''' loop through the dictionary and print out all available operations '''
    for operation in op:
        print(operation)

    calculation = True

    while calculation:

        ''' ask user to choose the operation they want to perform '''
        operation_symbol = input('please choose an operation: ')

        ''' use the chosen operation symbol to access the corresponding value in the dictionary   (i.e. the correct function) '''
        next_num = float(input('What is the next number? '))
        calculation_function = op[operation_symbol]
        result = calculation_function(num_1, next_num)
        print(f'{num_1} {operation_symbol} {next_num} = {result}')

        ''' ask user if they would like to continue calculating'''
        ask = input(f"type 'y' to continue calculating with {result} or 'n' to start a new calculation: ").lower()
        if ask == 'n':
            calculation = False
            ''' start new calculation '''
            calculator()
            print('Goodbye')
        else:
            num_1 = result


calculator()