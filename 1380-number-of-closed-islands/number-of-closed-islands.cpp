#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int ROWS,COLS = 0;
    vector<pair<int,int>> dirs = {
        {1,0},
        {-1,0},
        {0,1},
        {0,-1}
    };
    bool dfs(int x, int y, vector<vector<int>>& grid, vector<vector<bool>> &visited){
        if (grid[x][y]) return true;
        visited[x][y] = true;
        vector<bool> allD(4,false);
        for (int i = 0; i<4; i++){
            auto [r, c] = dirs[i];
            int nX = x + r;
            int nY = y + c;
            if (nX<0 || nX>=ROWS || nY<0 || nY>=COLS) continue;
            if (visited[nX][nY]) allD[i] = true;
            else allD[i] = dfs(nX,nY,grid,visited);
        }
        return allD[0] && allD[1] && allD[2] && allD[3];
    }
    int closedIsland(vector<vector<int>>& grid) {
        int count = 0;
        ROWS = grid.size();
        COLS = grid[0].size();
        vector<vector<bool>> visited (ROWS+1, vector<bool>(COLS+1,false));
        for (int r = 0; r<ROWS; r++){
            for (int c = 0; c<COLS; c++){
                if (visited[r][c]) continue;
                if (grid[r][c]) continue;
                if (dfs(r,c,grid,visited)) count++ ;
            }
        }
        return count;
    }
};