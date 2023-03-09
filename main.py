
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

column,rows,number_of_snakes,snake_lengths,grid = parsing()

