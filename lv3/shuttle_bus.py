import operator


def time2int(time):
    h = int(time[:2]) * 60
    m = int(time[3:5])
    return h+m


def int2time(time):
    h = int(time/60)
    m = int(time-h*60)
    return f'{h:0>2}:{m:0>2}'


def solution(n, t, m, timetable):
    answer = ''
    start_time = time2int('09:00')
    shuttle_bus = {start_time + t*i: m for i in range(n)}
    crew_arrive_times = {start_time + t*i: [] for i in range(n)}

    crews = []
    for time in timetable:
        minutes = time2int(time)
        crews.append(minutes)
    crews.sort()

    for crew in crews:
        for time, capa in shuttle_bus.items():
            if time >= crew and capa > 0:
                shuttle_bus[time] -= 1
                crew_arrive_times[time].append(crew)
                break

    reversed_shuttle_bus = dict(sorted(shuttle_bus.items(), key=operator.itemgetter(0), reverse=True))

    for time, capa in reversed_shuttle_bus.items():
        if capa >= 1:  
            answer = time
            break
        elif capa < 1:
            answer = crew_arrive_times[time][-1] - 1
            print(crew_arrive_times[time][-1], time)
            break

    answer = int2time(answer)

    return answer


# 테스트 1 〉	통과 (0.03ms, 10.5MB)
# 테스트 2 〉	통과 (0.04ms, 10.4MB)
# 테스트 3 〉	통과 (0.04ms, 10.5MB)
# 테스트 4 〉	통과 (0.05ms, 10.5MB)
# 테스트 5 〉	통과 (0.06ms, 10.5MB)
# 테스트 6 〉	통과 (0.04ms, 10.5MB)
# 테스트 7 〉	통과 (0.55ms, 10.5MB)
# 테스트 8 〉	통과 (0.03ms, 10.5MB)
# 테스트 9 〉	통과 (0.04ms, 10.5MB)
# 테스트 10 〉	통과 (0.05ms, 10.6MB)
# 테스트 11 〉	통과 (0.05ms, 10.5MB)
# 테스트 12 〉	통과 (0.45ms, 10.5MB)
# 테스트 13 〉	통과 (0.75ms, 10.6MB)
# 테스트 14 〉	통과 (0.13ms, 10.5MB)
# 테스트 15 〉	통과 (0.13ms, 10.5MB)
# 테스트 16 〉	통과 (0.20ms, 10.5MB)
# 테스트 17 〉	통과 (0.67ms, 10.5MB)
# 테스트 18 〉	통과 (0.43ms, 10.5MB)
# 테스트 19 〉	통과 (0.49ms, 10.5MB)
# 테스트 20 〉	통과 (0.49ms, 10.5MB)
# 테스트 21 〉	통과 (1.68ms, 10.5MB)
# 테스트 22 〉	통과 (0.55ms, 10.4MB)
# 테스트 23 〉	통과 (0.47ms, 10.5MB)
# 테스트 24 〉	통과 (1.51ms, 10.5MB)
