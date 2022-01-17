def solution(s):
    answer = 1

    for i in range(len(s)):  # 0~len-1
        for j in range(1, len(s)+1):  # 1~len

            if s[i:j] == s[i:j][::-1]:
                answer = max(answer, j-i)

    return answer
