class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char,int> MAP;
        for (char &ch: text) MAP[ch]++;
        int bC = MAP['b'];
        int aC = MAP['a'];
        int nC = MAP['n'];
        int lC = MAP['l']/2;
        int oC = MAP['o']/2;
        return min(min(min(bC,aC),nC),min(lC,oC));
    }
};