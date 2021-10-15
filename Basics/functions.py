#To start a function first write 'def [name of function]():'
#Code under function would execute only if correct indentation is followed.

def say_hi():               #basic function
    print("Hi User")

say_hi()        #calling the function

def say_name(name):         #parameterizing the function
    print("Hello " + name)

say_name("Saurabh")         #passing the value for name parameter


#Return statement usage

def cube(num):
    return num*num*num       #return back the value, you cannot write/execute code after writing return.

result = cube(3)
print(result)
