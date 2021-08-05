# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BFS_Level_Sum:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = 1
        maxSum = float('-inf')
        maxLevel = 1
        queue = deque([root])
        
        while queue:
			
            total = 0
            n = len(queue)
            
			for _ in range(n):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
			if total>maxSum:
                maxSum,maxLevel = total, level
            
            level = level+1
        
        return maxLevel
