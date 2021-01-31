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
