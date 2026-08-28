class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0
        new_nums = nums.copy()

        while new_nums:
            mid = len(new_nums) // 2

            if new_nums[mid] == target:
                return index + mid

            elif target > new_nums[mid]:
                index += mid + 1
                new_nums = new_nums[mid + 1:]

            elif target < new_nums[mid]:
                new_nums = new_nums[:mid]

        return -1
            
