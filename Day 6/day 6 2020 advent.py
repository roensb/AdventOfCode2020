def countMatch(group):
    total = 0
    letters = "abcdefghijklmnopqrstuvwxyz"
    for char in letters:
        matching = [s for s in group if char in s]
        if len(matching) == len(group):
            total +=1
    return total

file = open("data.txt", "r")
group = []
total = 0
counts ={}

for line in file:
    if line.strip() == "":
        total += countMatch(group)
        group = []
    else :
        group.append(line.strip())
total += countMatch(group) 
print ("Answer: " + str(total))



