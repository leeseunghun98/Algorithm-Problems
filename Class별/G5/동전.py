import sys
input = sys.stdin.readline
testcase = int(input())
for _ in range(testcase):
    n = int(input())
    coins = tuple(map(int, input().split()))
    target = int(input())
    
    dp = [[0 for _ in range(target+1)] for _ in range(len(coins)+1)]
    for coin in range(1, len(coins)+1):
        if coins[coin-1] <= target:
            for i in range(coins[coin-1]):
                dp[coin][i] = dp[coin-1][i]
            dp[coin][coins[coin-1]] = 1 + dp[coin-1][coins[coin-1]]
            for i in range(coins[coin-1]+1, target+1):
                dp[coin][i] = dp[coin-1][i] + dp[coin][i-coins[coin-1]]
        else:
            dp[coin] = dp[coin-1]
    print(dp[-1][-1])