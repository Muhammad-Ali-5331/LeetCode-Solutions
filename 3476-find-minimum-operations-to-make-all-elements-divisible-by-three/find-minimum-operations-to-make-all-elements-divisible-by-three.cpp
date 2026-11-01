class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int ops = 0;
        for (int val: nums){
            //if (val%3 == 0) continue;
            int q = val / 3;
            int hV = 3 * (q+1);
            int lV = 3 * q;
            ops += min(hV-val, val-lV);
        }
        return ops;
    }
};