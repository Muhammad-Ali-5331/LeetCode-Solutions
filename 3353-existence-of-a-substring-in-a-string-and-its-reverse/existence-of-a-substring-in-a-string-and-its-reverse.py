class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev = s[::-1]
        print(f"Rev: {rev}")
        for i in range(len(s)-1):
            cS = s[i]+s[i+1]
            print(f"CS: {cS}")
            if cS in rev: return True
        return False