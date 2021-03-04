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
