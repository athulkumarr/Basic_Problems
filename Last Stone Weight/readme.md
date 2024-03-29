## Problem Description
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. 

Suppose the stones have weights x and y with x <= y. The result of this smash is:

    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

## Input 1:
    stones = [2,7,4,1,8,1]
## Output 1:
    1
## Explanation 1:
    We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
    we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
    we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
    we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.

## Input 2:
    stones = [31,26,33,21,40]
## Output 2:
    5
## Explanation 2:
    We can combine 21 and 40 to get 19, so the array converts to [31,26,33,19] then,
    we can combine 33 and 26 to get 7, so the array converts to [31,7,19] then,
    we can combine 31 and 19 to get 12, so the array converts to [7,12] then,
    we can combine 7 and 12 to get 5, so the array converts to [5], then that's the optimal value.

## Input 3:
    stones = [1,2]
## Output 3:
    1
## Explanation 3:
    we can combine 2 and 1 to get 1, that's the optimal value.
