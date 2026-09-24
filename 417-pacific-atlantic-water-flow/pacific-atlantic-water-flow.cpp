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
    vector<vector<int>> dirs = {{1,0},{-1,0},{0,1},{0,-1}};
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        vector<vector<int>> result;
        int n = heights.size();
        int m = heights[0].size();
        vector<vector<bool>> visitedPacific (n,vector<bool>(m,false));
        vector<vector<bool>> visitedAtlantic (n,vector<bool>(m,false));
        queue<tuple<int,int>> q;
        for (int c = 0; c<m; c++){
            visitedPacific[0][c] = true;
            q.push({0,c});
        }
        for (int r = 0; r<n; r++){
            visitedPacific[r][0] = true;
            q.push({r,0});
        }
        while (!q.empty()){
            tuple<int,int> top = q.front();q.pop();
            int row = get<0>(top);
            int col = get<1>(top);
            for (int i = 0; i<4; i++){
                int x = row + dirs[i][0];
                int y = col + dirs[i][1];
                if (x>=0 && x<n && y>=0 && y<m && !visitedPacific[x][y] && heights[x][y]>=heights[row][col]){
                    visitedPacific[x][y] = true;
                    q.push({x,y});
                }
            }
        }
        for (int c = 0; c<m; c++){
            visitedAtlantic[n-1][c] = true;
            q.push({n-1,c});
        }
        for (int r = 0; r<n; r++){
            visitedAtlantic[r][m-1] = true;
            q.push({r,m-1});
        }
        while (!q.empty()){
            tuple<int,int> top = q.front();q.pop();
            int row = get<0>(top);
            int col = get<1>(top);
            for (int i = 0; i<4; i++){
                int x = row + dirs[i][0];
                int y = col + dirs[i][1];
                if (x>=0 && x<n && y>=0 && y<m && !visitedAtlantic[x][y] && heights[x][y]>=heights[row][col]){
                    visitedAtlantic[x][y] = true;
                    q.push({x,y});
                }
            }
        }
        
        for (int row = 0; row<n; row++){
            for (int col = 0; col<m; col++){
                if (visitedPacific[row][col] && visitedAtlantic[row][col]) result.push_back({row,col});
            }
        }
        return result;
    }
};