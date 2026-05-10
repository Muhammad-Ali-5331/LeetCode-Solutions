#include <bits/stdc++.h>
using namespace std;
struct Node {
    int d,node;
    bool operator>(const Node& other) const {
        return d > other.d;
    }
};
class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int cost = 0;
        int N = points.size();
        unordered_map<int,vector<Node>> adj;
        for (int i = 0; i<N;i++) {
            int currX = points[i][0],currY = points[i][1];
            for (int j = i+1;j<N;j++) {
                int nextX = points[j][0],nextY = points[j][1];
                int dist = abs(currX-nextX) + abs(currY-nextY);
                adj[i].push_back({dist,j});
                adj[j].push_back({dist,i});
            }
        }
        priority_queue<Node,vector<Node>,greater<Node>> minHeap;
        unordered_map<int,bool> visit;
        visit[0] = true;
        for (auto [d,neigh]: adj[0]){minHeap.push({d,neigh});}
        while (!minHeap.empty()) {
            Node currN = minHeap.top();minHeap.pop();
            if (visit[currN.node]) continue;
            visit[currN.node] = true;
            cost+=currN.d;
            for (auto [D,ne]: adj[currN.node]) {
                if (visit[ne]!=true) { minHeap.push({D,ne}); }
            }
        }
        return cost;
    }
};