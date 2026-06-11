class Solution {
public:
    int countSegments(string s) {
        int c = 0;
        stringstream ss(s);
        string word;
        while(ss>>word) c++;
        return c;
    }
};