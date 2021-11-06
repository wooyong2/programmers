# 출처: https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84-BFSDFS
# 출처에 적은 벨로그를 보고 공부한 뒤 기억나는대로 푼 문제라 내가 풀었다고 하긴 좀 그런 문제...

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    stack = [[numbers[0], 0], [-numbers[0], 0]]

    while stack:
        num, idx = stack.pop()
        idx += 1
        if idx == n:
            if num == target:
                answer += 1
        else:
            stack.append([num + numbers[idx], idx])
            stack.append([num - numbers[idx], idx])
    return answer