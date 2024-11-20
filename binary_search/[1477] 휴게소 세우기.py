import sys
input = sys.stdin.readline 

n,m, l = map(int,input().split())
li = list(map(int,input().split()))
li.sort()

diff = 0
for i in range(1,n):
    tmp = li[i] - li[i-1]
    diff = max(diff,tmp)

print(diff)
start,end = 1, l//m

while start <= end:
    mid = (start+end)//2

    for i in li:

    
    if mid >= diff:
        end = mid - 1
    else:
        start = mid + 1
    
    