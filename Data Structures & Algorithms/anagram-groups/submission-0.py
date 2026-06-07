class Solution:

    from collections import defaultdict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        op = defaultdict(list)

        for string in strs:
            check = str(sorted(string))
            op[check].append(string)

        return list(op.values())