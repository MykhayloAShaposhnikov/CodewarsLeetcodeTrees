class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return f'{self.left}, {self.val}, {self.right}'
# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    res = []
    def _pre_order(node):
        if node:
            res.append(node.data)
            _pre_order(node.left)
            _pre_order(node.right)
        if node is None:
            return res
    _pre_order(node)
    return res

def in_order(node):
    if node is None:
        return []
    res = []
    def _in_order(node):
        if node:
            _in_order(node.left)
            res.append(node.data)
            _in_order(node.right)
        if node is None:
            return res
    _in_order(node)
    return res
def post_order(node):
    if node is None:
        return []
    res = []
    def _post_order(node):
        if node:
            _post_order(node.left)
            _post_order(node.right)
            res.append(node.data)
        if node is None:
            return res
    _post_order(node)
    return res

