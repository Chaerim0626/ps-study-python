import sys
input = sys.stdin.readline 

n,m = map(int,input().split())
li = [int(input()) for _ in range(n)]
li.sort()

start, end = 1, li[-1] - li[0]
result = 0

while start <= end:
    mid = (start+end) // 2

    cnt = 1
    before = li[0]

    for i in range(1,n):
        if li[i] - before < mid: # 설치 못함
            continue
        else: # 설치 할 수 있음, 설치했으니 갱신
            before = li[i]
            cnt += 1


    if cnt < m: # 더많이 설치해야함 -> 거리를 작게
        end = mid - 1
    else: # 더 적게 설치해도됨 -> 거리를 크게 
        result = mid 
        start = mid + 1 


print(result)
            
    

