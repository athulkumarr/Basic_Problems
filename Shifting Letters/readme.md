## Problem Description
You are given a string s of lowercase English letters and an integer array shifts of the same length.
Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.


## Input 1: 
    s = "abc", shifts = [3,5,9]
## Output 1: 
    "rpl"
## Explanation: 
    We start with "abc".
    After shifting the first 1 letters of s by 3, we have "dbc".
    After shifting the first 2 letters of s by 5, we have "igc".
    After shifting the first 3 letters of s by 9, we have "rpl", the answer.

## Input 2: 
    s = "aaa", shifts = [1,2,3]
## Output 2: 
    "gfd"
## Explanation
    We start with "aaa".
    After shifting the first 1 letters of s by 1, we have "baa".
    After shifting the first 2 letters of s by 2, we have "dca".
    After shifting the first 3 letters of s by 3, we have "gfd", the answer.
