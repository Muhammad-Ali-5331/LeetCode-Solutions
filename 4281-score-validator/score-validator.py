class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        li = [0,0]
        i = 0
        addS = {"WD","NB"}
        while i<len(events) and li[1]<10:
            if events[i] in addS: li[0]+=1
            elif events[i].isnumeric(): li[0]+=int(events[i])
            else: li[1]+=1
            i+=1
        return li