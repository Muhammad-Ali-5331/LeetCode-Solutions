class Solution {
public:
    void recF(int oB, int cB, string currS, vector<string> &res){
        if (oB == 0 && cB == 0){res.push_back(currS);}
        else {
            if (oB>=cB){
                recF(oB-1,cB,currS + "(",res);
                //if (cB-1>=0) recF(oB,cB-1,currS + ")",res);
            }
            else {
                recF(oB,cB-1,currS + ")",res);
                if (oB-1>=0) recF(oB-1,cB,currS + "(",res);
            }
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        recF(n,n,"",res);
        return res;
    }
};