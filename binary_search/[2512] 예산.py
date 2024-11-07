import sys
input = sys.stdin.readline 

n = int(input())
li = list(map(int,input().split()))
m = int(input())

li.sort()

start, end = 1, li[-1]
result = 0

if sum(li) <= m:
    print(max(li))
else:

    while start <= end:
        mid = (start+end) // 2
        
        total = 0

        for i in li:
            if i <= mid:
                total += i 
            else: # i > mid
                total += mid 

        if total > m:
            end = mid - 1
        else: # total <= m 
            result = mid
            start = mid + 1
    print(result)