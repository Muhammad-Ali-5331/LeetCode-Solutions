# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def checkCritical(val1,val2,val3):
            return val1<val2>val3 or val1>val2<val3
        before = None
        curr = head
        after = curr.next
        minPos,maxPos = 0,-2
        prevPos,minD = -1,float("inf")
        cnt = 0
        i = 1
        while after:
            after = curr.next
            if before and after:
                if checkCritical(before.val,curr.val,after.val): # Check Critical point
                    maxPos = i # it's always the rightest most
                    minPos = i if minPos == 0 else minPos # Set to i if Not found else prev Pos
                    if prevPos!=-1:
                        minD = min(minD,i-prevPos)
                    cnt+=1
                    prevPos = i
            before = curr
            curr = after
            i+=1
        res = [-1 if minD == float("inf") else minD, max(-1,maxPos-minPos)]
        return res if cnt >= 2 else [-1,-1]