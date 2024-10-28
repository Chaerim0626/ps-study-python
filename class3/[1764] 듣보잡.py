import sys
input = sys.stdin.readline 
from collections import defaultdict

n,m = map(int,input().split())
dic = defaultdict(int)

for _ in range(n+m):
    dic[input().rstrip()] += 1

result = sorted([key for key, value in dic.items() if value == 2])

print(len(result))
print('\n'.join(result))