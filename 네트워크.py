# 풀긴 풀었는데 코드를 조금 깔끔하게 정리할 필요 있음.
from collections import deque


def solution(n, computers):
    answer = 0
    visited = []
    need_visited = deque()
    for i in range(n):
        if i not in visited:
            answer += 1
            need_visited.append(i)

        while need_visited:
            node = need_visited.popleft()
            if node not in visited:
                visited.append(node)
                for j in range(n):
                    if node == j:
                        continue
                    if computers[node][j] == 1:
                        need_visited.append(j)

    return answer