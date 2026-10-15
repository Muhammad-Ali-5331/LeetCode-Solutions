class Solution {
public:
    int sumCounts(vector<int>& nums) {
        int sSquare = 0;
        int n = nums.size();
        for (int i = 0; i<n; i++){
            unordered_set<int> seen;
            for (int j = i; j<n; j++){
                seen.insert(nums[j]);
                int sz = seen.size();
                sSquare += sz*sz;
            }
        }
        return sSquare;
    }
};