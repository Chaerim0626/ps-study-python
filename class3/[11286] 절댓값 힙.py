import sys, heapq
input = sys.stdin.readline 

hq = []

n = int(input())
for _ in range(n):
    x = int(input())

    if x:
        if x > 0:
            heapq.heappush(hq,(x,x))
        else:
            heapq.heappush(hq,(-x,x))
    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)

    