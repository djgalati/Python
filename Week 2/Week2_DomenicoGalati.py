names = ["Domenico Galati", "Duane Marshall", "Collin Duffy", "Skylar Aguado", "Collin Berney"]
numbers = [0,1,2,3,4]
size = len(names)

for i in numbers:
    temp = names[i].split(" ")
    firstName = temp[0]
    lastName = temp[1]
    print(str(i) +": " + firstName[0] + " " + lastName[0:3])
