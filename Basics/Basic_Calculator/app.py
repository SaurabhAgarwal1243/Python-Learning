num1 = input("Enter your 1st number: ")
num2 = input("Enter your 2nd number: ")

#When you input a number from user by default its a string so we have to cnvert it into a number

result = int(num1) + float(num2)    #int is for whole integer and float is for decimal numbers

print(result)