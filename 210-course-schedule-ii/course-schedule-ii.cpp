#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    void dfs(int node,vector<bool>&visited,stack<int>& st,unordered_map<int,vector<int>>& adjList) {
        visited[node] = true;
        for (auto &n: adjList[node]) {
            if (!visited[n]){dfs(n,visited,st,adjList);}
        }
        st.push(node);
    }

   vector<int> findOrder(int numCourses, vector<vector<int>>& connections) {
        unordered_map<int,vector<int>> adjList;
        for (auto node:connections) {

            // As node[1] is pre-req of node[0] so there is a directed edge from node[1] --> node[0]

            adjList[node[1]].push_back(node[0]);
        }
        vector<int> res;
        vector<bool> visited(numCourses,false);
        stack<int> st;
        for (int i = 0; i<numCourses;i++) { if (!visited[i]){dfs(i,visited,st,adjList);} }
        while (!st.empty()){res.push_back(st.top());st.pop();}
        unordered_map<int,int> MAP;
        bool possible = true;
        for (int i = 0;i<res.size();i++) { MAP[res[i]] = i; }
        for (auto node:connections) {
            // Every Dependent {v} here node[0] should appear after the pre-req {u} here node[1]

            // Here there is an edge btw u --> v so every u should appear before v
            int uInd = MAP[node[1]];
            int vInd = MAP[node[0]];
            if (uInd>=vInd) {
                possible = false;
                break;
            }
        }
        if (possible){return res;}
        else {return {};}
    }
};