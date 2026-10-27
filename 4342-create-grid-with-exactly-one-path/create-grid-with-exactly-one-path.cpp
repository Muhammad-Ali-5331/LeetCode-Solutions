#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    void dfs(int x, int y, vector<vector<string>>& grid) {
        grid[x][y] = ".";
        if (x+1<grid.size()) dfs(x+1,y,grid); // Move Down
        else if (y+1<grid[0].size()) dfs(x,y+1,grid); // Move Right
    }
    vector<string> createGrid(int m, int n) {
        vector<vector<string>> grid(m,vector<string>(n,"#"));
        dfs(0,0,grid);
        vector<string> result;
        for (int i=0; i<m; i++) {
            string row = "";
            for (int j=0; j<n; j++) {
                row += grid[i][j];
            }
            result.push_back(row);
        }
        return result;
    }
};