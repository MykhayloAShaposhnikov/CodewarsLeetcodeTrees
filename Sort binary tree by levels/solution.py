from collections import deque
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
def tree_by_levels(node):
    if node is None:
        return []
    res = [node.value]
    q = deque([node])
    while q:
        popped = q.popleft()
        if popped.left is not None:
            res.append(popped.left.value)
            q.append(popped.left)
        if popped.right is not None:
            res.append(popped.right.value)
            q.append(popped.right)
    return res
