class Solution {
public:
    int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
        int cnt = 0;
        for (int val: arr1){
            bool nY = true;
            for (int val2: arr2){
                int diff = abs(val-val2);
                if (diff<=d){
                    nY = false;
                    break;
                }
            }
            cnt += nY;
        }
        return cnt;
    }
};