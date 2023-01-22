input('Hello! This is a simple calculator. To start click [Enter]') 
#import sys   sys.exit()

def valid_first_digit() -> float:
    while True:
        first_digit = input('Input first number you want operate to and click [Enter]. If you want to exit, input Exit: ')
        if first_digit == 'Exit':
            print('Goodbye')
            exit()
        try:
            return float(first_digit)
        except ValueError:
            print('Entered value invalid. Try again...')



def valid_operator() -> str:
    while True:
        operation = input('Input operation from the parentheses (+, -, *, /) and click [Enter]. If you want to exit, input Exit: ')
        if operation == 'Exit':
            print('Goodbye')
            exit()
        if operation in {'+', '-', '*', '/'}:
            return operation
        else:
            print('Entered operator invalid')


def valid_second_digit(operation: str) -> float:
    while True:
        second_digit = input('Input second number and click [Enter]. If you want to exit, input Exit: ')
        if second_digit == 'Exit':
            print('Goodbye')
            exit()
        try:
            num = float(second_digit)
            if operation == '/' and num == 0:
                raise Exception('You cant divide by zero')
            return num
        except ValueError:
            print('Entered value invalid. Try again...')
        except Exception as e:
            print(e)

def get_user_info() -> tuple[float,str, float]:
    number_1 = valid_first_digit()
    operation = valid_operator()
    number_2 = valid_second_digit(operation)
    return number_1, operation, number_2


def get_math_function(valid_operator: str):
    operations = {'+': lambda arg1, arg2: arg1 + arg2,
                  '-': lambda arg1, arg2: arg1 - arg2,
                  '*': lambda arg1, arg2: arg1 * arg2,
                  '/': lambda arg1, arg2: arg1 / arg2}
    return operations[valid_operator]

number_1, operation, number_2 = get_user_info()

math = get_math_function(operation)
rounded_result = round(math(number_1, number_2), 3)

output_message = f'{number_1} {operation} {number_2} = {rounded_result}'
print(output_message)













