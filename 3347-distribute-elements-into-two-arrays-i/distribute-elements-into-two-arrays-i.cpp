class Solution {
public:
    vector<int> resultArray(vector<int>& nums) {
        vector<int> arr1 = {nums[0]};
        vector<int> arr2 = {nums[1]};
        int l1 = nums[0], l2 = nums[1];
        int i = 2;
        while (i<nums.size()){
            if (l1>l2){l1 = nums[i]; arr1.push_back(nums[i++]);}
            else {l2 = nums[i]; arr2.push_back(nums[i++]);}
        }
        arr1.insert(arr1.end(),arr2.begin(),arr2.end());
        return arr1;
    }
};