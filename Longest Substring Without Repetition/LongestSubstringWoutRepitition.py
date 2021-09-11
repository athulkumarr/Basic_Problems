def lengthOfLongestSubstring(self, s: str) -> int:
		if len(s)==0:
				return 0
		start = 0
		end = 0
		max_len = 0
		while start<len(s):
				if end >= len(s):
						max_len = max(max_len, end-start)
						break
				elif s[end] in s[start:end]:
						max_len = max(max_len, end-start)
						start += 1
						end = start
				else:
						end += 1
		return max_len
