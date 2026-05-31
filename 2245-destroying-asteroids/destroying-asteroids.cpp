#include <bits/stdc++.h>
using namespace std;
class Solution {
    struct Edge {
        int weight,val;
        bool operator>(const Edge &o)const{return weight>o.weight;}
    };
public:
    bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
        sort(asteroids.begin(),asteroids.end());
        // priority_queue<Edge,vector<Edge>,greater<Edge>> mxHeap;
        // for (int &val: asteroids){mxHeap.push({abs(mass-val),val});}
        long long currMass = mass;
        for (int &weight: asteroids) {
            if (currMass<weight) return false;
            currMass+=weight;
        }
        // while (!mxHeap.empty()) {
        //     if (currMass<mxHeap.top().val) return false;
        //     currMass+=mxHeap.top().val;
        //     mxHeap.pop();
        // }
        return true;
    }
};
