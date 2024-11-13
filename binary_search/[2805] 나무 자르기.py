import sys
input = sys.stdin.readline 

n,m = map(int,input().split())
trees = list(map(int,input().split()))
trees.sort()

start,end = 1, trees[-1]
length = 0
result = 0

while start <= end:
    length = 0
    mid = (start+end) //2

    for tree in trees:
        if tree > mid:
            length += tree-mid
        else:
            continue

    if length >= m:
        start = mid + 1
        result = mid
    else:
        end = mid -1

print(result)