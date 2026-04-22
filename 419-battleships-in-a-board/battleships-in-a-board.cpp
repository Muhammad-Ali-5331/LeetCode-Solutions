#include <bits/stdc++.h>
using namespace std;
vector<pair<int,int>> dirs = {
    {1,0},
    {-1,0},
    {0,1},
    {0,-1}
};
class Solution {
public:
    int ROWS = 0;
    int COLS = 0;
    bool Valid(int r, int c){return r>=0 and c>=0 and r<ROWS and c<COLS;}
    void dfs(int i,int j,vector<vector<char>>& board) {
        board[i][j] = '.';
        for (auto &dir: dirs) {
            int newX = i+dir.first,newY = j+dir.second;
            if (!Valid(newX,newY)) continue;
            if (board[newX][newY] == '.') continue;
            dfs(newX,newY,board);
        }
    }
    int countBattleships(vector<vector<char>>& board) {
        int count = 0;
        ROWS = board.size();
        COLS = board[0].size();
        for (int row = 0; row<ROWS; row++) {
            for (int col = 0; col < COLS;col++) {
                if (board[row][col] == 'X') {
                    count++;
                    dfs(row,col,board);
                }
            }
        }
        return count;
    }
};