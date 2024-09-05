class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""

        if len(word1) > len(word2):
            for i in range(len(word2)):
                merged += word1[i] + word2[i]
            merged += word1[len(word2):]
            return merged
        elif len(word1) < len(word2):
            for i in range(len(word1)):
                merged += word1[i] + word2[i]
            merged += word2[len(word1):]
            return merged
        else:
            for i in range(len(word1)):
                merged += word1[i] + word2[i]
            return merged


word1 = "abcd"
word2 = "pq"

print(Solution().mergeAlternately(word1, word2))