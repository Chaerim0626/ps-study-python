import sys
input = sys.stdin.readline 

n,m, l = map(int,input().split())
li = list(map(int, input().split())) if n > 0 else []
li += [0,l]
li.sort()

start,end = 1, max(li[i+1] - li[i] for i in range(len(li) - 1))

while start <= end:
    mid = (start+end) //2

    cnt = 0
    before = 0
    
    for i in range(len(li)):
        while li[i] - before > mid:
            cnt += 1
            before += mid 
        before = li[i]
    
    if cnt <= m: # 더 세워야함 그럼 길이를 짧게
        res = mid 
        end = mid - 1
    else: # 덜세워야 함 그럼 길이를 길게 
        start = mid + 1

print(res) 
