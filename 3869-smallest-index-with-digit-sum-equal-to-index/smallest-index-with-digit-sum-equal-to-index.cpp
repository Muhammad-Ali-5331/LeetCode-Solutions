#include <bits/stdc++.h>
using namespace std;

template <typename T>
void printUnorderedSet(const unordered_set<T>& s) {
    bool first = true;
    for (const auto& elem : s) {
        if (!first) cout << " ";
        cout << elem;
        first = false;
    }
    cout << '\n';
}

template <typename T>
void printVector(const vector<T>& vec) {
    for (size_t i = 0; i < vec.size(); ++i) {
        cout << vec[i] << (i + 1 < vec.size() ? " " : "");
    }
    cout << '\n';
}
class Solution {
public:
    int digS(int N){
        int res = 0;
        while(N > 0){
            res += N % 10;
            N /= 10;
        }
        return res;
    }
    int smallestIndex(vector<int>& nums) {
        int n = nums.size();
        int found = 0;
        int minInd = INT_MAX;
        for (int i = 0; i < n; i++) {
            if (digS(nums[i]) == i) {
                found++;
                minInd = min(minInd, i);
            }
        }
        return found > 0 ? minInd : -1;
    }
};