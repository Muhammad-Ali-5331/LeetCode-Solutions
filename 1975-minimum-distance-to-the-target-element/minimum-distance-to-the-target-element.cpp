class Solution {
public:
    int getMinDistance(vector<int>& nums, int target, int start) {
        int minD = INT_MAX;
        for (int i = 0; i<nums.size(); i++){
            if (nums[i] == target) minD = min(minD,abs(start-i));
        }
        return minD;
    }
};