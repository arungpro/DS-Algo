'''
Input:  
Price = [10, 22, 5, 75, 65, 80]
    K = 2
Output:  87
'''
def k_max_profit(arr, k):
    max_profit = []
    for j in range(k*2):
        if(j%2 == 0):
            max_profit.append(float("-INF"))
        else:
            max_profit.append(0)
    
    for day_value in arr:
        for j in range(k*2):
            if j == 0:
                max_profit[j] = max(-day_value, max_profit[j])
            else:
                if j % 2 == 0:
                    max_profit[j] = max(max_profit[j-1]-day_value, max_profit[j])
                else:
                    max_profit[j] = max(max_profit[j-1]+day_value, max_profit[j])
    print(max_profit)
    print(max_profit[k*2-1])

k_max_profit([10, 22, 5, 75, 65, 80], 2)