import sys
input = sys.stdin.readline 


n = int(input())
dp = [0] * (n+1)

if n == 1:
    print(1)
elif n == 2:
    print(3)
elif n ==3 :
    print(5)
else:
    dp[1] = 1
    dp[2] = 2
    dp[3] = 5
    for i in range(4,n+1):
        if i % 2 == 0:
            dp[i] = 2*dp[i-1] + 1
        else:
            dp[i] = 2*dp[i-1] - 1
    
    print(dp[n] % 10007)