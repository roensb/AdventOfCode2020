
class ship():
    def __init__(self):
        self.xy = [0,0]
        self.waypoint = [10,1]
        
    def convDir(self,direction):
        switch = {"E": [1, 0],
                  "N": [0, 1],
                  "S": [0, -1],
                  "W": [-1,0]}
        if direction in switch:
            return switch[direction]
        
    def move(self, direction, value):
        rotate = ["L", "R"]
        if direction in rotate:
            delta = int(value/90)
            if direction == "L":
                for value in range(delta):
                    self.waypoint = [self.waypoint[1]*-1, self.waypoint[0]] 
            if direction == "R":
                for value in range(delta):
                    self.waypoint = [self.waypoint[1], self.waypoint[0]*-1]
        elif direction == "F":
            self.xy = [self.xy[0] + value*self.waypoint[0], self.xy[1] + value*self.waypoint[1]] 

        else:
            adjust = [x*value for x in self.convDir(direction)]
            self.waypoint = [self.waypoint[0] +adjust[0], self.waypoint[1] +adjust[1]] 
        
    def getDist(self):
        return (abs(self.xy[0]) + abs(self.xy[1]))

file = open("data.txt", "r")
direction =[]
ship = ship()
for line in file:
    line = line.strip()
    ship.move(line[0], int(line[1:]))

print (ship.getDist())
    

