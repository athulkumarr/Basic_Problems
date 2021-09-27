# Problem Description

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

# Input 1: 
    nums1 = [1,3], nums2 = [2]
# Output 1: 
    2.00000
# Explanation: 
    merged array = [1,2,3] and median is 2.

# Input 2: 
    nums1 = [1,2], nums2 = [3,4]
# Output 2: 
    2.50000
# Explanation: 
    merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Input 3: 
    nums1 = [0,0], nums2 = [0,0]
# Output 3: 
    0.00000

# Input 4: 
    nums1 = [], nums2 = [1]
# Output 4: 
    1.00000

# Input 5: 
    nums1 = [2], nums2 = []
# Output 5: 
    2.00000
