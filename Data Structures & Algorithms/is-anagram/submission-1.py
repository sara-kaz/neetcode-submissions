class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sort_s = "".join(sorted(s))
        sort_t = "".join(sorted(t))

        return sort_s == sort_t