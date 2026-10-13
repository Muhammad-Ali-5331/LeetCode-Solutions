class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i<n; i++){nums[i] = abs(nums[i]);}
        long long res = 0;
        sort(nums.begin(),nums.end());
        int l = 0,r = n-1;
        while (l<r){
            long long rightR = nums[r]*nums[r]; r--;
            long long leftR = nums[l]*nums[l]; l++;
            res += rightR - leftR ;
        }
        if (n%2!=0){res += nums[r]*nums[r];}
        return res;
    }
};