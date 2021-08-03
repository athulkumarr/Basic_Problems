class NumberOfGoodSplits:
    def numSplits(self, s: str) -> int:

		good_splits = 0

		# Initialize 2 dictionaries to store the characters and their count in left split and right split. 
        L = {s[0]:1}
        R = {}

        for i in s[1:]:
            if i in R.keys():
                R[i] +=1
            else:
                R[i] = 1
		
		# Find the number of unique characters in each split
        Lc = len(L.keys())
        Rc = len(R.keys())
		
		# Iterate through the string
        for i in range(1,len(s)):
            
			# If the number of unique characters in left and right splits are equal, increment the number of good splits by 1
            if Lc == Rc: 
                good_splits +=1
            
			# Add this character to the left split
            if s[i] in L:
                L[s[i]] += 1
            else:
                L[s[i]] = 1
                Lc +=1
			# Remove this character from the right split
            if R[s[i]] == 1:
                R.pop(s[i])
                Rc -= 1
            else:
                R[s[i]] -= 1

        return good_splits
        
