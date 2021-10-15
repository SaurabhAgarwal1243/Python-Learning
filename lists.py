#You can put anything into a list(int,float,string,boolean)
friends = ["kevin", "karen", "jim", "kelly", "jerry", "tom"]
print(friends)

print(friends[2]) #accesing particular value from list
print(friends[-1]) #reverse indexing

print(friends[1:])  #accessing all the elements after index 1 till end of the list
print(friends[1:4])  #accessing all the elements between index 1 and 4(excluding 4)
print(friends[:2])  #accessing all the elements from start of the list to index 2
print(friends[0:])  #accessing all the elements of the list

friends[1] = "Mike" #modifying the list element at index 1
print(friends)

#List functions

lucky_numbers = [4, 8, 15, 16, 88, 32]

friends.extend(lucky_numbers)       #appending lucky_numbers list into friends list
print(friends)

friends.append("creed")             #appending a single value into the list
print(friends)

friends.insert(1, "kelly")          #inserting new value at index 1 and pushing the rest ahead
print(friends)

friends.remove("jim")               #removing a particular value from list
print(friends)

friends.pop()                       #this pops the last element from the list
print(friends)

print(friends.index("tom"))         #to check at which index the value kevin is present

print(friends.count("kelly"))       #check the number of times a particular value is present in the list

number = [4, 8, 15, 16, 23, 2, 12, 88, 32]
number.sort()                 #sorting the list in asscending order
print(number)

number.reverse()              #reversing the list
print(number)

friends2 = friends.copy()           #copying one list to another
print(friends2)

friends.clear()                     #clearing the whole list and receiving blank list
print(friends)


#Tuples are basically lists with immutability i.e they cannot be modified in anyway possible once created.
#Tuples are used to create a data which does not need to be modified.
#Tuples can have different data types in a single tuple.

coordinates = (4, 5)
print(coordinates[0])       #accessing elements of a tuple

