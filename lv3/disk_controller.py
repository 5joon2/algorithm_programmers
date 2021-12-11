import heapq as pq

def solution(jobs):
    min_heap = []
    cur_time = 0
    last_job_start_time = -1
    completed_job = 0
    answer = 0

    while completed_job < len(jobs):
        for job in jobs:
            if last_job_start_time < job[0] <= cur_time:
                pq.heappush(min_heap, [job[1], job[0]])

        if len(min_heap) > 0:
            next_job = pq.heappop(min_heap)
            last_job_start_time = cur_time
            answer += next_job[0] + cur_time - next_job[1]
            cur_time += next_job[0]
            completed_job += 1

        else:
            cur_time += 1

    return int(answer / len(jobs))
