import operator
import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, idx, value):
        self.idx = idx
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None
        self.postorder_answer = []
        self.preorder_answer = []

    def insert(self, idx, value):
        self.root = self._insert_value(self.root, idx, value)
        return self.root is not None

    def _insert_value(self, node, idx, value):
        if node is None:
            node = Node(idx, value)
        else:
            if value <= node.value:
                node.left = self._insert_value(node.left, idx, value)
            else:
                node.right = self._insert_value(node.right, idx, value)
        return node

    def preorder(self, n):
        if n != None:
            self.preorder_answer.append(n.idx)
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            self.postorder_answer.append(n.idx)


def solution(nodeinfo):
    tree = BinaryTree()

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(nodeinfo[i][0] * -1)
        nodeinfo[i].append(i)
    sorted_nodeinfo = sorted(nodeinfo, key=operator.itemgetter(1, 2), reverse=True)
    for x, y, _, i in sorted_nodeinfo:
        tree.insert(i+1, x)

    tree.preorder(tree.root)
    tree.postorder(tree.root)
    return [tree.preorder_answer, tree.postorder_answer]


# 정확성  테스트
# 테스트 1 〉	통과 (0.03ms, 10.3MB)
# 테스트 2 〉	통과 (0.05ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (115.64ms, 11.4MB)
# 테스트 7 〉	통과 (100.58ms, 11.4MB)
# 테스트 8 〉	통과 (63.24ms, 12.5MB)
# 테스트 9 〉	통과 (315.47ms, 16.1MB)
# 테스트 10 〉	통과 (18.85ms, 11.3MB)
# 테스트 11 〉	통과 (277.82ms, 15.9MB)
# 테스트 12 〉	통과 (362.08ms, 16MB)
# 테스트 13 〉	통과 (0.64ms, 10.4MB)
# 테스트 14 〉	통과 (5.13ms, 10.7MB)
# 테스트 15 〉	통과 (26.92ms, 13.1MB)
# 테스트 16 〉	통과 (69.05ms, 15.6MB)
# 테스트 17 〉	통과 (8.71ms, 10.7MB)
# 테스트 18 〉	통과 (52.03ms, 15.7MB)
# 테스트 19 〉	통과 (9.01ms, 11.3MB)
# 테스트 20 〉	통과 (23.59ms, 12.6MB)
# 테스트 21 〉	통과 (32.01ms, 13.7MB)
# 테스트 22 〉	통과 (56.94ms, 15.6MB)
# 테스트 23 〉	통과 (64.99ms, 15.7MB)
# 테스트 24 〉	통과 (0.03ms, 10.3MB)
# 테스트 25 〉	통과 (0.03ms, 10.2MB)
# 테스트 26 〉	통과 (231.01ms, 11.8MB)
# 테스트 27 〉	통과 (0.05ms, 10.3MB)
# 테스트 28 〉	통과 (0.08ms, 10.3MB)
# 테스트 29 〉	통과 (0.01ms, 10.2MB)
