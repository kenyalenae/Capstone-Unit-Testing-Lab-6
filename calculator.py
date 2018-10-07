# create a simple calculator program to be used with unit testing


# create math functions
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


# create menu for user to choose selection from
print("Basic Calculator")
print('-' * 30)
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
print('-' * 30)

# ask user which operation they would like to select
option = int(input('Which operation would you like to perform? [1-4]: '))

number1 = int(input('Please enter the first number: '))
number2 = int(input('Please enter the second number: '))

# create if/else statement to run users option
if option == 1:
    print(number1, '+', number2, '=', add(number1, number2))
elif option == 2:
    print(number1, '-', number2, '=', subtract(number1, number2))
elif option == 3:
    print(number1, '*', number2, '=', multiply(number1, number2))
elif option == 4:
    print(number1, '/', number2, '=', divide(number1, number2))
else:
    print('Invalid input')
