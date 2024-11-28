import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)] 
result = [0] *(n-1)
visited = [0] *(n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start):
    visited[start] = 1
    
    for node in tree[start]:
        if not visited[node]:
            result[node-2] = start 
            dfs(node)

dfs(1)
for i in result:
    print(i)