class Solution {
public:
    bool isPalindrome(int x) {
        long long tempX = x;
        tempX = abs(tempX);
        long long res = 0;
        while (tempX>0){
            int digit = tempX%10;
            res = res*10 + digit;
            tempX/=10;
        }
        return res == x;
    }
};