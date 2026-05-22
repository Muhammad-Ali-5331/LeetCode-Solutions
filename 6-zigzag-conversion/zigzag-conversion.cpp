#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    string convert(string s, int numRows) {
        string res;
        int matrixCols = s.size()*2;
        vector<vector<char>> matrix (numRows,vector<char>(matrixCols,'!'));
        int colNo = 0;
        int stringPointer = 0;
        int n = s.size();
        while (stringPointer<n and colNo<matrixCols) {
            int r = 0;
            while (stringPointer<n and r<numRows) { matrix[r++][colNo] = s[stringPointer++]; }
            r = numRows-2;
            int col = colNo+1;
            while (stringPointer<n and r>0) {
                matrix[r--][col++] = s[stringPointer++];
            }
            colNo = col;
        }
        for (int i = 0; i<numRows;i++) {
            for (int j = 0; j<matrixCols;j++) {
                if (matrix[i][j] == '!') continue;
                res+=matrix[i][j];
            }
        }
        // for (auto& row: matrix) {
        //     for (auto &elem: row){cout << elem << " ";}
        //     cout<<endl;
        // }
        return res;
    }
};