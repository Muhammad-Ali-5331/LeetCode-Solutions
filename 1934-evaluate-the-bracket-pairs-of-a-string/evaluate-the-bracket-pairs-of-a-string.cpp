#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string evaluate(string s, vector<vector<string>>& knowledge) {
        string res;
        int n = s.size();
        unordered_map<string,string> MAP;
        for (vector<string> r: knowledge){ MAP[r[0]] = r[1]; }
        int i = 0;
        while (i<n){
            if (s[i] == '('){
                i++;
                string currS;
                while (i<n && s[i] !=')'){currS+=s[i++];}
                res += MAP.count(currS) == 0 ? string("?") : MAP[currS];
                i++;
            }
            else { res += s[i++]; }
        }
        return res;
    }
};