def largestTimeFromDigits(self, arr: List[int]) -> str:
		
		# Initialize best time to ""
		best = ""
		h1, h2, m1, m2 = 0, 0, 0, 0
		
		# If there is no digit available for h1
		if min(arr) > 2:
				return ""
		
		for i, h1 in enumerate(arr):
				for j, h2 in enumerate(arr):
						for k, m1 in enumerate(arr):
							
								# Ignore the repetition of digits
								if i==j or j==k or k==i:
										continue
							
								m2 = arr[6-i-j-k]

								s = str(h1)+str(h2)+":"+str(m1)+str(m2)

								if (h1*10+h2) < 24 and (m1*10+m2) < 60 and s > best:
										best = s
		return best
