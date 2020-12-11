
def checkAdj(seats, row, col, seat):
    adjacent = []
    #south
    for x in range(row+1, len(seats)):
        if not (seats[x][col] == "."):
            adjacent.append(seats[x][col])
            break
    #north
    for x in range(row-1, -1, -1):
        if not (seats[x][col] == "."):
            adjacent.append(seats[x][col])
            break
    #east
    for y in range(col+1, len(seats[0])):
        if not (seats[row][y] == "."):
            adjacent.append(seats[row][y])
            break
    #west
    for y in range(col-1, -1, -1):
        if not (seats[row][y] == "."):
            adjacent.append(seats[row][y])
            break
    #NE
    for i, x in enumerate(range(row-1, -1, -1)):
        y = col + i + 1
        if y >= len(seats[0]):
            break
        if not (seats[x][y] == "."):
            adjacent.append(seats[x][y])
            break
    #NW
    for i, x in enumerate(range(row-1, -1, -1)):
        y = col - i - 1
        if y < 0:
            break
        if not (seats[x][y] == "."):
            adjacent.append(seats[x][y])
            break
    #SW
    for i, x in enumerate(range(row+1, len(seats))):
        y = col - i - 1
        if y < 0:
            break
        if not (seats[x][y] == "."):
            adjacent.append(seats[x][y])
            break
    #SE
    for i, x in enumerate(range(row+1, len(seats))):
        y = col + i + 1
        if y >= len(seats[0]):
            break
        if not (seats[x][y] == "."):
            adjacent.append(seats[x][y])
            break
    if not("#" in adjacent) and seat == "L":
        return "#"
    if adjacent.count("#") >= 5 and seat == "#":
        return "L"
    else:
        return seat

def occupy(seats):
    newSeats = []
    for i, row in enumerate(seats):
        newRow = ""
        for j, seat in enumerate(row):
            newRow += checkAdj(seats, i, j, seat)
        newSeats.append(newRow)
    if newSeats == seats:
        return seats
    else:
        seats = occupy(newSeats)

    return seats
            
file = open("data.txt", "r")
seats =[]
for line in file:
    seats.append(line.strip())

finalSeats = occupy(seats)
occupied = 0
for row in finalSeats:
    occupied += row.count("#")
print (occupied)
