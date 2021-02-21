import json
with open("stateswpopn.txt") as file:
    stateDictionary = {}
    for line in file:
        temp = line.strip()
        temp = temp.split("\t")
        temp[1] = int(temp[1])
        stateDictionary.update({temp[0]:temp[1]})
file.close()

print("All States sorted by Name")
print()
print("State\t\t\tPopulation")
print("=======================================")
for key in sorted(stateDictionary):
    print (key, "\t\t", stateDictionary[key])


print("All States sorted by population")
print()
print("State\t\t\tPopulation")
print("=======================================")
for key,value in sorted(stateDictionary.items(), key=lambda items: items[1], \
                        reverse=True):
    print(key,"\t\t", value)

print("Top 10 Populated States")
print()
print("State\t\t\tPopulation")
print("=======================================")
for key,value in sorted(stateDictionary.items(), key=lambda items: items[1], \
                        reverse=True)[:10]:
        print(key,"\t\t", value)

newFile = open('stateswpopn.bin', 'wb+')
newFile.write(json.dumps(stateDictionary).encode('utf-8'))
newFile.close()
