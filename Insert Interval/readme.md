# Problem Description
You are given an array of non-overlapping intervals intervals where 
intervals[i] = [starti, endi] represent the start and the end of the ith interval 
and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and 
intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

# Input 1: 
    intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output 1: 
    [[1,5],[6,9]]

# Input 2: 
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output 2: 
    [[1,2],[3,10],[12,16]]

# Input 3: 
    intervals = [], newInterval = [5,7]
# Output 3: 
    [[5,7]]

# Input 4: 
    intervals = [[1,5]], newInterval = [2,3]
# Output 4: 
    [[1,5]]

# Input 5: 
    intervals = [[1,5]], newInterval = [2,7]
# Output 5:
    [[1,7]]
