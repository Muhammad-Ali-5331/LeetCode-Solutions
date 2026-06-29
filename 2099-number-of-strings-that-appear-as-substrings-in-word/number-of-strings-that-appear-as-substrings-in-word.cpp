class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        unordered_map<string,int> MAP;
        int n = word.size();
        for (int i = 0; i<n; i++){
            string S;
            for (int j = i;j<n;j++){S+=word[j]; MAP[S]++;}
        }
        int c = 0;
        for (string &w: patterns){c += MAP[w]>=1;}
        return c;
    }
};