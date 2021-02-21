# Week 6, Dictionaries

The assignment for our week 6 project is to:

    - Create a dictionary from the text file stateswpopn.txt
    - Sort that dictionary based on:
        - State name
        - Population
    - Return the top 10 most populated states with their population in a simple table.
    - Store this dictionary as a binary file.
  
# Source Code  
  
The code I used in my program 

```python
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

```
# Output

```Output
All States sorted by Name

State			Population
=======================================
Alabama 		 4874747
Alaska 		 739795
Arizona 		 7016270
Arkansas 		 3004279
California 		 39536653
Colorado 		 5607154
Connecticut 		 3588184
Delaware 		 961939
District of Columbia 		 693972
Florida 		 20984400
Georgia 		 10429379
Hawaii 		 1427538
Idaho 		 1716943
Illinois 		 12802023
Indiana 		 6666818
Iowa 		 3145711
Kansas 		 2913123
Kentucky 		 4454189
Louisiana 		 4684333
Maine 		 1335907
Maryland 		 6052177
Massachusetts 		 6859819
Michigan 		 9962311
Minnesota 		 5576606
Mississippi 		 2984100
Missouri 		 6113532
Montana 		 1050493
Nebraska 		 1920076
Nevada 		 2998039
New Hampshire 		 1342795
New Jersey 		 9005644
New Mexico 		 2088070
New York 		 19849399
North Carolina 		 10273419
North Dakota 		 755393
Ohio 		 11658609
Oklahoma 		 3930864
Oregon 		 4142776
Pennsylvania 		 12805537
Puerto Rico 		 3337177
Rhode Island 		 1059639
South Carolina 		 5024369
South Dakota 		 869666
Tennessee 		 6715984
Texas 		 28304596
Utah 		 3101833
Vermont 		 623657
Virginia 		 8470020
Washington 		 7405743
West Virginia 		 1815857
Wisconsin 		 5795483
Wyoming 		 579315
All States sorted by population

State			Population
=======================================
California 		 39536653
Texas 		 28304596
Florida 		 20984400
New York 		 19849399
Pennsylvania 		 12805537
Illinois 		 12802023
Ohio 		 11658609
Georgia 		 10429379
North Carolina 		 10273419
Michigan 		 9962311
New Jersey 		 9005644
Virginia 		 8470020
Washington 		 7405743
Arizona 		 7016270
Massachusetts 		 6859819
Tennessee 		 6715984
Indiana 		 6666818
Missouri 		 6113532
Maryland 		 6052177
Wisconsin 		 5795483
Colorado 		 5607154
Minnesota 		 5576606
South Carolina 		 5024369
Alabama 		 4874747
Louisiana 		 4684333
Kentucky 		 4454189
Oregon 		 4142776
Oklahoma 		 3930864
Connecticut 		 3588184
Puerto Rico 		 3337177
Iowa 		 3145711
Utah 		 3101833
Arkansas 		 3004279
Nevada 		 2998039
Mississippi 		 2984100
Kansas 		 2913123
New Mexico 		 2088070
Nebraska 		 1920076
West Virginia 		 1815857
Idaho 		 1716943
Hawaii 		 1427538
New Hampshire 		 1342795
Maine 		 1335907
Rhode Island 		 1059639
Montana 		 1050493
Delaware 		 961939
South Dakota 		 869666
North Dakota 		 755393
Alaska 		 739795
District of Columbia 		 693972
Vermont 		 623657
Wyoming 		 579315
Top 10 Populated States

State			Population
=======================================
California 		 39536653
Texas 		 28304596
Florida 		 20984400
New York 		 19849399
Pennsylvania 		 12805537
Illinois 		 12802023
Ohio 		 11658609
Georgia 		 10429379
North Carolina 		 10273419
Michigan 		 9962311
```
along with the file stateswpopn.bin
