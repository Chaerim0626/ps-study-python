import sys
input = sys.stdin.readline 

n = int(input())
homes = list(map(int,input().split()))
homes.sort()

result = 0
result2 = 0

for home in homes:
    result += abs(home-homes[len(homes)//2])


for home in homes:
    result2 += abs(home- homes[len(homes)//2-1])


print(homes[len(homes)//2-1]) if result <= result2 else print(homes[len(homes)//2])