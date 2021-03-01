# Week 7, Bubble Sort Algorithm

The assignment for our week 7 project is to:

    - This assignment will have you work on a classical algorithm that all programmers should know, the Bubble Sort.  
    - The Bubble Sort takes a list of numbers and sorts them based on an iterative review of an indexes value and it's following index value.
    - While code for this is readily available on the internet, work this out on your own before referencing other sources.  
    - This project is not about getting the code right necessarily, but understanding the problem and working through the best solution.
  
# Source Code  
  
The code I used in my program 

```python
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
      

```
# Output

```Output
enter 5 numbers at random
2
6
3
2
3
The sorted numbers are:
['2', '2', '3', '3', '6']
```
