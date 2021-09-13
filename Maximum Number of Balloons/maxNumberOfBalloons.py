def maxNumberOfBalloons(self, text: str) -> int:
		ch_list = {"b":0,"a":0,"l":0,"o":0,"n":0}
		for i in text:
				if i in ch_list.keys():
						if i in ("l","o"):
								ch_list[i] += 1
						else:
								ch_list[i] += 2
		return min(ch_list.values())//2
