## Problem Description

Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once. <br/>

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. <br/>

The earliest 24-hour time is 00:00, and the latest is 23:59.<br/>

Return the latest 24-hour time in "HH:MM" format.  If no valid time can be made, return an empty string.<br/>

## Input 1:
		arr = [0,0,1,0]
## Output 1:
		"10:00"
## Explanation 1:
		The valid 24-hour times are "00:01", "00:10", "01:00", and "10:00". 
		Of these times, "10:00" is the latest.

## Input 2:
		arr = [1,2,3,4]
## Output 2:
		"23:41"
## Explanation 2:
		The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". 
		Of these times, "23:41" is the latest.

## Input 3:
		arr = [5,5,5,5]
## Output 3:
		""
## Explanation 3:
		The only possible combination is "55:55" which is not a valid 24-hour time.
