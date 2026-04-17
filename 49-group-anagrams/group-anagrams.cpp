class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> anagrams;
        anagrams.reserve(strs.size());
        for (const auto& str : strs){
            string sortedStr = str;
            sort(sortedStr.begin(),sortedStr.end());
            anagrams[sortedStr].push_back(str);
        }
        vector<vector<string>> res;
        res.reserve(anagrams.size());
        for (auto &pair : anagrams){
            res.push_back(move(pair.second));
        }
        return res;
    }
};