#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define fast_io ios_base::sync_with_stdio(false); cin.tie(NULL); cout.precision(10);

// The macro to mimic print(*arr)
#define print_v(v) for(auto _i=0; _i<v.size(); ++_i) std::cout << v[_i] << (_i==v.size()-1 ? "" : " "); std::cout << endl;

class Solution {
public:
    ll INF = 1e18;
    int shortestPath(int n, vector<vector<int>>& edges, string labels, int k) {
    vector<vector<tuple<int, int, char>>> adj(n);
    for (auto& e : edges) {
        int u = e[0], v = e[1], w = e[2];
        adj[u].emplace_back(v, w, labels[v]);
    }
    vector<vector<ll>> dist(n, vector<ll>(k+1, INF ));
    dist[0][1] = 0;
    vector<char> label(n); for(int i=0; i<n; ++i) label[i] = labels[i];
    priority_queue<tuple<ll, int, int>, vector<tuple<ll, int, int>>, greater<tuple<ll, int, int>>> pq;
    pq.push({0, 1, 0}); // distance, count of same labels, node
    while (!pq.empty())
    {
    auto [d, cnt, u] = pq.top(); pq.pop();
    if (d > dist[u][cnt]) continue;
    for (auto [neigh,weight,nL]: adj[u]){
        int newKCount = labels[u] == nL ? cnt+1 : 1;
        if (newKCount>k) continue;
        ll newW = d + weight;
        if (newW<dist[neigh][newKCount]){
            dist[neigh][newKCount] = newW;
            pq.push({newW,newKCount,neigh});
        }
    }
    }
    ll ans = INF;
    for (int i=0; i<=k; ++i) ans = min(ans, dist[n-1][i]);
    return ans == INF ? -1 : ans;
}
};