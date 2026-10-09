class Solution:
    def minInsertions(self, s: str) -> int:
        ops = 0
        n = len(s)
        stk = []
        i = 0
        while i<n:
            ch = s[i]
            if ch == '(':
                stk.append('(')
                i+=1
            else:
                # Combining Two Closing Brackets as One
                if i+1<n and s[i+1] == ')': 
                    i+=1
                    # Check if we have opening bracket for them
                    if stk and stk[-1] == "(": stk.pop()
                    else: ops+=1 # Else it requires placing one opening bracket (1 Operation)
                else:
                    #It reuqires placing one closing bracket to form closing brackets
                    ops+=1
                    # Check if we have opening bracket for them
                    if stk and stk[-1] == "(":stk.pop()
                    else: ops+=1 # Else it requires placing one opening bracket (1 Operation)
                i+=1
        while stk:
            stk.pop()
            ops+=2
        return ops