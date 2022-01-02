def solution(triangle):
    
    for i, numbers in enumerate(triangle):
        if i == 0:
            continue
        elif i > 0:
            for j, number in enumerate(numbers):
                if j == 0:  # left end
                    numbers[j] += triangle[i-1][0]
                elif j == len(numbers)-1:  # right end
                    numbers[j] += triangle[i-1][-1]
                else:  # in the middle
                    numbers[j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])       
  

# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.05ms, 10.2MB)
# 테스트 4 〉	통과 (0.32ms, 10.2MB)
# 테스트 5 〉	통과 (1.15ms, 10.3MB)
# 테스트 6 〉	통과 (0.59ms, 10.2MB)
# 테스트 7 〉	통과 (2.17ms, 10.3MB)
# 테스트 8 〉	통과 (0.26ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.17ms, 10.3MB)
# 효율성  테스트
# 테스트 1 〉	통과 (42.25ms, 14.2MB)
# 테스트 2 〉	통과 (32.65ms, 13.1MB)
# 테스트 3 〉	통과 (47.93ms, 14.6MB)
# 테스트 4 〉	통과 (44.63ms, 14.2MB)
# 테스트 5 〉	통과 (39.36ms, 13.9MB)
# 테스트 6 〉	통과 (49.06ms, 14.6MB)
# 테스트 7 〉	통과 (46.04ms, 14.4MB)
# 테스트 8 〉	통과 (45.60ms, 13.7MB)
# 테스트 9 〉	통과 (35.64ms, 14MB)
# 테스트 10 〉	통과 (46.49ms, 14.4MB)
