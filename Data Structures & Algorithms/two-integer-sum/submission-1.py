class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hash_map:
                answer = [hash_map[target - nums[i]], i]

            else:
                hash_map[nums[i]] = i
        #make sure you handle edge cases
        return answer