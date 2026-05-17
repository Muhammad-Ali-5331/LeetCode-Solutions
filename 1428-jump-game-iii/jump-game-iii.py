class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        L = len(arr)
        q = deque()
        q.append(start)
        visit = set()
        while q:
            currInd = q.popleft()
            if arr[currInd] == 0: return True
            if currInd in visit: continue
            visit.add(currInd)
            jump1 = currInd+arr[currInd]
            jump2 = currInd-arr[currInd] 
            if 0<=jump1<L and jump1 not in visit: q.append(jump1)
            if 0<=jump2<L and jump2 not in visit: q.append(jump2)
        return False