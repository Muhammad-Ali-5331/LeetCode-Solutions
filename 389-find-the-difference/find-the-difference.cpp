class Solution {
public:
    char findTheDifference(string s, string t) {
        char res = '1';
        unordered_map<char,int> mp1;
        unordered_map<char,int> mp2;
        for (auto ch: s){mp1[ch]+=1;}
        for (auto ch: t){mp2[ch]+=1;}
        for (auto ch: t){if (mp2[ch]!=mp1[ch]) {res = ch;break;}}
        return res;
    }
};