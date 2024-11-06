import sys
input = sys.stdin.readline 
from collections import deque

t = int(input())

def isvalid(y,x):
    return 0 <= y < n and 0 <= x < m

def bfs(sy,sx,graph,visited):

    dq = deque()
    dq.append((sy,sx))
    dir = [[1,0],[-1,0], [0,1], [0,-1]]

    while dq:
        cy,cx = dq.popleft()
        for dy,dx in dir:
            ny,nx = cy+dy, cx+dx
            if isvalid(ny,nx) and graph[ny][nx]:
                if not visited[ny][nx]:
                    dq.append((ny,nx))
                    visited[ny][nx] = 1
    

for _ in range(t):
    m,n,k = map(int,input().split())
    graph = [[0] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1

    visited = [[0]*(m+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j]:
                bfs(i,j,graph,visited)
                cnt += 1
    print(cnt)
