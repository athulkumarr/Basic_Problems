def time_taken(keyboard, text):
	
    res, curr = 0, 0
	map = {char: i for i,char in enumerate(keyboard)}
    
	for char in text:
        diff = abs(map[char] - curr)
        res += diff
        curr = map[char]

	return res
