class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefix(n,0),suffix(n,0),res(n,0);
        prefix[0] = nums[0];
        suffix[n-1] = nums[n-1];
        for (int i = 1; i<n; i++){prefix[i] = nums[i]+prefix[i-1];}
        for (int i = n-2; i>=0; i--){suffix[i] = nums[i]+suffix[i+1];}
        for (int i = 0; i<n; i++){
            int leftS = i-1>=0 ? prefix[i-1] : 0;
            int rightS = i+1<n ? suffix[i+1] : 0;
            res[i] = abs(leftS - rightS);
        }
        return res;
    }
};