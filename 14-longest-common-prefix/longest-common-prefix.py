class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 1:
            return strs[0]
        common_prefix = ""
        first_word = strs[0]
        remaining_words = strs[1:]
        length_of_rems = len(remaining_words)
        while True:
            count = 0
            if first_word:
                current_checking = first_word[0]
                len_of_current_checking = len(current_checking)
                for word in remaining_words:
                    if len(word) < len_of_current_checking:
                        break
                    if word.startswith(current_checking):
                        count+=1
                if count == length_of_rems:
                    common_prefix=current_checking
                if not common_prefix: 
                    break
                else:
                    for i in range(2,len(first_word)+1):
                        count = 0
                        current_checking = first_word[:i]
                        len_of_current_checking = len(current_checking)
                        for word in remaining_words:
                            if len(word) < len_of_current_checking:
                                break
                            if word.startswith(current_checking):
                                count+=1
                        if count == length_of_rems:
                            common_prefix=current_checking
                    break
            else:
                break
        return common_prefix