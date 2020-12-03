import time
import re
from functools import reduce

start_time = time.time()
file = open("data.txt", "r")
counts = [0,0,0,0,0]
rights = [0,0,0,0,0]
slopes = [1,3,5,7,1]
skippedIndex = 4
for i, line in enumerate(file) :
    if i == 0:
        continue
    length = len(line.strip())
    for j, slope in enumerate(slopes):
        if j == skippedIndex and i%2:
            continue
        rights[j] += slope
        if rights[j] >= length:
            rights[j] = rights[j] - length
        if line[rights[j]] == "#":
            counts[j] +=1

count = reduce((lambda x, y: x * y), counts)

print ("P1:" + str(counts[1]))
print ("P2:" + str(count))


print("--- %s seconds ---" % (time.time() - start_time))
