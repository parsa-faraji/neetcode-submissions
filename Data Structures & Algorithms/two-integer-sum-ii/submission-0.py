class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # input : sorted list
        # output: list of 1-indexed nums

        l, r = 0, len(numbers)-1

        while r > l:
            if numbers[l] + numbers[r] == target:
                return [l+1 ,r+1]
            if (numbers[l] + numbers[r]) > target:
                r -= 1
            if (numbers[l] + numbers[r]) < target:
                l += 1

            
