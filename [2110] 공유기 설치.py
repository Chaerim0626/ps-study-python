import sys
input = sys.stdin.readline

n,c = map(int,input().split())
homes = []

for _ in range(n):
    homes.append(int(input()))
homes.sort()  # O(nlgn)

start = 0
end = homes[-1] - homes[0]
result = 0

while start <= end:
    mid = (start+end)//2
    cur = homes[0]
    cnt = 1

    for i in range(1,n):
        if homes[i] - cur >= mid:
            cur = homes[i]
            cnt += 1
    
    if cnt < c:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)