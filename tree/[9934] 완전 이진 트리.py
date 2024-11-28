import sys
input = sys.stdin.readline 

k = int(input())
trees = list(map(int,input().split()))
level = [[] for _ in range(2**k-1)]

def solution(tree,i):

    if not tree:
        return
    level[i].append(tree[len(tree)//2])
    root_idx = len(tree)//2

    left = tree[:root_idx]
    right = tree[root_idx+1:]

    solution(left,i+1)
    solution(right,i+1)

solution(trees,0)

for i in level:
    if i:
        print(*i)