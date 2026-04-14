class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backTrack(openingCount,closingCount,li):
            if openingCount == n and closingCount == n:
                res.append("".join(li))
                return
            if closingCount < openingCount:
                li.append(')')
                backTrack(openingCount,closingCount+1,li)
                li.pop()
            if openingCount!=n:
                li.append('(')
                backTrack(openingCount+1,closingCount,li)
                li.pop()
        backTrack(0,0,[])
        return res