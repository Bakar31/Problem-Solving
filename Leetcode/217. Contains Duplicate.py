class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        initial_length = len(nums)
        final_length = len(set(nums))

        if initial_length != final_length:
            return True
        else:
            False