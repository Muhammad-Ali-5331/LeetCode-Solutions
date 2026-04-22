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
    int ROWS = 0,COLS = 0;
    bool isValid(int r, int c){return r>=0 and c>=0 and r<ROWS and c<COLS;}
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        ROWS = heights.size();
        COLS = heights[0].size();
        vector<vector<int>> res;

        // Explore Pacific Ocean Points
        map<pair<int,int>,int> MAP1;
        queue<pair<int,int>> q;
        for (int row = 1; row < ROWS ; row++) {q.push({row,0});MAP1[{row,0}] = 1;}
        for (int col = 0; col < COLS; col++){q.push({0,col});MAP1[{0,col}] = 1;}
        while (!q.empty()) {
            auto curr = q.front();q.pop();
            int currX = curr.first,currY = curr.second;
            int currHeight = heights[currX][currY];
            MAP1[{currX,currY}] = 1;
            for (auto dir: dirs) {
                int newX = curr.first+dir.first,newY = curr.second+dir.second;
                if (!isValid(newX,newY)) continue;
                if (MAP1.contains({newX,newY})) continue;
                if (heights[newX][newY]>=currHeight){q.push({newX,newY});}
            }

        }
        // Explore Atlantic Ocean points
        map<pair<int,int>,int> MAP2;
        for (int row = 0 ; row < ROWS-1 ; row++) {q.push({row,COLS-1});MAP2[{row,COLS-1}] = 1;}
        for (int col = 0; col < COLS; col++){q.push({ROWS-1,col});MAP2[{ROWS-1,col}] = 1;}
        while (!q.empty()) {
            auto curr = q.front();q.pop();
            int currX = curr.first,currY = curr.second;
            int currHeight = heights[currX][currY];
            MAP2[{currX,currY}] = 1;
            for (auto dir: dirs) {
                int newX = curr.first+dir.first,newY = curr.second+dir.second;
                if (!isValid(newX,newY)) continue;
                if (MAP2.contains({newX,newY})) continue;
                if (heights[newX][newY]>=currHeight){q.push({newX,newY});}
            }

        }
        for (auto [key,val]:MAP1) {
            if (MAP2.contains(key)){res.push_back({key.first,key.second});}
        }
        return res;

    }
};