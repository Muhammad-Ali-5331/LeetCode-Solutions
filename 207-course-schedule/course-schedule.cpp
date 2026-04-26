#include <bits/stdc++.h>
using namespace std;
void dfs(int node,vector<bool>&visited,stack<int>& st,unordered_map<int,vector<int>>& adjList) {
    visited[node] = true;
    for (auto &n: adjList[node]) {
        if (!visited[n]){dfs(n,visited,st,adjList);}
    }
    st.push(node);
}
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& connections) {
        unordered_map<int,vector<int>> adjList;
        for (auto node:connections) { adjList[node[1]].push_back(node[0]); }
        vector<int> res;
        vector<bool> visited(numCourses,false);
        stack<int> st;
        for (int i = 0; i<numCourses;i++) { if (!visited[i]){dfs(i,visited,st,adjList);} }
        while (!st.empty()){res.push_back(st.top());st.pop();}
        unordered_map<int,int> MAP;
        for (int i = 0;i<res.size();i++) { MAP[res[i]] = i; }
        for (auto node:connections) {
            int uInd = MAP[node[1]];
            int vInd = MAP[node[0]];
            if (uInd>=vInd) return false;
        }
        return true;
    }
};