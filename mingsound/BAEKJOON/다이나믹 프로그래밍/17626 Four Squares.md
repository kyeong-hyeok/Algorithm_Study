### 풀이
```python
# 2:45 - 2:57

# 1. dp에 해당 숫자가 최소 몇 개의 제곱수의 합으로 표현할 수 있는지 기록
# 2. 점화식 : dp[해당 숫자] = dp[해당 숫자 - 해당 숫자 이하의 제곱수]값의 최솟값 + 1
import math

n = int(input())
dp = [0] * (n+1)
dp[1] = 1

prev_sqrt = 1
for i in range(2, n+1):
    if math.sqrt(i) == int(math.sqrt(i)): # 제곱수라면
        dp[i] = 1 # dp에 1 기록
        prev_sqrt = int(math.sqrt(i)) # prev_sqrt에 해당 i의 루트값 기록
        continue

    # i보다 작은 제곱수들에 대해서 
    _min = 1e9
    for j in range(prev_sqrt, 0, -1):
        _min = min(_min, dp[i - (j**2)])# dp[i - (j**2)]의 최솟값 구하기

    dp[i] = _min + 1 # 해당 최솟값 + 1을 dp에 기록

print(dp[n]) # 정답 출력
```

### 아이디어
```text
1. dp에 해당 숫자가 최소 몇 개의 제곱수의 합으로 표현할 수 있는지 기록

2. 점화식 : dp[해당 숫자] = dp[해당 숫자 - 해당 숫자 이하의 제곱수]값의 최솟값 + 1
```

### 실수 & 깨달은 바
```text
처음에는 해당 값과 가장 가까운 큰 제곱수만 고려하면 되겠다고 생각했는데 아니었다.

dp를 사용하면 되게 효율화가 많이 된다고 생각했는데 문제를 풀 수록 생각보다 dp 테이블은 완전 탐색을 하는 경우도 있는 것 같다는 것을 깨달았다.
```