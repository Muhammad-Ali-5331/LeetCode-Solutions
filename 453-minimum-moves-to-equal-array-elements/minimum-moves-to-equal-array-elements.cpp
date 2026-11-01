class Solution {
public:
    int minMoves(vector<int>& nums) {
        int mi = nums[0];
        for (int val: nums){mi = min(val,mi);}
        int ops= 0;
        for (int val: nums){ops+=val-mi;}
        return ops;
    }
};