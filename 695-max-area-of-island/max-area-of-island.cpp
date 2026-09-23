class Solution {
public:
    vector<vector<int>> d = {
        {1,0},
        {-1,0},
        {0,1},
        {0,-1}
    };
    int dfs(int r, int c, vector<vector<int>>& grid){
        int count = 1;
        grid[r][c] = 0;
        for (int i = 0; i<4; i++){
            int x = r + d[i][0];
            int y = c + d[i][1];
            if (x>=0 && x<grid.size() && y>=0 && y<grid[0].size() && grid[x][y] == 1){
                count += dfs(x,y,grid);
            }
        }
        return count;
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int mx = 0;
        for (int row = 0; row<grid.size(); row++){
            for (int col = 0; col<grid[0].size(); col++){
                if (grid[row][col]){
                    int res = dfs(row,col,grid);
                    if (res>mx){mx = res;}
                }
            }
        }
        return mx;
    }
};