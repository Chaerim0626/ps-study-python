import sys
input = sys.stdin.readline 

n = int(input())
li = list(map(int,input().split()))
li.sort()
result = float('inf')
left, right = 0, n-1

answer = (0,0)

while left < right:
    tmp = li[left] + li[right]

    if abs(tmp) < abs(result):
        result = tmp
        answer = (li[left], li[right])
    
    if tmp > 0:
        right -= 1
    elif tmp < 0:
        left += 1
    else:
        answer = (li[left], li[right])
        break

print(answer[0], answer[1])