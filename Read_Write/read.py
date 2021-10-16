'''
We are trying to read data from employees file in the same directory
'open' command opens the said file, the 1st parameter is the file location if its in different directory or name if in same directory
the 2nd parameter is the way we want to access the said file
'r': read mode (We cant modify anything in the file)
'w': write mode (We can modify the file)
'a': append mode (We can append the data in the end of file)
'r+': read and write (We can both read and write in the file)
'''

employee_file = open("employees.txt", "r")

print(employee_file.readable())         #readable functions lets us identify that the file is readable or not
print(employee_file.read())             #read functions lets us read the whole file at once
print(employee_file.readline())         #readline functions lets us read firstline in the first iteration and then reads next lines in subsequent iterations
print(employee_file.readlines())        #readlines functions lets us read the whole file and puts data in a list
print(employee_file.readlines()[1])     #accessing the first line using readlines funtions

for employee in employee_file.readlines():      #for loop to print every employee using readlines function
    print(employee)


employee_file.close()
