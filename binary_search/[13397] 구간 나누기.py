import sys
input = sys.stdin.readline 

n,m = map(int,input().split())
li = list(map(int,input().split()))

start,end = 0, max(li)

result = float('inf')

while start <= end:
    mid = (start+end)//2

    cnt = 1

    max_val = li[0]
    min_val = li[0]

    for i in range(n):
        max_val = max(max_val,li[i])
        min_val = min(min_val, li[i])

        if max_val - min_val > mid:
            cnt += 1
            max_val = li[i]
            min_val = li[i]

    if cnt <= m: # 개수가 작거나 같으니까 더 나눠야함
        end = mid - 1
        result = min(result,mid)

    else:
        start = mid + 1

print(result)