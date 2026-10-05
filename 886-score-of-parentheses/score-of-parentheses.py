class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        li = list(s)
        replaced = True
        while replaced:
            replaced = False
            for i in range(1,len(li)):
                if li[i] == ")":
                    replaced = True
                    # Only One bracket pair "()"
                    if li[i-1] == "(":
                        li[i-1:i+1] = [1]
                    else:
                        curS = 0
                        prevP = i-1
                        while li[prevP]!='(':
                            curS += li[prevP]
                            prevP-=1
                        li[prevP:i+1] = [2*curS]
                    break
        return sum(li)