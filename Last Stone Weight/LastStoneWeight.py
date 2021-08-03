def lastStoneWeightII(self, stones: List[int]):
	
	# The idea is to split the stones array into 2 such that the sum of the elements of each array is as same as possible
	req = sum(stones) // 2

	# Initialize a DP table of size sum(stones)//2 + 1
	dp = [0]* (req+1)

	# dp stores whether a particular sum is possible with the stones in first subset, initially the first subset is empty.
	dp[0] = 1

	for s in stones:
		for i in range(req, -1, -1):
			# The sum 'i' is possible by adding stone s, only if i-s was possible before adding s.
			if i-s>=0 and dp[i-s]==1:
				dp[i] = 1

	for i in range(req, -1, -1):
		# Find the maximum possible sum with this subset
		if dp[i] == 1:
			print(sum(stones) - 2*i)
			return
