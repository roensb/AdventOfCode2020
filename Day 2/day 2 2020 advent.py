import time
import re
start_time = time.time()
    

file = open("day 2 input.txt", "r")

count = 0
count2 = 0
for line in file :
    line = line.strip(" ")
    result = line.split(":")
    minVal,maxVal = result[0][:-1].split("-")
    letter = result[0][-1]
    if result[1].count(letter)<= int(maxVal) and result[1].count(letter)>= int(minVal):
        count = count + 1
    if (result[1][int(maxVal)] == letter) ^ (result[1][int(minVal)] == letter):
        count2 = count2 + 1

print ("P1:" + str(count))
print ("P2:" + str(count2))


print("--- %s seconds ---" % (time.time() - start_time))
