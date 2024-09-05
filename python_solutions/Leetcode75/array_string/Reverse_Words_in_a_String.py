class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


print(Solution().reverseWords("a good   example"))