class Solution:
    def minimizeSum(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort(reverse=True)
        mi = float('inf')
        mi = min(mi, arr[1]-arr[-2])
        mi = min(mi, arr[2]-arr[-1])
        mi = min(mi, arr[0]-arr[-3])
        return mi