class Solution {
public:
    int minimumCost(vector<int>& cost) {
        int n = cost.size();
        if (n == 1) return cost[0];
        else if (n==2) return cost[0]+cost[1];
        int res = 0;
        sort(cost.begin(),cost.end());
        reverse(cost.begin(),cost.end());
        int i = 0;
        while (i+1<n){
            res+=cost[i] + cost[i+1];
            i+=3;
        }
        int rem = n%3;
        if (rem == 1) res+=cost[n-1];
        return res;
    }
};