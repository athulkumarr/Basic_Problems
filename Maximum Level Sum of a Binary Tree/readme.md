## Problem Description

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

## Input 1:
		[989,null,10250,98693,-89388,null,null,null,-20167]
## Output 1:
		2
## Explanation 1:
		Level 1 sum = 989.
		Level 2 sum = 10250.
		Level 3 sum = 98693 + -89388 = 9305.
		Level 4 sum = -20167.
		So we return the level with the maximum sum which is level 2.

## Input 2:
		root = [1,7,0,7,-8,null,null]
## Output 2:
		2
## Explanation 2:
		Level 1 sum = 1.
		Level 2 sum = 7 + 0 = 7.
		Level 3 sum = 7 + -8 = -1.
		So we return the level with the maximum sum which is level 2
