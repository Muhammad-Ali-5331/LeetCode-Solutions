class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        MAP = Counter(list(map(str,digits)))
        for i in range(100,999):
            if i%2!=0: continue
            target = Counter(str(i))
            al = True
            for k,v in target.items():
                if MAP.get(k,0)<v:
                    al = False
                    break
            if al: res.append(i)
        return res