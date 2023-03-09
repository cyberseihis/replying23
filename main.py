
def parsing():
    f = open("input/00-example.txt", "r")
    temp = f.readlines()
    lines = []
    for line in temp:
        lines.append(line[:-1].split(' '))
    column = int(lines[0][0])
    rows = int(lines[0][1])
    number_of_snakes = int(lines[0][2])
    snake_lengths = [int(x) for x in lines[1]]
    lines.pop(0)
    lines.pop(0)
    return column,rows,number_of_snakes,snake_lengths,lines

# Get the data from the text file
column,rows,number_of_snakes,snake_lengths,grid = parsing()

# a loop through the grid
for x in range(len(grid)) :
    for y in range(len(grid[x])) :
        grid[x][y]
        print(grid[x][y],end=" ")
    print("\n")

# loop through the grid to find the first instance of the largest number
max = 0
max_x = 0
max_y = 0
for x in range(len(grid)) :
    for y in range(len(grid[x])) :
        if grid[x][y] != "*":
            if int(grid[x][y]) > max :
                max = int(grid[x][y])
                max_x = x
                max_y = y
        #print(grid[x][y],end=" ")
    #print("\n")

print("largest (x,y) is " + str(max) + " at location (" + str(max_x) + "," + str(max_y) + ")" ) 