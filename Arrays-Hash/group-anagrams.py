class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = 'abcdefghijklmnopqrstuvwxyz'
        p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        d_map = dict(zip(a, p))
        
        a_dic = {}

        for word in strs: # loop through all words in the arrsy
            val = 1
            for char in word: # loop through all the characters in each word 
                val *= d_map[char] # find ascii numerical value and sum it up to find val

            if val in a_dic:
                a_dic[val].append(word)
            else:
                a_dic[val] = [word]

        result = []
        for keys in a_dic:
            result.append(a_dic[keys])
        
        return result
