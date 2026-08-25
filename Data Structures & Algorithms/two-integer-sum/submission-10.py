class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_to_indicies = {}
        x = 0
        y = 0

        for i in range(len(nums)):
            if nums[i] not in nums_to_indicies:
                nums_to_indicies[nums[i]] = [i]
            else:
                nums_to_indicies[nums[i]].append(i)
        
        for n in nums:
            difference = target - n
            if difference in nums_to_indicies:
                
                if n != difference:
                    return [nums_to_indicies[n][0], nums_to_indicies[difference][0]]

                elif n == difference and len(nums_to_indicies[n]) > 1:
                    return [nums_to_indicies[n][0], nums_to_indicies[n][1]]

                
