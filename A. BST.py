import sys


class Node:
    def __init__(self, k):
        self.k = k
        self.l = None
        self.r = None

def add(root, x):
    if root is None:
        return Node(x)
    cur = root
    while True:
        if x == cur.k:
            return root
        if x < cur.k:
            if cur.l is None:
                cur.l = Node(x)
                return root
            cur = cur.l
        else:
            if cur.r is None:
                cur.r = Node(x)
                return root
            cur = cur.r

def exists(root, x):
    cur = root
    while cur is not None:
        if x == cur.k:
            return True
        cur = cur.l if x < cur.k else cur.r
    return False

def height(root):
    if root is None:
        return 0
    best = 0
    stack = [(root, 1)]
    while stack:
        v, d = stack.pop()
        if d > best:
            best = d
        if v.l is not None:
            stack.append((v.l, d + 1))
        if v.r is not None:
            stack.append((v.r, d + 1))
    return best

def delete(root, x):
    parent = None
    cur = root
    while cur is not None and cur.k != x:
        parent = cur
        cur = cur.l if x < cur.k else cur.r
    if cur is None:
        return root

    if cur.l is not None and cur.r is not None:
        p = cur
        m = cur.r
        while m.l is not None:
            p = m
            m = m.l
        cur.k = m.k
        if p.l is m:
            p.l = m.r
        else:
            p.r = m.r
        return root

    child = cur.l if cur.l is not None else cur.r
    if parent is None:
        return child
    if parent.l is cur:
        parent.l = child
    else:
        parent.r = child
    return root

def preorder(root):
    if root is None:
        return []
    res = []
    stack = [root]
    while stack:
        v = stack.pop()
        res.append(str(v.k))
        if v.r is not None:
            stack.append(v.r)
        if v.l is not None:
            stack.append(v.l)
    return res

def main():
    data = sys.stdin.buffer.read().split()
    i = 0
    q = int(data[i])
    i += 1
    root = None
    out = []
    for _ in range(q):
        cmd = data[i].decode()
        i += 1
        if cmd == "add":
            root = add(root, int(data[i]))
            i += 1
        elif cmd == "del":
            root = delete(root, int(data[i]))
            i += 1
        elif cmd == "exists":
            out.append("YES" if exists(root, int(data[i])) else "NO")
            i += 1
        elif cmd == "height":
            out.append(str(height(root)))
        elif cmd == "print":
            vals = preorder(root)
            out.append("Empty" if not vals else " ".join(vals))
    sys.stdout.write("\n".join(out) + "\n")
main()