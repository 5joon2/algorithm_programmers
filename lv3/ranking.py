def solution(n, results):
    wins = {}
    loses = {}

    for i in range(1, n + 1):  # init
        wins[i] = []
        loses[i] = []

    for result in results:
        winner, loser = result[0], result[1]
        wins[winner].append(loser)
        loses[loser].append(winner)

    for i in range(1, n + 1):
        losers = [loser for loser in wins[i]]  # save direct loser
        visited = [False for i in range(n+1)]
        while losers:
            loser = losers.pop()
            visited[loser] = True
            wins[i].append(loser)
            loses[loser].append(i)
            if len(wins[loser]) > 0:
                for far_loser in wins[loser]:
                    if visited[far_loser] is False:
                        losers.append(far_loser)

        wins[i] = list(set(wins[i]))
        loses[i] = list(set(loses[i]))

    answer = 0
    for i in range(1, n + 1):
        wins[i] = list(set(wins[i]))    # TODO: why needs this line???
        loses[i] = list(set(loses[i]))

        if len(wins[i]) + len(loses[i]) == n-1:
            answer += 1

    return answer
