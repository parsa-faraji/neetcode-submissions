from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded


    def decode(self, s: str) -> List[str]:
        """Decodes a single string back to a list of strings."""
        result = []
        i = 0
        while i < len(s):
            # find the delimiter '#'
            j = i
            while s[j] != '#':
                j += 1
            # length of the next string
            length = int(s[i:j])
            # move past the '#'
            start = j + 1
            # extract the string
            result.append(s[start:start + length])
            # move i to the start of the next length field
            i = start + length
        return result
