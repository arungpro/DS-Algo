"""
Largest Sum Contiguous Subarray
"""

def maxSumContSubArray(arr):
    oldSum = 0
    currentSum = 0
    for ele in arr:
        currentSum = currentSum + ele
        if(currentSum < 0):
            currentSum = 0
        elif(oldSum < currentSum):
            oldSum = currentSum
    return oldSum

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSumContSubArray(arr))