def Valid(values, target):
    for value in values:
        search = target - value
        if search in values:
            return True
    return False

def search(values, found):
    window = []
    total = 0
    for value in values:
        if found == total:
            result = min(window) + max(window)
            return result
        window.append(value)
        total = sum(window)
        while total > found:
            window.pop(0)
            total = sum(window)

file = open("data.txt", "r")
values = []
preamble = 25
found = None
for line in file:
    values.append(int(line.strip()))
for i, value in enumerate(values):
    if i-preamble < 0 :
        continue
    if not(Valid(values[i-preamble:i], value)):
        found = value
        break
if found is None:
    found = values[-1]

result = search(values, found)

print ("P1:" +str(found))
print ("P2:" +str(result))





