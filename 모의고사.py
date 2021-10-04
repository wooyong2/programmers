def solution(answers):
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score1, score2, score3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == num1[i % 5]:
            score1 += 1
        if answers[i] == num2[i % 8]:
            score2 += 1
        if answers[i] == num3[i % 10]:
            score3 += 1

    winners = []
    if score1 >= score2 and score1 >= score3:
        winners.append(1)
    if score2 >= score1 and score2 >= score3:
        winners.append(2)
    if score3 >= score1 and score3 >= score2:
        winners.append(3)

    return winners