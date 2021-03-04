# Week 9, The Luhn Algorithm

The assignment for our week 9 project is to:

    - familiarize yourself with the Luhn algorithm
    - The code should consist of one function that takes a single argument.
    - Your function should return a boolean value, either True or False
    - Call the function appropriately at the end of your code.
  
# Source Code  
  
The code I used in my program 

```python
def runLuhnAlgorithm(nums):
    total = 0
    position = len(nums)-2
    #loop doubles every other int on the list
    while (position >= 0):
        #if # > 10, it would properly adjust the number to be 1 + the remiander
        if((int(nums[position])*2) < 10):
            nums[position] = int(nums[position])*2
        else:
            temp = int(nums[position])*2 - 10
            temp = 1+ temp
            nums[position] = temp
        position = position - 2
    #add the list 
    for item in nums:
        total = int(item) + total
    #Verifies is checksum is valid or not    
    if(total%10 == 0):
        return True
    else:
        return False
    
print("enter the full number one digit at a time. press enter with no input to\
terminate")
numbers = []
#Allows user to enter numbers untill they were finished
while(True):
    try:
        userInput = int(input("enter a number: "))
    except ValueError:
        break
    numbers.append(userInput)
#Runs the algorithm and prints the corresponding output
if(runLuhnAlgorithm(numbers)):
    print("The numbers entered are valid for the Luhn algorithm")
else:
    print("The numbers entered are invalid for the Luhn algorithm")
```
# Output

```Output
= RESTART: /Users/domenicogalati/Documents/CIS215/Week 8/Week8_Domenico_Galati.py
enter the full number one digit at a time. press enter with no input toterminate
enter a number: 1
enter a number: 2
enter a number: 3
enter a number: 4
enter a number: 5
enter a number: 6
enter a number: 7
enter a number: 8
enter a number: 1
enter a number: 2
enter a number: 3
enter a number: 4
enter a number: 5
enter a number: 6
enter a number: 7
enter a number: 0
enter a number: 
The numbers entered are valid for the Luhn algorithm
>>> 
= RESTART: /Users/domenicogalati/Documents/CIS215/Week 8/Week8_Domenico_Galati.py
enter the full number one digit at a time. press enter with no input toterminate
enter a number: 1
enter a number: 2
enter a number: 3
enter a number: 4
enter a number: 5
enter a number: 6
enter a number: 7
enter a number: 8
enter a number: 1
enter a number: 2
enter a number: 3
enter a number: 4
enter a number: 5
enter a number: 6
enter a number: 7
enter a number: 8
enter a number: 
The numbers entered are invalid for the Luhn algorithm
```
