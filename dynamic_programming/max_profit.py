def maxProfit(prices, k):
    if(len(prices) < 2):
        print("You need atleast 2 transaction")
        return

    # dp = [float("-INF"), 0, float("-INF"), 0]
    # Assumption to start, -INF and sell with 0
    dp = []
    for i in range(0, k*2):
        if i % 2 == 0:
            dp.append(float("-INF"))
        else:
            dp.append(0)

    for day_price in prices:
        for j in range(0, len(dp)):
            if j == 0:
                dp[j] = max(dp[j], -1*day_price)
            elif j % 2 == 0:
                dp[j] = max(dp[j], dp[j-1] - day_price)
            else:
                dp[j] = max(dp[j], dp[j-1] + day_price)
    
    print(dp)
    print("Best possible profit is ", dp[-1])

prices = [10, 22, 5, 75, 65, 80]
transactions = 2

maxProfit(prices, transactions)