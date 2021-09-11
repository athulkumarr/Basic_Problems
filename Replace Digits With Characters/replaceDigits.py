def replaceDigits(self, s: str) -> str:
        def shift(ch, n):
            asci = ord(ch)+(n%26)
            return chr(asci)
                
        new_s = ""
        for i in range(0,len(s),2):
            if i==len(s)-1:
                new_s +=s[i]
            else:
                new_s +=s[i]+shift(s[i], int(s[i+1]))
        
        return str(new_s)
