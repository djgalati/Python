# Week 5, Working with Files

The assignment for our week 5 project is to:

    - Use the attached text file, namelist.txt
    - Write a program that opens the file and writes the lines out to the screen in the manner that you did on previous assignments
    - Limit that data to Freshman only.
  
# Source Code  
  
The code I used in my program 

```python
with open("namelist.txt") as file:
    print("All Students")
    print()
    print("Name\t\tYear\t\tAge\tGPA")
    print("====================================================")
    for line in file:
        print(line.strip())
file.close()

print("\n\n")

with open("namelist.txt") as file:
    print("Freshman Students")
    print()
    print("Name\t\tYear\t\tAge\tGPA")
    print("===========================================")
    for line in file:
        if "Freshman" in line:
            print(line.strip())
file.close()
```
# Output

```Output
All Students

Name		Year		Age	GPA
====================================================
Duane Marshall	Freshman	25	3.0
Howard Thomas	Sophomore	63	3.75
Betsy Randolf	Senior		120	3.8
Nancy Bloom	Freshman        30	3.3
Doug Hammersmith	Junior		85	2.75
Rebecca Smith	Freshman	20	2.9



Freshman Students

Name		Year		Age	GPA
===========================================
Duane Marshall	Freshman	25	3.0
Nancy Bloom	Freshman        30	3.3
Rebecca Smith	Freshman	20	2.9
```
