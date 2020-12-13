import math
from sympy.ntheory.modular import crt
file = open("data.txt", "r")
file = file.readlines()
time = int(file[0].strip())
buses = file[1].strip().split(",")
busesInt = [int(x) for x in buses if x != "x"] 
closest = 1
first = 0
remain = []
for i, bus in enumerate(buses):
    if bus != "x":
      remain.append(int(bus)-i)
      
print(crt(busesInt, remain))


for value in busesInt:
    if math.ceil(time/int(value)) < math.ceil(time/closest):
        closest = int(value)

bustime = closest*math.ceil(time/closest)
wait = bustime - time

   
print ("p1:" + str(wait*closest))
    

