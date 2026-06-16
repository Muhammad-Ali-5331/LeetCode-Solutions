class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3: return False
        n = len(arr)
        i = 0
        inc = False
        dec = False
        while i<n-1:
            while i<n-1 and arr[i]<arr[i+1]: 
                i+=1
                inc = True
            while i<n-1:
                if not arr[i]>arr[i+1]:
                    return False
                else: i+=1
                dec = True
        return inc and dec