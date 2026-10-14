class Solution {
public:
    string maxSumOfSquares(int num, int sum) {
        string res;
        for (int i = 1; i<=num; i++){
            if (sum<=0){res += "0";}
            else{
                for (int j = 9; j>=0; j--){
                    if (sum-j>=0){
                        sum-=j;
                        res += to_string(j);
                        break;
                    }
                }
            }
        }
        return sum == 0 ? res : "";
    }
};