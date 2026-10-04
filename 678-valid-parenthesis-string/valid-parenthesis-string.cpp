class Solution {
public:
    bool checkValidString(string s) {
        stack<int> stk;
        for (char ch: s){
            if (ch == '(' || ch == '*'){stk.push(ch);}
            else {
                int sC = 0;
                if (stk.empty()) return false;
                while (!stk.empty() && stk.top()!='('){
                    char top = stk.top(); stk.pop();
                    if (top == '*') sC++;
                }
                if (stk.empty() && sC == 0) return false;
                bool starUsed = true;
                if (!stk.empty() && stk.top() == '('){ stk.pop(); starUsed = false;}
                if (starUsed) sC--;
                for (int i = 0; i<sC; i++){stk.push('*');}
            }
        }
        int sC = 0;
        while (!stk.empty()){
            char top = stk.top();stk.pop();
            if (top == '*') sC++;
            else if (top == '('){
                if (sC) sC--;
                else return false;
            }
            else return false;
        }
        return true;
}
};