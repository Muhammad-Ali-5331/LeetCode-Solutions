class Solution {
public:
    string largestEven(string s) {
        int n = s.size();
        string res = "";
        int i = n-1;
        while (i>=0 and s[i] == '1') i--;
        int j = 0;
        while (j<=i){res+=s[j++];}
        return res;
    }
};