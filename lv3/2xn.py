import sys

sys.setrecursionlimit(60000)

def solution(n):
  # must recursive dp 
#     dp = [-1 for i in range(60001)]
#     dp[1] = 1
#     dp[2] = 2

#     for i in range(3, (n+1)):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n] % 1000000007

    dp = [-1 for i in range(60001)]
    dp[1] = 1
    dp[2] = 2
    
    def call_dp(n):
        if dp[n] != -1:
            return dp[n]
        elif n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        dp[n] = (call_dp(n-1) + call_dp(n-2)) % 1000000007
        
        return dp[n]
    
    return call_dp(n)
