class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        unordered_map<int,int> MAP;
        int mx = 1;
        int n = nums.size();
        nums.insert(nums.begin(),0);
        int l = 1,r = 1;
        while (r<=n){
            MAP[nums[r]]++;
            while (MAP[nums[r]]>k){
                MAP[nums[l++]]--;
            }
            mx = max(mx,r-l+1);
            r++;
        }
        return mx;
    }
};