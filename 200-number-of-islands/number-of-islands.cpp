class Solution {
public:
    vector<vector<int>> dirs = {{1,0},{-1,0},{0,1},{0,-1}};
    void dfs(int i ,int j, vector<vector<char>>& grid){
        grid[i][j] = '0';
        for (int t = 0; t<4; t++){
            int x = i + dirs[t][0];
            int y = j + dirs[t][1];
            if (x>=0 && x<grid.size() && y>=0 && y<grid[0].size()){
                if (grid[x][y] == '1'){ dfs(x,y,grid); }
            }
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for (int row = 0; row<grid.size(); row++){
            for (int col = 0; col<grid[0].size(); col++){
                if (grid[row][col] == '1'){
                    count++;
                    dfs(row,col,grid);
                }
            }
        }
        return count;
    }
};