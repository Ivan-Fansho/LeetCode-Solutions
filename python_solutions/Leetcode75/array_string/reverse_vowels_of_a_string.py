class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        st="aeiouAEIOU"
        b=0
        e=len(s)-1
        while(b<e):
            while b<e and s[b] not in st:
                b=b+1
                continue
            while b<e and s[e] not in st:
                e=e-1
                continue
            s[b],s[e]=s[e],s[b]
            b=b+1
            e=e-1
        s=''.join(s)
        return s

print(Solution().reverseVowels("aeiouAEIOU"))