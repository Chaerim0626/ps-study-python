import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start):

    visited[start] = 1

    for next in graph[start]:
        if not visited[next]:
            dfs(next)
    
cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)