class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def getPrd(X):
            digs = list(map(int,list(str(X))))
            res = 1
            for dig in digs: res*=dig
            return res
        while True:
            if getPrd(n)%t == 0: return n
            n+=1