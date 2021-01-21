# Week 2, Numbers and Strings

The assignment for our week 2 project is to:
    - Generate a list of names.
    - Manipulate the list of names into first initial, first 3 letters of last name and a random number.

We are required to use a loop function in order to achieve this. The code I used in my program is as follows:

```python
names = ["Domenico Galati", "Duane Marshall", "Collin Duffy", "Skylar Aguado", "Collin Berney"]
numbers = [0,1,2,3,4]
size = len(names)

for i in numbers:
    temp = names[i].split(" ")
    firstName = temp[0]
    lastName = temp[1]
    print(str(i) +": " + firstName[0] + " " + lastName[0:3])
```
