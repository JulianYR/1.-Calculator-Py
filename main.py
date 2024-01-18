option = 0 
addition = 0
subtraction = 0
multiplication = 0
division = 0
division = 0
typeDivision = 0

n1 = 0
n2 = 0

while option != 6:

    option = int(input(
    '''
    Enter the number of the operation to be executed.
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. All
    6. Turn off program.
    '''))

    if option == 1:
        n1 = float(input('Enter the first digit: '))
        n2 = float(input('Enter the second digit: '))
        addition = n1 + n2
        print('The result is: ' + str(addition))
    elif option == 2:
        n1 = float(input('Enter the first digit: '))
        n2 = float(input('Enter the second digit: '))
        subtraction = n1 - n2
        print('The result is: ' + str(subtraction))
    elif option == 3:
        n1 = float(input('Enter the first digit: '))
        n2 = float(input('Enter the second digit: '))
        multiplication = n1 * n2
        print('The result is: ' + str(multiplication))
    elif option == 4:
        n1 = float(input('Enter the first digit: '))
        n2 = float(input('Enter the second digit: '))
        typeDivision = float(input(
        '''
        Integer or decimal division.
        1. Integer division
        2. Decimal division
        '''))
        if typeDivision == 1:
            division = n1 / n2 
            if division % 1 > 0.5:
                division = int(division) + 1
            else:
                division = int(division)
            print('The result is: ' + str(division))
        elif typeDivision == 2:
            division = n1 / n2
            print('The result is: ' + str(division))
    elif option == 5:
        n1 = float(input('Enter the first digit: '))
        n2 = float(input('Enter the second digit: '))
        addition = n1 + n2
        subtraction = n1 - n2
        multiplication = n1 * n2
        division = n1 / n2
        print('Addition: ' + str(addition))
        print('Subtraction: ' + str(subtraction))
        print('Multiplication: ' + str(multiplication))
        print('Division: ' + str(division))
    elif option == 6:
        print('Turning off program.')
    else :
        print('Please enter a valid value.')