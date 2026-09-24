#include <bits/stdc++.h>
using namespace std;

template <typename T>
void printUnorderedSet(const unordered_set<T>& s) {
    bool first = true;
    for (const auto& elem : s) {
        if (!first) cout << " ";
        cout << elem;
        first = false;
    }
    cout << '\n';
}

template <typename T>
void printVector(const vector<T>& vec) {
    for (size_t i = 0; i < vec.size(); ++i) {
        cout << vec[i] << (i + 1 < vec.size() ? " " : "");
    }
    cout << '\n';
}

class Solution {
public:
    vector<vector<int>> dir = { {1,0}, {-1,0}, {0,1}, {0,-1}};
    int orangesRotting(vector<vector<int>>& grid) {
        int minT = 0;
        queue<tuple<int, int, int>> q; // (row, col, time)

        int rows = grid.size();
        int cols = grid[0].size();
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == 2) { q.push({r, c, 0}); }
            }
        }
        while (!q.empty()){
            tuple<int, int, int> top = q.front();q.pop();
            int row = get<0>(top);
            int col = get<1>(top);
            grid[row][col] = 2;
            int currT = get<2>(top);
            minT = max(minT,currT);
            for (int i = 0; i<4; i++){
                int x = row + dir[i][0];
                int y = col + dir[i][1];
                if (x>=0 && x<rows && y>=0 && y<cols && grid[x][y] == 1){
                    q.push({x,y,currT+1});
                    grid[x][y] = 2;
                }
            }

        }
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == 1) { return -1; }
            }
        } 
        return minT;
    }
};