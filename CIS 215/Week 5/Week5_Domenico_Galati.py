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
