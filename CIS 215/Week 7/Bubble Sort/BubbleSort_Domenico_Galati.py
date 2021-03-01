def runBubbleSort(nums):
    swap = True
    while(swap):
        swap=False
        iteration = 0
        while(iteration < 4):
            if(nums[iteration]>nums[iteration+1]):
                temp = nums[iteration]
                nums[iteration] = nums[iteration+1]
                nums[iteration+1] = temp
                swap=True
            iteration +=1
    return nums;

print("enter 5 numbers at random")
numbers = []
numbers.append(input())
numbers.append(input())
numbers.append(input())
numbers.append(input())
numbers.append(input())
numbers = runBubbleSort(numbers)
print("The sorted numbers are:")
print(numbers)
      
