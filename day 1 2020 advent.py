import time
start_time = time.time()

def finder(values):
    for value in values:
        search = 2020 - value
        newList = [item for item in values if item < search]
        for newValue in newList:
            search2 = 2020 - value - newValue
            if search2 in newList:
                print (newValue*value*search2)
                return

file = open("data.txt", "r")

values = []

for x in file :
	values.append(int(x))




finder(values)
print("--- %s seconds ---" % (time.time() - start_time))
