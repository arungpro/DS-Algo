'''
Given binary array [1,1,0,0,0,1,1,1,0,1], Find longest continous 1's.
Output 3
'''
def longestOnes(arr):
    curr = 0
    maxCount = 0
    for ele in arr:
        if ele == 1:
            curr += 1
        else:
            maxCount = max(maxCount, curr)
            curr = 0
    return maxCount

result = longestOnes([1,1,0,0,0,1,1,1,1,0,1])
print(result)