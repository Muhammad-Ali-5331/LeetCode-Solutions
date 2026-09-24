class Solution {
public:
    vector<vector<int>> dir = { {1,0}, {-1,0}, {0,1}, {0,-1}};
    void dfs(int row, int col, vector<vector<char>>& grid,vector<vector<bool>> &visited){
        visited[row][col] = true;
        for (int i =0; i<4; i++){
            int x = row + dir[i][0];
            int y = col + dir[i][1];
            if (x>=0 and x<grid.size() and y>=0 and y<grid[0].size() and grid[x][y] == 'O' and !visited[x][y]){ dfs(x,y,grid,visited); }
        }
    }
    void solve(vector<vector<char>>& grid) {
        int ROWS= grid.size();
        int COLS= grid[0].size();
        vector<vector<bool>> visited (ROWS,vector<bool>(COLS,false));


        for (int col = 0; col<COLS; col++){
           if (grid[0][col] == 'O'){ dfs(0,col,grid,visited); }
        }
        for (int col = 0; col<COLS; col++){
           if (grid[ROWS-1][col] == 'O'){ dfs(ROWS-1,col,grid,visited); }
        }
        for (int row = 0; row<ROWS; row++){
           if (grid[row][0] == 'O'){ dfs(row,0,grid,visited); }
        }
        for (int row = 0; row<ROWS; row++){
           if (grid[row][COLS-1] == 'O'){ dfs(row,COLS-1,grid,visited); }
        }


        for (int row = 1; row<ROWS-1; row++){
            for (int col = 1; col<COLS-1; col++){
                if(grid[row][col] == 'O' && !visited[row][col]) grid[row][col] = 'X';
            }
        }
    }
};