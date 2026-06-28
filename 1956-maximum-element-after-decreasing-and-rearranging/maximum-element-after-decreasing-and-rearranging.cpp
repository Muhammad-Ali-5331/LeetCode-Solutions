class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        sort(arr.begin(),arr.end());
        arr[0] = arr[0] == 1 ? arr[0] : 1;
        for(int i =1; i<arr.size();i++){
            arr[i] = arr[i]-arr[i-1]<=1 ? arr[i] : arr[i-1]+1;
        }
        int mx = 0;for(int& n: arr){mx = max(mx,n);}
        return mx;
    }
};