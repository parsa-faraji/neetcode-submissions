class Solution:
    def hammingWeight(self, n: int) -> int:
        # turn the number into binary, then string, then count number of 1s

        # converts number into binary string starting with 0b
        binary = bin(n)


        ans = 0
        for ch in binary[2:]:
            if ch == "1":
                ans += 1

        return ans
