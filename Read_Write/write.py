
employee_file = open("employees.txt", 'a')          #opening a file in append mode

#employee_file.write("Toby - Human Resources")          #appending a new entry in the file
employee_file.write("\nKelly - Customer Services")      #appending in a new line in the file

employee_file.close()

#Using write function to create and write in a new file
new_employee = open("new_employee.txt", 'w')

new_employee.write("This is new file for employees")

new_employee.close()
