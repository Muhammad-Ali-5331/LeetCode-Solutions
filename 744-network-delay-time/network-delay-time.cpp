#include <bits/stdc++.h>
using namespace std;
struct Edge {
    int weight,nodeVal;
    bool operator>(const Edge& other) const{return weight>other.weight;}
};
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        int cost = 0;
        unordered_set<int> visited;
        unordered_map<int,vector<Edge>> adj;
        for (int i = 0; i< times.size();i++){
            adj[times[i][0]].push_back({times[i][2],times[i][1]});
        }
        cout << endl;
        priority_queue<Edge,vector<Edge>,greater<Edge>> minHeap;
        visited.insert(k);
        for (auto [W,N]: adj[k]){ minHeap.push({W,N});}
        while (!minHeap.empty()) {
            Edge curr = minHeap.top();minHeap.pop();
            if (visited.contains(curr.nodeVal)) continue;
            visited.insert(curr.nodeVal);
            cost = max(cost,curr.weight);
            for (auto [WE,NE]:adj[curr.nodeVal]) {
                if (!visited.contains(NE)){minHeap.push({curr.weight+WE,NE});}
            }
        }
        return visited.size() == n ? cost : -1;
    }
};