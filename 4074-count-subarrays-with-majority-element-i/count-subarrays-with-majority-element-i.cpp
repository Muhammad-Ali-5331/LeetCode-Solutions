class Solution {
public:
    int countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size();
        int count = 0;
        for (int i =0; i<n;i++){
            unordered_map<int,int> MAP;
            for (int j=i;j<n;j++){
                MAP[nums[j]]++;
                int currL = (j-i+1)/2;
                if (MAP[target]>currL) count++;
            }
        }
        return count;
    }
};