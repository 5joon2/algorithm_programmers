from itertools import permutations

def split(word):
    return [char for char in word]


def compare(id1, id2):  # id2 has *
    id_1 = split(id1)
    id_2 = split(id2)
    if len(id_1) != len(id_2):
        return False
    for idx, char in enumerate(id_1):
        if id_2[idx] == '*':
            continue
        if char != id_2[idx]:
            return False
    return True


def solution(user_id, banned_id):
    checked = []
    user_permutations = list(permutations(user_id, len(banned_id)))

    for candi in user_permutations:
        matching = True
        for i in range(len(candi)):
            if compare(candi[i], banned_id[i]) is False:
                matching = False
                break
        if matching:
            candi_set = set(candi)
            if candi_set not in checked:
                checked.append(candi_set)

    return len(checked)


if __name__ == '__main__':
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["*rodo", "*rodo", "******"]
    solution(user_id, banned_id)

    
# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (1.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.38ms, 10.3MB)
# 테스트 4 〉	통과 (0.48ms, 10.3MB)
# 테스트 5 〉	통과 (530.19ms, 14.9MB)
# 테스트 6 〉	통과 (61.51ms, 12.1MB)
# 테스트 7 〉	통과 (3.22ms, 10.3MB)
# 테스트 8 〉	통과 (2.88ms, 10.3MB)
# 테스트 9 〉	통과 (2.48ms, 10.3MB)
# 테스트 10 〉	통과 (51.28ms, 14.9MB)
# 테스트 11 〉	통과 (4.45ms, 10.3MB)
