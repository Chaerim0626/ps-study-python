import sys
input = sys.stdin.readline 

n,m = map(int,input().split())
li = []
for _ in range(n):
    li.append(int(input()))

li.sort()
