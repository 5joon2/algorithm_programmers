import math

def solution(enroll, referral, seller, amount):
    parent = {'minho': '-'}
    income = {'minho': 0}

    for i in range(len(enroll)):
        if referral[i] != '-':
            parent[enroll[i]] = referral[i]
        else:
            parent[enroll[i]] = 'minho'

        income[enroll[i]] = 0

    for idx in range(len(seller)):
        target = seller[idx]
        money = amount[idx] * 100

        while target != '-':
            toss = math.floor(money * 0.1)
            if toss < 1 or parent[target] == '-':
                income[target] += money
                break

            own = money - toss
            income[target] += own
            money = toss
            target = parent[target]

    answer = [val for val in income.values()]

    return answer[1:]


# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.12ms, 10.3MB)
# 테스트 3 〉	통과 (0.05ms, 10.3MB)
# 테스트 4 〉	통과 (0.16ms, 10.4MB)
# 테스트 5 〉	통과 (1.25ms, 10.3MB)
# 테스트 6 〉	통과 (2.63ms, 12.6MB)
# 테스트 7 〉	통과 (2.70ms, 12.6MB)
# 테스트 8 〉	통과 (4.17ms, 12.7MB)
# 테스트 9 〉	통과 (17.52ms, 14.2MB)
# 테스트 10 〉	통과 (151.81ms, 21.2MB)
# 테스트 11 〉	통과 (132.61ms, 20.5MB)
# 테스트 12 〉	통과 (139.38ms, 20.6MB)
# 테스트 13 〉	통과 (138.81ms, 20.6MB)
