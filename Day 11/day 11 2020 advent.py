
def checkAdj(seats, row, col, seat):
    N, S, E, W, NW, NE ,SE, SW = "","","","","","","",""
    for x in range(row+1, len(seats)):
        if not (seats[x][col] == "."):
            S = seats[x][col]
            break
    for x in range(row-1, -1, -1):
        if not (seats[x][col] == "."):
            N = seats[x][col]
            break
    for y in range(col+1, len(seats[0])):
        if not (seats[row][y] == "."):
            E = seats[row][y]
            break
    for y in range(col-1, -1, -1):
        if not (seats[row][y] == "."):
            W = seats[row][y]
            break
    for i, x in enumerate(range(row-1, -1, -1)):
        y = col + i + 1
        if y >= len(seats[0]):
            break
        if not (seats[x][y] == "."):
            NE = seats[x][y]
            break
    for i, x in enumerate(range(row-1, -1, -1)):
        y = col - i - 1
        if y < 0:
            break
        if not (seats[x][y] == "."):
            NW = seats[x][y]
            break
    for i, x in enumerate(range(row+1, len(seats))):
        y = col - i - 1
        if y < 0:
            break
        if not (seats[x][y] == "."):
            SW = seats[x][y]
            break
    for i, x in enumerate(range(row+1, len(seats))):
        y = col + i + 1
        if y >= len(seats[0]):
            break
        if not (seats[x][y] == "."):
            SE = seats[x][y]
            break
    adjacent = [N, S, E , W, NE, NW, SE, SW]
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





