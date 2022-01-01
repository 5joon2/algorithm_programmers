def bfs(begin, words, target, visited):
    stack = [(begin, 0)]  # (word, depth)
     
    while stack:
        cur_word, cur_depth = stack.pop()
        print('satck go: ', cur_word, cur_depth)
        if target == cur_word:
            return cur_depth
        
        for idx, target_word in enumerate(words):
            if visited[idx]:
                continue

            
            compare = 0
            for a, b in zip(cur_word, target_word):
                if a != b:
                    compare += 1
            if compare == 1:
                stack.append((target_word, cur_depth+1))
                visited[idx] = True

            
    
def solution(begin, target, words):
    visited = [False for word in words]
    print('visited: ', visited)
    
    if target not in words:
        answer = 0
    else:   
        answer = bfs(begin, words, target, visited)
        
    print('answer: ', answer)
    
    return answer
    
    
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.06ms, 10.3MB)
# 테스트 3 〉	통과 (0.31ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
