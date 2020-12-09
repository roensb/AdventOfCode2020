import time
start_time = time.time()
def Valid(values, target):
    for value in values:
        search = target - value
        if search in values:
            return True
    return False

def search(values, found):
    for i, value in enumerate(values):
        for end in range(i+1,len(values)):
            if found == sum(values[i:end]):
                result = min(values[i:end]) + max(values[i:end])
                return result
            if found <= sum(values[i:end]):
                break

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
print("--- %s seconds ---" % (time.time() - start_time))





