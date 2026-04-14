class Solution:
    def sortColors(self, arr: List[int]) -> None:
        start = 0
        mid = 0
        end = len(arr)-1
        while mid<=end:
            if arr[mid] == 0:
                arr[start],arr[mid] = arr[mid],arr[start]
                start+=1
                mid+=1
            elif arr[mid] == 2:
                arr[end],arr[mid] = arr[mid],arr[end]
                end-=1
            else:mid+=1