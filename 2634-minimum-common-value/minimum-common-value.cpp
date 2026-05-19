class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> seen(nums2.begin(),nums2.end());
        sort(nums1.begin(),nums1.end());
        for (int &x: nums1){if (seen.find(x)!=seen.end()) return x;}
        return -1;
    }
};