## Problem Description
  
Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.
Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.

## Input 1:
    nums = [5,3,2,4]
## Output 1:
    2
## Explanation 1:
    Change the array [5,3,2,4] to [2,2,2,2].
    The difference between the maximum and minimum is 2-2 = 0.

## Input 2:
    nums = [1,5,0,10,14]
## Output 2:
    1
## Explanation 2:
    Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
    The difference between the maximum and minimum is 1-0 = 1.

## Input 3:
    nums = [6,6,0,1,1,4,6]
## Output 3:
    2
## Explanation 3:
    Change the array [6,6,0,1,1,4,6] to [6,6,5,5,5,4,6]. 
    The difference between the maximum and minimum is 6-4 = 2.
