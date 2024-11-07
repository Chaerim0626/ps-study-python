import sys
input = sys.stdin.readline 
n = int(input())
li = list(map(int,input().split()))
li.sort()


def solution(li):
    result = float('inf')
    left, right = 0, n-1 
    answer = [0,0,0]
    

    for i in range(1,n-1):
        left, right = 0, n-1

        while left < i and right > i:
            tmp = li[left] + li[i] + li[right]

            if abs(tmp) < abs(result):
                result = tmp
                answer = [li[left], li[i], li[right]]

            if tmp > 0:
                right -= 1
            elif tmp < 0:
                left += 1
            else:
                return answer
    
    return answer

answer = solution(li)
print(answer[0], answer[1], answer[2])