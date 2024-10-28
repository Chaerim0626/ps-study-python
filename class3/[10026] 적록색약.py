import sys, copy
input = sys.stdin.readline 
from collections import deque

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
graph2 = [['G' if color=='R' else color for color in row]for row in graph]


def isvalid(x,y):
    return 0 <= x < n and 0 <= y < n

def bfs(sx,sy,graph):
    dq = deque()
    dq.append((sx,sy))
    res = 0
    visited[sx][sy] = 1

    dir = [[0,1],[0,-1], [1,0], [-1,0]]
    while dq:
        cx,cy = dq.popleft()

        for dx,dy in dir:
            nx,ny = dx+cx, dy+cy

            if isvalid(nx,ny) and not visited[nx][ny]:
                if graph[cx][cy] == graph[nx][ny]:
                    visited[nx][ny] = 1
                    dq.append((nx,ny))
    return 1

cnt = 0

def solution(graph):
        
    visited = [[0]* n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += bfs(i,j,graph)

    return cnt

cnt = solution(graph)
cnt2 = solution(graph2)
print(cnt, cnt2)

