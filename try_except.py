'''
Scenario: Here we are asking user to input a number and converting it into an integer, but what if user enters wrong input like string,
          the code now would try to run the normal function and if there is a wrong input it would go in except and excute that code.
'''

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:           #Divide by zero error has specific except reference
    print(err)
except ValueError:                         #Invalid value error has specific except reference
    print("Invalid Input")

