import sys
input = sys.stdin.readline 

dic = dict()
n , m = map(int,input().split())
for _ in range(n):
    s = input().split()

    url = s[0]
    pwd = s[1]
    dic[url] = pwd
for _ in range(m):
    s = input().rstrip()
    print(dic[s])