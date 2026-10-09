class Solution:
    def minInsertions(self, s: str) -> int:
        ops = 0
        n = len(s)
        opsCount = 0
        i = 0
        while i<n:
            ch = s[i]
            if ch == '(': opsCount+=1
            else:
                # Combining Two Closing Brackets as One
                if i+1<n and s[i+1] == ')': 
                    i+=1
                    # Check if we have opening bracket for them
                    if opsCount:  opsCount-=1
                    else: ops+=1 # Else it requires placing one opening bracket (1 Operation)
                else:
                    #It reuqires placing one closing bracket to form closing brackets
                    ops+=1
                    # Check if we have opening bracket for them
                    if opsCount: opsCount-=1
                    else: ops+=1 # Else it requires placing one opening bracket (1 Operation)
            i+=1

        # only remains the opening brackets, so we require two steps for all of them
        return ops +  opsCount*2