class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [1]*n
        for i in range(n): arr[i] = [arr[i],i]
        arr.sort(key = lambda x: x[0])
        rank = 1
        i = 0
        while i<n:
            num,ind = arr[i]
            res[ind] = rank
            i+=1
            while i<n and arr[i][0] == num:
                newNum,newInd = arr[i]
                res[newInd] = rank
                i+=1
            rank+=1
        return res