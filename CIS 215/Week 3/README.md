# Week 3, Create lists, output as table

The assignment for our week 3 project is to:
    
    - Create a list of this information and output this list into a table with headers.
    - Next, output a second list with only the students who are Freshmen.
    
We should be using anything we have gone over so far in class plus some control structures. The code I used in my program 

```python
Names = ["Jeff George", "Howard Thomas", "Betsy Randolf", "Nancy Bloom", "Doug Hammersmith", "Rebecca Smith"]
Year = ["Freshman", "Sophomore", "Senior", "Freshman", "Junior", "Freshman"]
Age = [25, 63, 120, 30, 85, 20]
GPA = [3.0, 3.75, 3.8, 3.3, 2.75, 2.9]
size = len(Names)
Numbers = [0,1,2,3,4,5]
print ("{:<18} {:<10} {:<4} {:<6}".format('Name', 'Year', 'Age', 'GPA'))
print ("{:<18} {:<10} {:<4} {:<6}".format('====', '====', '===', '==='))

for i in Numbers:
    print ("{:<18} {:<10} {:<4} {:<6}".format(Names[i], Year[i], Age[i], GPA[i]))

print("=======================================")
print()
print ("{:<18} {:<10} {:<4} {:<6}".format('Name', 'Year', 'Age', 'GPA'))
print ("{:<18} {:<10} {:<4} {:<6}".format('====', '====', '===', '==='))
for i in Numbers:
    if "F" in Year[i]:
        print ("{:<18} {:<10} {:<4} {:<6}".format(Names[i], Year[i], Age[i], GPA[i]))
print("=======================================")

```
