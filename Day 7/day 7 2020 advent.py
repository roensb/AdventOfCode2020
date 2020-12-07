file = open("data.txt", "r")

def findBags(search, bags, foundBags):
    for bag in bags:
        if not(isinstance(bags[bag], dict)):
            continue
        elif search in bags[bag].keys():
            if bag in foundBags:
                continue
            else:
                foundBags.append(bag)
                foundBags = findBags(bag, bags, foundBags)
    return foundBags

def findBagsP2(search, bags, count):
    if bags[search] == "no other":
        return 0
    bagsBelow = 0
    countCur = 0
    for bag in bags[search]:
        bagsBelow = findBagsP2(bag, bags,0)
        count += int(bags[search][bag]) + int(bags[search][bag])*bagsBelow
    return count

combinations ={}
for line in file:
    container, bags =line.strip().split("bags contain")
    bags = bags.replace(".","").replace("bags","bag").replace("bag","").split(",")
    combinations[container.strip()] = {}
    for bag in bags:
        if "no other" in bag:
            combinations[container.strip()] = "no other"
        else:
            combinations[container.strip()][bag.strip()[1:].strip()] = bag.strip()[0]

        
count = findBags("shiny gold", combinations, [])
count2 = findBagsP2("shiny gold", combinations, 0)
print (len(count))
print (count2) 




