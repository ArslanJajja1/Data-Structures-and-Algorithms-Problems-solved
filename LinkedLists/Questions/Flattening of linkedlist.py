def merge(a, b):
    temp = None
    res = temp
    while a and b:
        if a.val < b.val:
            temp.bottom = a
            temp = temp.bottom
            a = a.bottom
        else:
            temp.bottom = b
            temp = temp.bottom
            b = b.bottom
        if not a:
            temp.bottom = b
        if not b:
            temp.bottom = a
        return res.bottom


def flatten(root):
    if not root or not root.next:
        return root
    root.next = flatten(root.next)
    root = merge(root, root.next)
    return root
