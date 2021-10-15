
#2D LIST
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1])            #accesing value from 2D list, list_name[row][coloumn]

#Nested for loop

for row in number_grid:             #accesing all the rows of the 2D list
    print(row)

for row in number_grid:             #accesing all the rows of the 2D list
    for col in row:                 #accesing all the col values of accessed row of the 2D list
        print(col)
