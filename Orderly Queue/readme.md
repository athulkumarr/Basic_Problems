## Problem Description

You are given a string s and an integer k. 
You can choose one of the first k letters of s and append it at the end of the string..
Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.

## Input 1: 
    s = "cba", k = 1
## Output 1: 
    "acb"
## Explanation: 
    In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
    In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".

## Input 2: 
    s = "baaca", k = 3
## Output 2: 
    "aaabc"
## Explanation: 
    In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
    In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".
