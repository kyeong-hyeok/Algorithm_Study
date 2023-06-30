def solution(answers):
    ans = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    inx = 0
    total = [0, 0, 0]
    for i in answers:
        if ans[0][inx % len(ans[0])] == i:
            total[0] += 1
        if ans[1][inx % len(ans[1])] == i:
            total[1] += 1
        if ans[2][inx % len(ans[2])] == i:
            total[2] += 1
        inx += 1
    max_ans = max(total)
    result = []
    for i in range(len(total)):
        if total[i] == max_ans:
            result.append(i+1)
    return result