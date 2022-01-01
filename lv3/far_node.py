from collections import deque

def solution(n, edge):
    visited = [False] * (n+1)
    answer = 0
    dq = deque()
    graph = {}
    for e in edge:
        if e[0] not in graph.keys():
            graph[e[0]] = []
        if e[1] not in graph.keys():
            graph[e[1]] = []
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    dq.append(1)
    visited[1] = True
    while dq:
        this_distance_nodes = len(dq)
        answer = this_distance_nodes
        for i in range(this_distance_nodes):
            current = dq.popleft()
            for adj_node in graph[current]:
                if visited[adj_node] is not True:
                    dq.append(adj_node)
                    visited[adj_node] = True
    return answer
  
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.4MB)
# 테스트 3 〉	통과 (0.04ms, 10.3MB)
# 테스트 4 〉	통과 (0.26ms, 10.3MB)
# 테스트 5 〉	통과 (1.17ms, 10.7MB)
# 테스트 6 〉	통과 (3.37ms, 10.9MB)
# 테스트 7 〉	통과 (28.34ms, 17.6MB)
# 테스트 8 〉	통과 (44.50ms, 20.8MB)
# 테스트 9 〉	통과 (39.13ms, 20.7MB)
