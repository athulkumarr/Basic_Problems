def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    final=[]
    if root:
        final.append(root.val)
        q = deque([root])
    else:
        return final
    while(q):
        n = len(q)
        l = []
        for i in range(n):
            m = q.popleft()
            if m.left:
                q.append(m.left)
                l.append(m.left)
            if m.right:
                q.append(m.right)
                l.append(m.right)
        if l:
            final.append(l[-1].val)
    return final
