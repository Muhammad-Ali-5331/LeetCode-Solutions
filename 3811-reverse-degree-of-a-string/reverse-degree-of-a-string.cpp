class Solution {
public:
    int reverseDegree(string s) {
        int res = 0;
        for(int i = 0; i<s.size(); i++){
            char ch = s[i];
            int diff = 'z' - ch + 1;
            res += (i+1)*diff;
        }
        return res;
    }
};