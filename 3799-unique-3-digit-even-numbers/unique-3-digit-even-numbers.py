class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = 0
        print(set(permutations(digits,r=3)))
        for p in set(permutations(digits,r=3)):
            if p[0]!=0 and p[-1]%2 == 0: count+=1
        return count