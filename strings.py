print("Hi this is\na sting")    #\n is for next line
print("Hi this is\"a sting")    #\" is for quatation mark in between

phrase = "This is a String"     #sting in a variable
print(phrase)
print(phrase + " which is Cool")     #concatenation

print(phrase.lower())       #function to convert string to lowercase
print(phrase.upper())       #function to convert string to uppercase

print(phrase.islower())     #function to check if string is in lowercase
print(phrase.isupper())     #function to check if string is in uppercase

print(phrase.upper().isupper())     #function to check if string is in uppercase after converting to uppercase

print(len(phrase))      #length of the string

print(phrase[0])        #accessing the 1st character of string

print(phrase[1:6])      #accessing a set of characters from the string

print(phrase.index("s"))    #accessing the index of the character from string
print(phrase.index("Str"))  #accessing the index from where the string starts

print(phrase.replace("is","will"))  #replacing the particular string.
