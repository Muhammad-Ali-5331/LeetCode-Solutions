class Solution {
public:
    bool isPalindrome(int x) {
        if (x >=0 and x <=9)
            return true;
        if (x < 0){
            return false;
        }
        long long temp = x;
        long long n = 0;
        while (temp){
            n = n*10 + (temp % 10);
            temp = (int) temp/10;
        }
        return n == x;
    }
};