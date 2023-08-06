import sys

input_data = sys.stdin.readline

N = int(input_data())
result = 0
for i in range(N):
    word = input_data()
    d = {}
    okay = 1
    for j in range(len(word)):
        if word[j] in d and word[j-1] != word[j]:
            okay = 0
            break
        d[word[j]] = 1
    if okay:
        result += 1
print(result)
