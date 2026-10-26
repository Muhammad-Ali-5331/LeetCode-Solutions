class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<vector<int>> ppl(n+1,vector<int>(2,0));
        for (vector<int> node: trust){
            int u = node[0];
            int v = node[1];
            ppl[u][0]++;
            ppl[v][1]++;
        }
        for (int i = 1; i<=n; i++){
            if ((ppl[i][0] == 0) && (ppl[i][1] == (n-1))) return i;
        }
        return -1;
    }
};