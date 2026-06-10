class Solution {
public:
    int trailingZeroes(int n) {
        int c= 0;
        int p = 1;
        int res = 5;
        while (res<=n){
            c += n/res;
            res*=5;
        }
        return c;
    }
};