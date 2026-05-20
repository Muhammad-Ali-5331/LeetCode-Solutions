class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s1 = set()
        s2 = set()
        res = []
        c = 0
        for i in range(len(A)):
            s1.add(A[i])
            s2.add(B[i])
            if A[i] == B[i]: c+=1
            else:
                c+= 1 if A[i] in s2 else 0
                c+= 1 if B[i] in s1 else 0
            res.append(c)
        return res