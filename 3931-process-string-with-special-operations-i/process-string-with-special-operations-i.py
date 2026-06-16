class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for ch in s:
            if ch.isalpha(): res.append(ch)
            elif ch == "*":
                if res: res.pop()
            elif ch == "#": res += res
            else: res = res[::-1]
        return "".join(res)