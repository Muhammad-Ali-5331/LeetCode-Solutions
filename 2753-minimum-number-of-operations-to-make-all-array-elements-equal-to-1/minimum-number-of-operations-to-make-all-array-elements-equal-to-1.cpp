#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        int countOnes = 0;
        for (int x : nums) {
            if (x == 1) countOnes++;
        }
        
        // If there are already 1s in the array, convert each remaining non-1 in 1 step
        if (countOnes > 0) {
            return n - countOnes;
        }
        int mS = INT_MAX;
        for (int i = 0; i<n; i++){
            vector<int> temp;
            for (int j = i; j<n; j++){
                temp.push_back(nums[j]);
                if (temp.size() > 1){
                    int g = temp[0];
                    for (int k = 1; k<temp.size(); k++){ g = gcd(g, temp[k]); }
                    if (g == 1){
                        mS = min(mS, j-i+1);
                        break;
                    }
                }
            }
        }
        if (mS == INT_MAX) return -1;
        return mS-1+n-1;
    }
};