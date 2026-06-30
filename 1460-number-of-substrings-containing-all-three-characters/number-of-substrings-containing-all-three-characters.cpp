class Solution {
public:
    int numberOfSubstrings(string s) {
        int count = 0;
        int n = s.size();
        unordered_map<char,int> MAP;
        int l = 0,r = 0;
        while (r<=n){
            while (MAP['a'] >= 1 and MAP['b'] >= 1 and MAP['c'] >= 1){
                count++;
                count += n-r;
                MAP[s[l]]--;
                l++;
            }
            if (r == n) break;
            MAP[s[r]]++;
            r++;
        }
        return count;
    }
};