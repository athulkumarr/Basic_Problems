def isNumber(self, s: str) -> bool:
    digit = False
    exp = False
    dot = False
    s = s.lower() 
    for i, ch in enumerate(s):
        if ch.isdigit():
            digit = True

        elif ch in {'+','-'}:
            if i>0 and s[i-1] !='e':
                return False

        elif ch == 'e':
            if not digit or exp:
                return False
            exp = True
            digit = False

        elif ch == '.':
            if dot or exp:
                return False
            dot = True

        else:
            return False

    return digit
