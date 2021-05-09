'''
Maximum difference between two elements such that larger element appears after the smaller number

Examples :

Input : arr = {2, 3, 10, 6, 4, 8, 1}
Output : 8
Explanation : The maximum difference is between 10 and 2.

Input : arr = {7, 9, 5, 6, 3, 2}
Output : 2
Explanation : The maximum difference is between 9 and 7.

'''

def maxDifference(arr):
    least = arr[0]
    low_index = 0
    high_index = 0
    highest = 0
    for i in range(1, len(arr)):
        if least > arr[i]:
            least = arr[i]
        
        if highest < arr[i]:
            highest = arr[i]
    
    return(highest - least)

print(maxDifference([7, 9, 5, 6, 3, 2]))