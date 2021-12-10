def solution(lines):
    start_time_series = []
    end_time_series = []
    max_score = 1
    
    if len(lines) == 1:
        return 1
    
    for line in lines:        
        start_time, end_time = parse_time(line)
        start_time_series.append(start_time)
        end_time_series.append(end_time)
    
    for i in range(len(lines)):  # 전체 time series 순회
        cnt = 1
        for j in range(i+1, len(lines)):           
            if start_time_series[j] < end_time_series[i]+1:
                cnt += 1
        max_score = max(max_score, cnt)
        
    return max_score

def parse_time(log):
    date, end_time_log, duration_log = log.split(' ')
    times = end_time_log.split(":")
    h = float(times[0])
    m = float(times[1])
    s = float(times[2])
    
    duration = float(duration_log[:-1])
    end_time = h*3600 + m*60 + s
    
    start_time = end_time - duration + 0.001
    
    return start_time, end_time