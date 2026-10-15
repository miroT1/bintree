import sys

class Node:
    def __init__(self, k):
        self.k = k
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, k):
        if self.root is None:
            self.root = Node(k)
            return
        c = self.root
        while True:
            if k < c.k:
                if c.left is None:
                    c.left = Node(k)
                    return
                c = c.left
            else:
                if c.right is None:
                    c.right = Node(k)
                    return
                c = c.right

    def find(self, k):
        parent = None
        node = self.root
        while node is not None and node.k != k:
            parent = node
            if k < node.k:
                node = node.left
            else:
                node = node.right
        return parent, node

    def rotate_left(self, k):
        parent, x = self.find(k)
        y = x.right
        x.right = y.left
        y.left = x
        if parent is None:
            self.root = y
        elif parent.left is x:
            parent.left = y
        else:
            parent.right = y

    def rotate_right(self, k):
        parent, x = self.find(k)
        y = x.left
        x.left = y.right
        y.right = x
        if parent is None:
            self.root = y
        elif parent.left is x:
            parent.left = y
        else:
            parent.right = y

    def preorder(self):
        res = []
        stack = [self.root]
        while stack:
            v = stack.pop()
            res.append(str(v.k))
            if v.right is not None:
                stack.append(v.right)
            if v.left is not None:
                stack.append(v.left)
        return res

def main():
    data = sys.stdin.buffer.read().split()
    i = 0
    n = int(data[i]); i += 1
    tree = BST()
    for _ in range(n): tree.add(int(data[i])); i += 1
    m = int(data[i]); i += 1
    out = []
    for _ in range(m):
        cmd = data[i].decode(); i += 1
        key = int(data[i]); i += 1
        if cmd == "left": tree.rotate_left(key)
        else: tree.rotate_right(key)
        out.append(" ".join(tree.preorder()))
    sys.stdout.write("\n".join(out) + "\n")
main()