class Solution:
    def __init__(self):
        self.res  = []
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        LEN = len(digits)
        hashmap = {
            '2': ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
        }
        if 1 == len(digits): 
            return hashmap[digits[0]]
        else:
            self.res = hashmap[digits[0]]
            l = len(res)
            def backTrack(ind):
                if ind == LEN: return
                else:
                    temp = []
                    for i in range(len(self.res)):
                        for ch in hashmap[digits[ind]]: 
                            temp.append(self.res[i]+ch)
                    self.res = temp.copy()
                    backTrack(ind+1)
            backTrack(1)
            return self.res