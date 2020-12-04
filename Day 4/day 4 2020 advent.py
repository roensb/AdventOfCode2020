def checkValid(passport, ppList):
    valid = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    eclValid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for key in valid:
        if key in passport:
            passport['valid'] = True 
        else:
            passport['valid'] = False
            break
    if passport['valid']:
        if not(len(passport['byr']) == 4 and (1920 <= int(passport['byr']) <= 2002)):
            passport['valid'] = False
        elif not(len(passport['iyr']) == 4 and (2010 <= int(passport['iyr']) <= 2020)):
            passport['valid'] = False
        elif not(len(passport['eyr']) == 4 and (2020 <= int(passport['eyr']) <= 2030)):
            passport['valid'] = False
        elif not(passport['hgt'][-2:] == "cm" and (150 <= int(passport['hgt'][:-2]) <= 193) or (passport['hgt'][-2:] == "in" and (59 <= int(passport['hgt'][:-2]) <= 76))):
            passport['valid'] = False
        elif not(len(passport['hcl']) == 7 and passport['hcl'][0] == "#" and passport['hcl'][1:].isalnum()):
            passport['valid'] = False
        elif not(passport['ecl'] in eclValid):
            passport['valid'] = False
        elif not(len(passport['pid']) == 9 and passport['pid'].isnumeric()):
            passport['valid'] = False
    if passport['valid']:
        ppList.append(passport)
    return ppList

file = open("data.txt", "r")
passport ={}
ppList = []

for i, line in enumerate(file):
    if line.strip() == "":
        ppList = checkValid(passport, ppList)
        passport = {}
        
    else :
        pairs = line.strip().split(" ")
        for pair in pairs:
            passport[pair.split(":")[0]] = pair.split(":")[1]
 
ppList = checkValid(passport, ppList)
totalValid = len(ppList) 
print (totalValid)



