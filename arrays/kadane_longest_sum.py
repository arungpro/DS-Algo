def kadane(arr):
    currSum = 0
    oldSum = 0
    for ele in arr:
        currSum = currSum + ele
        if currSum < 0:
            currSum = 0
        elif currSum > oldSum:
            oldSum = currSum

    return oldSum

arr = [1, 2, -1, 5, -3, 4, -10]
print(kadane(arr))