#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int ROWS,COLS;
    struct Node {
        int x,y,H;
        bool operator<(const Node &other) const {return H<other.H;};
    };
    bool isValid(int &r, int &c) {return r>=0 and r<ROWS and c>=0 and c<COLS;}
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        priority_queue<Node> q;
        int dirsX[4] = {1,-1,0,0};
        int dirsY[4] = {0,0,1,-1};
        ROWS = grid.size(), COLS = grid[0].size();
        vector<vector<bool>> visited (ROWS+1,vector<bool>(COLS,false));
        q.push({0,0,grid[0][0] == 1 ? health-1 : health});
        while (!q.empty()) {
            Node curr = q.top();q.pop();
            if (curr.H<1) continue;
            if (visited[curr.x][curr.y]) continue;
            visited[curr.x][curr.y] = true;
            if (curr.x == ROWS-1 && curr.y == COLS-1) return true;
            for (int i = 0; i<4;i++) {
                int newX = curr.x + dirsX[i], newY = curr.y+ dirsY[i];
                if (!isValid(newX,newY)) continue;
                if (visited[newX][newY]) continue;
                q.push({newX,newY, grid[newX][newY] == 1 ? curr.H-1: curr.H});
            }
        }
        return false;
    }
};