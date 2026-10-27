#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<string> createGrid(int m, int n) {
        vector<vector<string>> grid(m,vector<string>(n,"#"));
        deque<tuple<int,int>> q; // X, Y, direction
        q.push_back({0,0});
        while (!q.empty()) {
            auto [x, y] = q.front(); q.pop_front();
            grid[x][y] = ".";
            if (x+1<m && grid[x+1][y]=="#") { q.push_back({x+1,y}); } // Move Down
            else if (y+1<n && grid[x][y+1]=="#") { q.push_back({x,y+1}); } // Move Right
        }
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