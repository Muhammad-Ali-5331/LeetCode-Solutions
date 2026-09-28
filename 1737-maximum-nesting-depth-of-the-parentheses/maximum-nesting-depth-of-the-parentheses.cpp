class Solution {
public:
    int maxDepth(string s) {
        int mx = 0;
        stack<int> st;
        for (char ch: s){
            if (ch == '('){
                int top = st.empty() ? 0 : st.top();
                st.push(top+1);
            }
            if (ch == ')'){mx = max(mx,st.top()); st.pop();}
        }
        return mx;
    }
};