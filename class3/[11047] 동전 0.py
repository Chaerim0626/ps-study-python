import sys
input = sys.stdin.readline 

n,k = map(int,input().split())
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)
coins.sort(reverse=True)

cnt = 0
for coin in coins:
    share = k // coin
    remainder = k % coin

    cnt += share 
    k = remainder

print(cnt)