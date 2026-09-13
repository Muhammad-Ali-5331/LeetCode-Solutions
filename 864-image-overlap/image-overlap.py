class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        cords1,cords2 = [],[]
        for i in range(n):
            for j in range(n):
                if img1[i][j]: cords1.append((i,j))
        for i in range(n):
            for j in range(n):
                if img2[i][j]: cords2.append((i,j))
        trans = defaultdict(int)
        for r1,c1 in cords1:
            for r2,c2 in cords2:
                changeR = r2-r1
                changeC = c2-c1
                trans[(changeR,changeC)]+=1
        mx = trans.values()
        return max(mx) if len(mx) else 0