import sys
input = sys.stdin.readline

n, k = map(int, input().split())

start, end = 0, n // 2
result = "NO"

while start <= end:
    mid = (start + end) // 2

    # 현재 mid에서의 paper 계산
    paper = (mid + 1) * (n - mid + 1)
    
    if paper == k:  # 조건 만족 시
        result = "YES"
        break  # 정답을 찾으면 탐색 종료

    if paper < k:  # 너무 작으면 범위를 오른쪽으로 확장
        start = mid + 1
    else:  # 너무 크면 범위를 왼쪽으로 축소
        end = mid - 1

print(result)
