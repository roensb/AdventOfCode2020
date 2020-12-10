file = open("data.txt", "r")

adapters = []
curJolt = 0
num1Jolt = 0
num2Jolt = 0 
num3Jolt = 0
for line in file:
    adapters.append(int(line.strip()))
adapters.sort()
adapters.append(adapters[-1] + 3)

for adapter in adapters:
    if (adapter - curJolt) == 1:
        num1Jolt += 1
    elif(adapter - curJolt) == 2:
        num2Jolt += 1
    elif(adapter - curJolt) == 3:
        num3Jolt += 1
    curJolt = adapter

print ("P1:" +str(num1Jolt*num3Jolt))





