import sys, heapq
input = sys.stdin.readline 

hq = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush((hq,-x))
    elif not x and hq:
        print(heapq.heappop(hq))
    else:
        print(0)


