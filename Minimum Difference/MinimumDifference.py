from heapq import nlargest, nsmallest

class MinimumDifference:    
	def minimumDifference(self, nums: List[int]) -> int:
		
		# If there are 3 or less elements in the list, all of them can be made equal and the difference will be zero.
		if len(nums) < 4:
            return 0
        
		# Find the largest 4 and smallest 4 numbers in the list.
        top_4 = nlargest(4, nums)
        least_4 = nsmallest(4, nums)
        
		# We have 4 different options namely 
		# remove all 3 from the largest, 
		# remove 2 from largest 1 from smallest, 
		# remove 1 from largest 2 from smallest, 
		# remove all 3 from smallest
		
        return int (min
        (
            top_4[3] - least_4[0],
            top_4[2] - least_4[1],
            top_4[1] - least_4[2],
            top_4[0] - least_4[3]
        ))
