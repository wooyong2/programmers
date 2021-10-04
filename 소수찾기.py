from itertools import permutations


def solution(numbers):
    answer = 0

    # 에라토스테네스의 체 이용해서 소수 판별 리스트 미리 구해놓기
    lim = 10000000
    prime = [True] * lim
    m = int(lim ** 0.5)
    for i in range(2, m + 1):
        if prime[i] == True:
            for j in range(i + i, lim, i):
                prime[j] = False
    prime[0], prime[1] = False, False

    # 주어진 숫자로 만들 수 있는 숫자(문자열) 리스트 전부 만든 다음 정수형 변환 및 중복 제거
    str_nums = []
    int_nums = []
    for i in range(len(numbers)):
        str_nums.append(list(map(''.join, permutations(numbers, i + 1))))

    for i in range(len(str_nums)):
        for j in range(len(str_nums[i])):
            int_nums.append(int(str_nums[i][j]))

    int_nums = set(int_nums)
    int_nums = list(int_nums)

    for num in int_nums:
        if prime[num]:
            answer += 1

    return answer