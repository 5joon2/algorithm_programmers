def solution(N, number):
    dp = []
    answer = -1

    for i in range(0, 8):
        tmp = []
        print('dp: ', dp)
        for j in range(0, i):
            for k in dp[j]:
                print('i, j: ', i, j)
                for l in dp[i-j-1]:
                    mul = k * l
                    if l > 0:
                        div = k // l if k // l > 0 else None
                    add = k + l
                    sub = k - l if k - l >= 0 else None
                    if div is not None:
                        tmp.append(div)
                    if sub is not None:
                        tmp.append(sub)
                    tmp.append(add)
                    tmp.append(mul)


        tmp.append(int(str(N) * (i+1)))
        if number in tmp:
            answer = i+1
            break
        dp.append(list(set(tmp)))
    return answer
  
  
  
# 테스트 1 〉	통과 (0.78ms, 10.5MB)
# 테스트 2 〉	통과 (0.03ms, 10.4MB)
# 테스트 3 〉	통과 (0.04ms, 10.4MB)
# 테스트 4 〉	통과 (13.87ms, 12.4MB)
# 테스트 5 〉	통과 (8.11ms, 11.6MB)
# 테스트 6 〉	통과 (0.21ms, 10.4MB)
# 테스트 7 〉	통과 (0.22ms, 10.4MB)
# 테스트 8 〉	통과 (11.26ms, 11.9MB)
# 테스트 9 〉	통과 (0.02ms, 10.4MB)
