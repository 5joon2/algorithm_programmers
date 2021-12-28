import heapq

def solution(operations):
    min_heap = []
    
    for op in operations:
        command, value = op.split()
        print(command, value)
        if command == 'I':
            heapq.heappush(min_heap, int(value))
        elif command == 'D':
            if len(min_heap) == 0:
                continue
                
            if value == '1':
                max_value = heapq.nlargest(1, min_heap)[0]
                min_heap.pop(min_heap.index(max_value))
            elif value == '-1':
                min_value = heapq.heappop(min_heap)
    
    if len(min_heap) == 0:
        return [0, 0]
    else:
        return [heapq.nlargest(1, min_heap)[0], min_heap[0]]
        
# 테스트 1 〉	통과 (0.03ms, 10.5MB)
# 테스트 2 〉	통과 (0.03ms, 10.4MB)
# 테스트 3 〉	통과 (0.05ms, 10.4MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.03ms, 10.4MB)
# 테스트 6 〉	통과 (0.03ms, 10.4MB)
