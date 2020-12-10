file = open("data.txt", "r")
adapters = []

for line in file:
    adapters.append(int(line.strip()))
adapters.sort()
adapters.append(adapters[-1] + 3)
adapters.insert(0, 0)

combos = [1] + [0]*adapters[-1]
for i in adapters[1:]:
	combos[i] = combos[i-3] + combos[i-2] + combos[i-1]
print ("P2: " + str(combos[-1]))





