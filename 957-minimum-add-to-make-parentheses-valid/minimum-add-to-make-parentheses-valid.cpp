class Solution {
public:
    int minAddToMakeValid(string s) {
        int moves = 0;
        stack<char> stk;
        for (char ch:s){
            if (ch == '('){stk.push('(');}
            else{
                while (!stk.empty() && stk.top()!= '('){stk.pop();}
                if (!stk.empty()) stk.pop();
                else moves++;
            }
        }
        moves+=stk.size();
        return moves;
    }
};