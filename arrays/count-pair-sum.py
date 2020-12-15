"""
Given an array of integers, and a number sum, find the number of unique pairs of integers in the array whose sum is equal to sum.

Examples:  

Input  :  arr[] = {1, 5, 7, -1}, 
          sum = 6
Output :  2
Pairs with sum 6 are (1, 5) and (7, -1)

Time complexity should be O(n)
"""

def sortArray(arr):
    arr.sort()
    return arr

def countPairSum(arr, sum):
    sortedArr = sortArray(arr)
    # print(sortedArr) #[-1, 1, 5, 7]
    i = 0
    j = len(arr) - 1
    count = 0
    while(i < j):
        tempSum = sortedArr[i] + sortedArr[j]
        if(tempSum == sum):
            count = count + 1
            i = i + 1
            j = j - 1
        elif(tempSum > sum):
            j = j - 1
        else:
            i = i + 1

    print(count) 
        
arr = [1, 5, 7, -1]
sum = 6
countPairSum(arr, sum)