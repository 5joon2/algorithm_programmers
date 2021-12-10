def can_process_person(given_time, times):
    res = 0
    for each_line_time in times:
        res += int(given_time / each_line_time)
    return res   

def solution(n, times):
    most_slow_line = max(times)
    max_time = most_slow_line * n
    min_time = 1

    while min_time <= max_time:
        middle_time = int((max_time + min_time) / 2)
        capacity = can_process_person(middle_time, times)
        
        if capacity >= n:
            max_time = middle_time-1
        elif capacity < n:
            min_time = middle_time+1

    return min_time