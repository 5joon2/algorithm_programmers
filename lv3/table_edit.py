class Node:
    def __init__(self, item=None, state=True):
        self.data = item
        self.left = None
        self.right = None

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.head.left = self.head
        self.tail.right = self.tail
        self.tail.left = self.head
        self.pointer = self.head  # point head at first
        self.stack = []

    def insert(self, node):
        self.pointer.right = node
        node.left = self.pointer
        node.right = self.tail
        self.pointer = node

    def move(self, command, n):
        if command == 'U':
            while n:
                if self.pointer.left != self.head:
                    n -= 1
                    self.pointer = self.pointer.left
                elif self.pointer.left == self.head:
                    break


        elif command == 'D':
            while n:
                if self.pointer.right != self.tail:
                    n -= 1
                    self.pointer = self.pointer.right
                elif self.pointer.right == self.tail:
                    break

    def remove(self):
        self.pointer.state = False
        self.pointer.left.right = self.pointer.right
        self.pointer.right.left = self.pointer.left
        self.stack.append(self.pointer)

        if self.pointer.right == self.tail:
            self.pointer = self.pointer.left
        else:
            self.pointer = self.pointer.right

    def recover(self):
        recover_node = self.stack.pop(-1)
        recover_node.state = True
        recover_node.left.right = recover_node
        recover_node.right.left = recover_node


    def set_pointer(self, n):
        cur = self.head
        while n+1:
            self.pointer = cur.right
            n -= 1
            cur = cur.right


def solution(n, k, cmd):
    answer = ['X']*n
    dll = DLL()
    for i in range(n):
        node = Node(item=str(i), state=True)
        dll.insert(node)
    dll.set_pointer(k)


    for command in cmd:
        commands = command.split()
        if len(commands) > 1:
            if commands[0] == 'U' or commands[0] == 'D':
                dll.move(commands[0], int(commands[1]))
        elif commands[0] == 'C':
            dll.remove()
        elif commands[0] == 'Z':
            dll.recover()

    cur = dll.head
    while cur.right != dll.tail:
        answer[int(cur.right.data)] = 'O'
        cur = cur.right

    return ''.join(answer)


  
#   효율성  테스트
# 테스트 1 〉	통과 (2285.82ms, 238MB)
# 테스트 2 〉	통과 (2395.20ms, 238MB)
# 테스트 3 〉	통과 (2337.52ms, 238MB)
# 테스트 4 〉	통과 (2036.60ms, 244MB)
# 테스트 5 〉	통과 (2300.08ms, 244MB)
# 테스트 6 〉	통과 (1965.71ms, 244MB)
# 테스트 7 〉	통과 (481.87ms, 61.7MB)
# 테스트 8 〉	통과 (575.42ms, 75.7MB)
# 테스트 9 〉	통과 (2289.19ms, 245MB)
# 테스트 10 〉	통과 (2157.53ms, 245MB)
