class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n = nums.size();
        int half = n / 2;
        int md = 0;
        if (n%2 == 0){md = (nums[half] + nums[half-1])/2;}
        else {md = nums[half];}
        int moves = 0;
        for (int val: nums){
            if (val<md) moves += (md-val);
            else if (val>md) moves += (val-md);
        }
        return moves;
    }
};