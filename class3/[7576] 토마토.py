import sys
input = sys.stdin.readline 
from collections import deque

m,n = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

# 익은 토마토가 있는 모든 좌표
tomato = [(i, j) for i in range(len(graph)) for j in range(len(graph[i])) if graph[i][j]==1]


def isvalid(x,y):
    return 0 <= y < m and 0 <= x < n

def bfs():
    dq = deque([(x,y,0) for x,y in tomato]) # 동시에 모든 좌표를 넣기
    m_day = 0
    dir = [[0,1], [0,-1], [1,0], [-1,0]]

    while dq:
        cx,cy,day = dq.popleft()
        m_day = max(m_day,day)
        for dx,dy in dir:
            nx,ny = cx+dx, cy+dy

            if isvalid(nx,ny) and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                dq.append((nx,ny,day+1))

    # bfs 끝난 후
    for row in graph:
        if 0 in row:
            return -1
    return m_day
    

print(bfs())