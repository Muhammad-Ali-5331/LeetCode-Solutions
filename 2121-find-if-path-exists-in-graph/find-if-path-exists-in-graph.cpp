class Solution {
public:
    vector<bool> vt;
    bool dfs (int node, int &target, vector<vector<int>>& adj){
        if (node == target) return true;
        for (int ne: adj[node]){
            if (!vt[ne]){
                vt[ne] = true;
                if (dfs(ne,target,adj)) return true;
            }
        }
        return false;
    }
    bool validPath(int n, vector<vector<int>>& e, int s, int d){
        vector<vector<int>> adj(n+1);
        for (int i = 0; i<e.size(); i++){
            int u = e[i][0];
            int v = e[i][1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        vt.assign(n,false);
        vt[s] = true;
        return dfs(s,d,adj);
    }
};