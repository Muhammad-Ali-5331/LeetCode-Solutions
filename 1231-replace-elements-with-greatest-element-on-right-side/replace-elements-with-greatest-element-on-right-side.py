class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0]*n
        res[-1] = -1
        mx = arr[-1]
        for i in range(len(arr)-2, -1, -1 ):
            res[i] = mx
            mx = max(arr[i],mx)
        return res