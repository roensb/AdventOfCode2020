import time
start_time = time.time()
def valid(values, target):
    for value in values:
        search = target - value
        if search in values:
            return True
    return False

def search(values, found):
    window = []
    for value in values:
        if found == sum(window):
            result = min(window) + max(window)
            return result
        window.append(value)
        while sum(window) > found:
            window.pop(0)


file = open("data.txt", "r")
values = []
preamble = 25
found = None
for line in file:
    values.append(int(line.strip()))
for i, value in enumerate(values):
    if i-preamble < 0 :
        continue
    if not(valid(values[i-preamble:i], value)):
        found = value
        break
if found is None:
    found = values[-1]

result = search(values, found)

print ("P1:" +str(found))
print ("P2:" +str(result))
print("--- %s seconds ---" % (time.time() - start_time))





