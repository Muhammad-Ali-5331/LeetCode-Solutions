class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        d = Counter(moves)
        if not 'L' in d and not 'R' in d: return d['_']
        if d['L']>=d['R']: return abs(d['L'] + d.get('_',0) - d.get('R',0))
        else: return abs(d['R'] + d.get('_',0) - d.get('L',0))