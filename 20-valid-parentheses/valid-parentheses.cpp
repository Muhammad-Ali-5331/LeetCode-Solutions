class Solution {
public:
    bool isValid(string const &s) {
        stack <char> STACK;
        unordered_map<char,char> map = {{'}','{'}, {']','['}, {')','('}};
        for (auto c : s) {
            if (map.contains(c)) {
                if (STACK.empty()) { return false; }
                char opening = map[c];
                char top = STACK.top();
                STACK.pop();
                if (opening != top) { return false; }
            }
            else {STACK.push(c); }
        }
        return STACK.empty();
    }
};