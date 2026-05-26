class Solution {
public:
    int numberOfSpecialChars(string word) {
        unordered_set<char> seen(word.begin(),word.end());
        int count = 0;
        for (char c: seen){
            if (seen.contains(c-32)) count++;
        }
        return count;
    }
};