## Problem Description

You are given a string s. <br/>

A split is called good if you can split s into 2 non-empty strings p and q where its concatenation is equal to s and the number of distinct letters in p and q are the same.

Return the number of good splits you can make in s.

## Input 1
	s = "aacaba"
## Output 1
	2
## Explanation 1 
	There are 5 ways to split "aacaba" and 2 of them are good. 
	{"a", "acaba"} Left string and right string contains 1 and 3 different letters respectively.
	{"aa", "caba"} Left string and right string contains 1 and 3 different letters respectively.
	{"aac", "aba"} Left string and right string contains 2 and 2 different letters respectively.
	{"aaca", "ba"} Left string and right string contains 2 and 2 different letters respectively.
	{"aacab", "a"} Left string and right string contains 3 and 1 different letters respectively.
	
	Out of the 5 splits shown above, {"aac", "aba"} & {"aaca", "ba"} are the only good splits
	
## Input 2
	s = "aaaaa"
## Output 2
	4
## Explanation 2
	{"a", "aaaa"} Left string and right string both contains 1 unique letters.
	{"aa", "aaa"} Left string and right string both contains 1 unique letters.
	{"aaa", "aa"} Left string and right string both contains 1 unique letters.
	{"aaaa", "a"} Left string and right string both contains 1 unique letters.

	All these splits are good splits.
	
## Input 3
	s = "acbadbaada"
## Output 3
	2
## Explanation 3
	{"a", "cbadbaada"} Left string and right string contains 1 and 4 different letters respectively.
	{"ac", "badbaada"} Left string and right string contains 2 and 3 different letters respectively.
	{"acb", "adbaada"} Left string and right string contains 3 and 3 different letters respectively.
	{"acba", "dbaada"} Left string and right string contains 3 and 3 different letters respectively.
	{"acbad", "baada"} Left string and right string contains 4 and 3 different letters respectively.
	{"acbadb", "aada"} Left string and right string contains 4 and 2 different letters respectively.
	{"acbadba", "ada"} Left string and right string contains 4 and 2 different letters respectively.
	{"acbadbaa", "da"} Left string and right string contains 4 and 2 different letters respectively.
	{"acbadbaad", "a"} Left string and right string contains 4 and 1 different letters respectively.
	
	Out of this only {"acb", "adbaada"} & {"acba", "dbaada"} are good splits.
	
