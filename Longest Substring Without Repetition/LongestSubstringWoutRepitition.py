def lengthOfLongestSubstring(self, s: str) -> int:
		if len(s)==0:
				return 0
		left = 0
		viewedC = {} # store unique character's index
		maxLength = 0

		for right, c in enumerate(s):
				if c not in viewedC:
						viewedC[c] = right
				else:

						if viewedC[c] < left: 		# update unique character's index
								viewedC[c] = right
						else:
								length = right - left
								if length > maxLength: 
										maxLength = length
								left = viewedC[c] + 1

								viewedC[c] = right	# update unique character's index

		length = len(s[left:]) 

		return maxLength if maxLength > length else length
