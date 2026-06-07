class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        one = sorted(s)
        two = sorted(t)

        return one == two