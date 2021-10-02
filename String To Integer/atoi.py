def myAtoi(self, s: str) -> int:   
    st = 0
    sign = 1
    s = s.strip()
    if len(s)<1:
        return 0
    sign = 1
    index = 0
    if s[0] == '-':
        sign = -1
        index += 1

    if s[0] == '+':
        sign = +1
        index += 1

    while index<len(s) and s[index].isdigit():
        st = st*10 + int(s[index])
        index += 1

    return min(max(st*sign, -2**31), 2**31-1)
