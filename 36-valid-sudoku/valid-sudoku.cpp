class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i = 0; i< 9; i++){
            unordered_set<char> seen;
            for(int j = 0; j < 9; j++){
                char curr = board[i][j];
                if (seen.contains(curr)){
                    return false;
                }
                else if (curr != '.'){
                    seen.insert(curr);
                }
            }
        }
        for (int i = 0; i< 9; i++){
            unordered_set<char> seen;
            for(int j = 0; j < 9; j++){
                char curr = board[j][i];
                if (seen.contains(curr)){
                    return false;
                }
                else if (curr != '.'){
                    seen.insert(curr);
                }
            }
        }
        int startRow = 0;
        while (startRow < 9){
            int currentGridStartIndex = 0;
            while (currentGridStartIndex < 9){
                unordered_set<char> seen;
                for (int i = startRow; i< startRow+3; i++){
                    for(int j = currentGridStartIndex; j < currentGridStartIndex+3; j++){
                        char curr = board[i][j];
                        if (seen.contains(curr)){
                            return false;
                        }
                        else if (curr != '.'){
                            seen.insert(curr);
                        }
                    }
                }
                currentGridStartIndex+=3;
            }
            startRow+=3;
        }
        return true;
    }
};