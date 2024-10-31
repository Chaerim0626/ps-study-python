import sys
input = sys.stdin.readline 

s = int(input())
result = 0

i = 1
while s >= i:
    s -= i
    result += 1
    i += 1

print(result) if i != 1 else print(1)