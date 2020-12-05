
def findMiddle(array):
    mid = float(len(array))/2
    return int(mid)

file = open("data.txt", "r")

seats = {}
for x in range(128):
    for y in range(8):
        seats[(x*8 +y)] = "missing"
IDs = []
for line in file:
    line =line.strip()
    rows = [ x for x in range(128)]
    cols = [ x for x in range(8)]
    for char in line:
        if char == "F":
            mid = findMiddle(rows)
            rows = rows[:mid]
        if char == "B":
            mid = findMiddle(rows)
            rows = rows[mid:]
        if char == "L":
            mid = findMiddle(cols)
            cols = cols[:mid]
        if char == "R":
            mid = findMiddle(cols)
            cols = cols[mid:]
    ID = rows[0]*8 + cols[0]
    IDs.append(ID)
    seats[ID] = "taken"
for key in seats:
    if seats[key] ==  "missing" and (7 < int(key) < 1016) and seats[key-1] == "taken" and seats[key+1] == "taken":
        myID = key
          
       
print ("P1: " + str(max(IDs)))
print ("P2: " + str(myID))



