class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int gD = INT_MAX;
        int ans = 0;
        for(int &n: nums){
            int dist = n<=0 ? abs(n) : n;
            if (dist<=gD){
                gD = dist; 
                ans = n;
            }
        }
        return ans;
    }
};