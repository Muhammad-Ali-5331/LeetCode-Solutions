class Solution {
public:
    int trailingZeroes(int n) {
        int c= 0;
        int p = 1;
        int res = (int) pow(5,p);
        while (res<=n){
            c += n/res;
            p++;
            res = (int) pow(5,p);
        }
        return c;
    }
};