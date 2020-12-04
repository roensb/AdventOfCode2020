def checkValid(passport, ppList, numFalse):
    valid = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    eclValid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for key in valid:
        if key in passport:
            passport['valid'] = True 
        else:
            passport['valid'] = False
            numFalse += 1
            break
    if passport['valid']:
        if not(len(passport['byr']) == 4 and (1920 <= int(passport['byr']) <= 2002)):
            passport['valid'] = False
            numFalse += 1
        elif not(len(passport['iyr']) == 4 and (2010 <= int(passport['iyr']) <= 2020)):
            passport['valid'] = False
            numFalse += 1
        elif not(len(passport['eyr']) == 4 and (2020 <= int(passport['eyr']) <= 2030)):
            passport['valid'] = False
            numFalse += 1
        elif not(passport['hgt'][-2:] == "cm" and (150 <= int(passport['hgt'][:-2]) <= 193) or (passport['hgt'][-2:] == "in" and (59 <= int(passport['hgt'][:-2]) <= 76))):
            passport['valid'] = False
            numFalse += 1
        elif not(len(passport['hcl']) == 7 and passport['hcl'][0] == "#" and passport['hcl'][1:].isalnum()):
            passport['valid'] = False
            numFalse += 1
        elif not(passport['ecl'] in eclValid):
            passport['valid'] = False
            numFalse += 1
        elif not(len(passport['pid']) == 9 and passport['pid'].isnumeric()):
            passport['valid'] = False
            numFalse += 1
    ppList.append(passport)
    return ppList, numFalse

file = open("data.txt", "r")
passport ={}
ppList = []
valid = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
numFalse = 0

for i, line in enumerate(file):
    if line.strip() == "":
        ppList, numFalse = checkValid(passport, ppList, numFalse)
        passport = {}
        
    else :
        pairs = line.strip().split(" ")
        for pair in pairs:
            passport[pair.split(":")[0]] = pair.split(":")[1]
 
ppList, numFalse = checkValid(passport, ppList, numFalse)
totalValid = len(ppList) - numFalse
print (totalValid)



