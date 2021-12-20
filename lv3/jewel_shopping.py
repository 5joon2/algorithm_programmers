from collections import defaultdict

def solution(gems):
    gems_dict = defaultdict(int)
    gems_num = len(set(gems))
    gems_candidate_num = len(gems)

    left = 0
    right = 0
    last_min = 99999999999
    answer = []


    while right < gems_candidate_num:
        gems_dict[gems[right]] += 1
        right += 1

        if len(gems_dict) == gems_num:
            while left < right:
                if gems_dict[gems[left]] <= 1:
                    break
                gems_dict[gems[left]] -= 1
                left += 1

            if last_min > right - left:
                last_min = right - left
                answer = [left+1, right]

    return answer

# 	["AA", "AB", "AC", "AA", "AC"]

# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.09ms, 10.4MB)
# 테스트 3 〉	통과 (0.16ms, 10.2MB)
# 테스트 4 〉	통과 (0.20ms, 10.3MB)
# 테스트 5 〉	통과 (0.25ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.28ms, 10.3MB)
# 테스트 9 〉	통과 (0.64ms, 10.3MB)
# 테스트 10 〉	통과 (0.32ms, 10.3MB)
# 테스트 11 〉	통과 (0.47ms, 10.4MB)
# 테스트 12 〉	통과 (0.67ms, 10.3MB)
# 테스트 13 〉	통과 (1.03ms, 10.4MB)
# 테스트 14 〉	통과 (0.84ms, 10.4MB)
# 테스트 15 〉	통과 (2.05ms, 10.5MB)
# 효율성  테스트
# 테스트 1 〉	통과 (2.94ms, 10.6MB)
# 테스트 2 〉	통과 (3.31ms, 10.6MB)
# 테스트 3 〉	통과 (7.37ms, 11.2MB)
# 테스트 4 〉	통과 (6.91ms, 12MB)
# 테스트 5 〉	통과 (13.54ms, 12MB)
# 테스트 6 〉	통과 (15.81ms, 12.3MB)
# 테스트 7 〉	통과 (19.37ms, 12.7MB)
# 테스트 8 〉	통과 (19.43ms, 12.8MB)
# 테스트 9 〉	통과 (21.53ms, 13.5MB)
# 테스트 10 〉	통과 (29.01ms, 14.1MB)
# 테스트 11 〉	통과 (32.42ms, 14.8MB)
# 테스트 12 〉	통과 (22.82ms, 15.5MB)
# 테스트 13 〉	통과 (31.38ms, 16.4MB)
# 테스트 14 〉	통과 (48.72ms, 17.1MB)
# 테스트 15 〉	통과 (45.13ms, 17.8MB)
