#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int precedence(char& op) {
        if (op == '^')
            return 3;
        if (op == '*' || op == '/')
            return 2;
        if (op == '+' || op == '-')
            return 1;
        return 0;
    }

    string infixToPostFix(string& expr) {
        string result = "";
        stack<char> STACK;

        for (int i = 0; i < expr.size(); i++) {
            char c = expr[i];
            if (c == ' ')
                continue;
            if (isdigit(c)) {
                while (i < expr.size() and isdigit(expr[i])) {
                    result += expr[i];
                    i++;
                }
                result += ' ';
                i--;
            } else if (c == '(') {
                STACK.push(c);
            } else if (c == ')') {
                while (!STACK.empty() && STACK.top() != '(') {
                    result += STACK.top();
                    result += ' ';
                    STACK.pop();
                }
                STACK.pop();
            } else {
                int j = i - 1;
                while (j >= 0 && expr[j] == ' ')
                    j--;

                // 🔥 Detect unary minus
                if (c == '-' && (j < 0 || expr[j] == '(' ||
                                 (!isdigit(expr[j]) && expr[j] != ')'))) {
                    result += "0 ";
                }

                while (!STACK.empty() && STACK.top() != '(' &&
                       precedence(STACK.top()) >= precedence(c)) {
                    result += STACK.top();
                    result += ' ';
                    STACK.pop();
                }
                STACK.push(c);
            }
        }

        while (!STACK.empty()) {
            result += STACK.top();
            result += ' ';
            STACK.pop();
        }

        return result;
    }

    int calculate(string s) {
        stack<long long> st;
        string postFix = infixToPostFix(s);
        string token;
        stringstream ss(postFix);
        while (ss >> token) {
            if (isdigit(token[0])) {
                st.push(stoll(token));
            } else {
                long long b = st.top();
                st.pop();
                long long a = st.top();
                st.pop();
                if (token == "+")
                    st.push(a + b);
                else if (token == "-")
                    st.push(a - b);
                else if (token == "*")
                    st.push(a * b);
                else if (token == "/")
                    st.push(a / b);
                else if (token == "^")
                    st.push(pow(a, b));
            }
        }
        return st.top();
    }
};