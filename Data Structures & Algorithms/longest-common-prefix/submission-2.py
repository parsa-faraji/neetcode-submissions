class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0

        prefix = strs[0]

        while i < len(prefix):
            for s in strs:
                if i == len(s) or s[i] != prefix[i]:
                    return prefix[:i]
            i += 1
        return prefix[:i]

                