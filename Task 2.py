# Calculator 

print('Calculator!!')

# Taking input from the user
number1 = int(input('Enter number1: '))
number2 = int(input('Enter number2: '))

# Displaying operation choices
print('Press 1 for Addition Operation')
print('Press 2 for Subtraction Operation')
print('Press 3 for Multiplication Operation')
print('Press 4 for Division Operation')
print('Press 5 for Exponential Operation')
print('Press 6 to get Remainder')

# Function for addition
def addition(number1, number2):
    total = number1 + number2
    return total

# Function for subtraction
def subtraction(number1, number2):
    difference = number1 - number2
    return difference

# Function for multiplication
def multiplication(number1, number2):
    final = number1 * number2
    return final

# Function for division with zero check
def division(number1, number2):
    if number2 == 0:
        return "Division by zero is invalid!"
    dividedno = number1 / number2
    return dividedno

# Function for exponentiation
def power(number1, number2):
    exp = number1 ** number2
    return exp

# Function to calculate remainder
def remainder(number1, number2):
    mod = number1 % number2
    return mod

# Asking user to select an operation
selectedno = int(input('Enter the no for the operation to be performed: '))

# Performing the selected operation
if selectedno == 1:
    print('Result:', addition(number1, number2))
elif selectedno == 2:
    print('Result:', subtraction(number1, number2))
elif selectedno == 3:
    print('Result:', multiplication(number1, number2))
elif selectedno == 4:
    print('Result:', division(number1, number2))
elif selectedno == 5:
    print('Result:', power(number1, number2))
elif selectedno == 6:
    print('Result:', remainder(number1, number2))
else:
    print('Invalid number selected!')