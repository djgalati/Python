import json
with open("UN.txt") as file:
    longDictionary = {}
    for line in file:
        temp = line.strip()
        temp = temp.split(",")
        temp[0] = str(temp[0]+', '+temp[1])
        temp[1] = (temp[3] + '\t\t' +temp[2])
        longDictionary.update({temp[0]:temp[1]})
file.close()

print("All Countries sorted by Name")
print()
print("Country, Continent\t\t\tPopulation\t(some number)")
print("======================================================================")

for key in sorted(longDictionary):
    print (key, "\t\t\t", longDictionary[key])

with open("UN_sub.txt") as file:
    shortDictionary = {}
    for line in file:
        temp = line.strip()
        temp = temp.split(",")
        temp[0] = str(temp[0]+', '+temp[1])
        temp[1] = (temp[3] + '\t\t' +temp[2])
        shortDictionary.update({temp[0]:temp[1]})
file.close()

print("All Countries sorted by Name (Short List")
print()
print("Country, Continent\t\t\tPopulation\t(some number)")
print("======================================================================")

for key in sorted(shortDictionary):
    print (key, "\t\t\t", shortDictionary[key])


newFile = open('stateswpopn.bin', 'wb+')
newFile.write(json.dumps(longDictionary).encode('utf-8'))
newFile.write(json.dumps(shortDictionary).encode('utf-8'))
newFile.close()

