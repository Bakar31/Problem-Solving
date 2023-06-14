class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        mapping = {}

        for i, j in enumerate(nums):
            diff = target - j
            print(diff)

            if diff in mapping:
                return [mapping[diff],  i]
            
            mapping[j] = i