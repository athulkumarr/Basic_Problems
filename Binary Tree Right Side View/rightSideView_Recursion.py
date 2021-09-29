def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
   def rightview(root, level, order):
       if root is None:
           return

       if len(order) == level:
           order.append(root.val)
       rightview(root.right, level + 1, order)
       rightview(root.left, level + 1, order)
       return order
   return rightview(root, 0, [])
