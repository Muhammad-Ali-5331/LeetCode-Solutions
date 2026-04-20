class Solution {
public:
    int sumOfGoodNumbers(vector<int>& nums, int k) {
        int ans = 0;
        int n = nums.size();
        for (int i = 0; i< n; i++){
            int le = i-k>=0 ? nums[i-k] : 0;
            int re = i+k>=n ? 0 : nums[i+k];
            if (nums[i]>le && nums[i]>re){ans+=nums[i];}
        }
        return ans;
    }
};