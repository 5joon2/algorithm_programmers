def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    
    for i in range(n):
        if visited[i] == False:
            bfs(n, computers, i, visited)
            answer += 1
    
    return answer


def bfs(n, computers, comp_idx, visited):
    queue = []    
    queue.append(comp_idx)
    
    while len(queue) > 0:
        target = queue.pop(0)
        visited[target] = True
        for i in range(n):
            if computers[target][i] == 1 and target != i and visited[i] != True:
                queue.append(i)

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.06ms, 10.2MB)
# 테스트 4 〉	통과 (0.07ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.78ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.32ms, 10.2MB)
# 테스트 9 〉	통과 (0.14ms, 10.3MB)
# 테스트 10 〉	통과 (0.21ms, 10.2MB)
# 테스트 11 〉	통과 (2.78ms, 10.3MB)
# 테스트 12 〉	통과 (1.41ms, 10.3MB)
# 테스트 13 〉	통과 (0.57ms, 10.2MB)






def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]

    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(computers, visited, i, n)

    return answer

def dfs(computers, visited, comp_idx, n):

    if visited[comp_idx]:
        return

    visited[comp_idx] = True
    for idx, neighbor in enumerate(computers[comp_idx]):
        if idx != comp_idx and neighbor == 1 and not visited[idx]:  # not me && connected
            dfs(computers, visited, idx, n)
            
            
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (0.00ms, 10.3MB)
# 테스트 6 〉	통과 (0.14ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.4MB)
# 테스트 8 〉	통과 (0.10ms, 10.3MB)
# 테스트 9 〉	통과 (0.06ms, 10.2MB)
# 테스트 10 〉	통과 (0.06ms, 10.2MB)
# 테스트 11 〉	통과 (0.50ms, 10.4MB)
# 테스트 12 〉	통과 (0.37ms, 10.3MB)
# 테스트 13 〉	통과 (0.21ms, 10.3MB)
            
            
