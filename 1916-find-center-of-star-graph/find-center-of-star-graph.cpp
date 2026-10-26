class Solution {
public:
    int findCenter(vector<vector<int>>& e) {
        int n = 1e5;
        int eS = e.size();
        int mx = 1;
        vector<vector<int>> dist(n+1, vector<int>(2,0));
        for (int i = 0 ; i<eS; i++){
            int u = e[i][0];
            int v = e[i][1];
            mx = max(max(u,v),mx);
            dist[u][0]++;dist[u][1]++;
            dist[v][0]++;dist[v][1]++;
        }
        int cnt = 1;
        for (int i = 1; i<=mx; i++){
            if ((dist[i][0] == (mx-1)) && (dist[i][1] == (mx-1))) cnt = i;
        }
        return cnt;
    }
};