import sys
class Node:
    __slots__ = ("k", "l", "r", "h")
    def __init__(self, k):
        self.k = k
        self.l = None
        self.r = None
        self.h = 1

def H(v):   return v.h if v else 0
def upd(v): v.h = 1 + max(H(v.l), H(v.r))
def bal(v): return H(v.r) - H(v.l)         

def rot_r(v):
    x = v.l
    v.l = x.r
    x.r = v
    upd(v); upd(x)
    return x

def rot_l(v):
    x = v.r
    v.r = x.l
    x.l = v
    upd(v); upd(x)
    return x

def add(v, k):
    if v is None:
        return Node(k)
    if k < v.k:
        v.l = add(v.l, k)
    elif k > v.k:
        v.r = add(v.r, k)
    else:
        return v                           
    upd(v)
    b = bal(v)
    if b == 2:                            
        if bal(v.r) >= 0:
            return rot_l(v)                 
        v.r = rot_r(v.r)
        return rot_l(v)                     
    if b == -2:                            
        if bal(v.l) <= 0:
            return rot_r(v)                
        v.l = rot_l(v.l)
        return rot_r(v)                     
    return v

def exists(v, k):
    while v:
        if k == v.k: return True
        v = v.l if k < v.k else v.r
    return False

def preorder(v):
    if not v: return []
    res, st = [], [v]
    while st:
        x = st.pop()
        res.append(str(x.k))
        if x.r: st.append(x.r)
        if x.l: st.append(x.l)
    return res

def main():
    data = sys.stdin.buffer.read().split()
    i = 0
    q = int(data[i]); i += 1
    root = None
    out = []
    for _ in range(q):
        c = data[i].decode(); i += 1
        if c == "add": root = add(root, int(data[i])); i += 1
        elif c == "exists": out.append("YES" if exists(root, int(data[i])) else "NO"); i += 1
        elif c == "root": out.append(str(root.k) if root else "Empty")
        elif c == "height": out.append(str(H(root)))
        elif c == "print":
            p = preorder(root)
            out.append("Empty" if not p else " ".join(p))
    sys.stdout.write("\n".join(out) + "\n")
main()