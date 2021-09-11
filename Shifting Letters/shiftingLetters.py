def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        def shift(ch, n):
            asci = ord(ch)+(n%26)
            if asci<=122:
                return chr(asci)
            return chr(96+(asci%122))
                
        new_s = ""
        for i in range(len(shifts)-2, -1, -1):
            shifts[i] += shifts[i+1]
        
        for i in range(len(s)):
            new_s += shift(s[i], shifts[i])
        
        return str(new_s)
