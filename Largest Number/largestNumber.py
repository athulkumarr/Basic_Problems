class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class LargestNumber:
    def largestNumber(self, nums: List[int]) -> str:
        st = ''.join(sorted(map(str,nums), key = LargerNumKey)) 
        st = st if st[0] != '0' else '0'
        return st
