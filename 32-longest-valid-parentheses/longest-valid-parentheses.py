class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if 0<=len(s)<=1:
            return 0
        max_length = 0
        left=right=0
        for i in range(len(s)):
            if s[i] == '(':
                left+=1
            else:
                right+=1
            if(right > left): left=right=0
            elif(left==right): max_length = max(max_length,left+right)
            
        left=right=0
        for i in range(len(s)-1,0,-1):
            if s[i] == '(':
                left+=1
            else:
                right+=1
            if(left > right): left=right=0
            elif(left==right): max_length = max(max_length,left+right)

        return max_length