class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [1, 3, 0, 0, 4, 2]
        # index 2.   index 3. + replace each with _. + count num equal
        # 0 put at the last - switch the last with that index if last != target
        i = len(nums) - 1
        count = 0
        for j in range(len(nums)):
            if j > i:
                break
            if nums[j] == val:
                count += 1
                nums[j] = "_"
                while nums[i] == val and i > 0:
                    count += 1
                    nums[i] = "_"
                    i -= 1 

                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i -= 1

        print(nums)
        return (len(nums) - count)
            
                



