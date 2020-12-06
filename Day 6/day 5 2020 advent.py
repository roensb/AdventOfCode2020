
file = open("data.txt", "r")

group = []
total = 0
counts ={}
letters = "abcdefghijklmnopqrstuvwxyz"
for line in file:
    if line.strip() == "":
        for char in letters:
            matching = [s for s in group if char in s]
            if len(matching) == len(group):
                total +=1  
        group = []
    else :
        group.append(line.strip())
for char in letters:
    matching = [s for s in group if char in s]
    if len(matching) == len(group):
        total +=1  
print ("Answer: " + str(total))



