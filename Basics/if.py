
is_male = False
is_tall = True

if is_male:                     #Basic if else condition
    print("you are a male")
else:
    print("you are not a male")

if is_male and is_tall:                  #OR/AND operators in if statement
    print("you are a male and tall")
else:
    print("you are not a male and not tall")

if is_male and is_tall:                  #elif statements
    print("you are a male and tall")
elif is_male and not(is_tall):
    print("you are a short male")
elif not (is_male) and is_tall:
    print("you are a tall female")
else:
    print("you are not a male and not tall")


#if statements with comparisons
# Basic comparison operators:
#   ==   'equals to'   to check if values are equal
#   !=  'not equals to'    to check if values are not equal
#   > , <   'greater than and less than'
#   >= , <=     'greater than equal to and less than equal to'
#we can compare any datatype

def max_num(num1,num2,num3):                #comparing numbers to check which is max
    if num1 >= num2 and num1 >= num3:       
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300,42,992))

