class Solution {
public:
    bool judgeCircle(string moves) {
        pair<int,int> st = {0,0};
        for (char &ch: moves){
            if (ch == 'U'){st.second-=1;}
            else if (ch == 'D'){st.second+=1;}
            else if (ch == 'L'){st.first-=1;}
            else {st.first+=1;}
        }
        return st.first == 0 && st.second == 0;
    }
};