import sys
input = sys.stdin.readline

# 입력받기
n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]
times.sort()

# 이진 탐색 변수 초기화
start, end = 1, m * times[0]
answer = 0

# 이진 탐색 시작
while start <= end:
    mid = (start + end) // 2

    # 주어진 시간 안에 처리할 수 있는 사람의 수 계산
    total_people = sum(mid // time for time in times)

    if total_people >= m:  # 목표 인원을 충족하는 경우
        answer = mid
        end = mid - 1
    else:  # 목표 인원에 미달하는 경우
        start = mid + 1

# 최종 값 보정
total_people_at_start = sum(start // time for time in times)

if total_people_at_start == m:
    print(min(answer, start))
else:
    print(answer)
