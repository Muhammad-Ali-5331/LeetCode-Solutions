class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        res = 0
        i = 0
        sign = 1
        signs = {"+","-"}
        if s[0] in signs:
            sign = sign*-1 if s[0] == '-' else sign
            s = s[1::]
        spes = {'-','+'}
        while i<len(s):
            if s[i].isnumeric():
                res = res*(10) + int(s[i])
            else:
                break
            i+=1
        higherLimit = 2**31 -1
        lowerLimit = -2**31
        if res * sign >= higherLimit:
            return higherLimit
        elif res * sign <= lowerLimit:
            return lowerLimit
        else:
            return res * sign