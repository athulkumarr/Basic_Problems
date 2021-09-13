def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
    def bin_search(arr, val):
        low = 0
        high = len(arr)

        while low<high:
            m = (high+low)//2
            if arr[m] <= val:
                high = m
            else:
                low = m+1
        return low

    f = []
    for i in range(len(words)):
        f.append(words[i].count(sorted(words[i])[0]))
    f = sorted(f, reverse = True)
    ans = []
    for i in range(len(queries)):
        f_q_i = queries[i].count(sorted(queries[i])[0])
        ans.append(bin_search(f,f_q_i))
    return ans
