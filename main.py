from snake import Snake
from grid import Grid,Direction

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
print("---------------------------------------")
print("Grid :\n")
for x in range(len(grid)) :
    for y in range(len(grid[x])) :
        grid[x][y]
        print(grid[x][y],end=" ")
    print("\n")
print("---------------------------------------")
# loop through the grid to find the largest number, ignoring some values
past_largest_numbers = []
def find_largest():
    max = 0
    max_x = 0
    max_y = 0
    for x in range(len(grid)) :
        for y in range(len(grid[x])) :
            if grid[x][y] != "*" :
                if (x,y) not in past_largest_numbers and int(grid[x][y]) > max :
                    max = int(grid[x][y])
                    max_x = x
                    max_y = y
    #print("largest (x,y) is " + str(max) + " at location (" + str(max_x) + "," + str(max_y) + ")" )
    return max,max_x,max_y

glob_grid = Grid(grid)

for i in range(number_of_snakes):
    start,x,y = find_largest()
    past_largest_numbers.append((x,y))

    s = Snake(grid=glob_grid)
    s.create_interactive(snake_lengths[i],(x,y))
    print(f"Starting Snake with Length : {str(snake_lengths[i])} at location ({str(x)},{str(y)})")
    print(f"This snake can move in these boxes {[glob_grid.grid_weigths[id] for id in s.int_options()]}")
    s.int_mv_seg(Direction.U)
    print(f"Snake moved Upwards")
    print(f"This snake can move in these boxes {[glob_grid.grid_weigths[id] for id in s.int_options()]}")
    exit()

