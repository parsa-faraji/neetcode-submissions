class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
       hash_set = {}
       for i, num in enumerate(numbers):
            if (target - num) in hash_set:
                return [min(i, hash_set[target - num])+1,
                max(i, hash_set[target - num])+1]
            hash_set[num] = i
        

                
