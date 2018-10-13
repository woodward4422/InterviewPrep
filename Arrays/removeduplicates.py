# Question: Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length. Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory

# My Initial Thoughts: Its sorted so let us try an approach where we iterate through the array and check to see if we can

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0 
        
        counter = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i] == nums[i-1]:
                del nums[i]
            else:
                counter += 1
        print(nums)
        return counter + 1


solution = Solution()
nums = [1,1,2,3,4,5,6,6,7,8,9,9,9,10,11,11,12,12,13,14,14]
unique_characters = solution.removeDuplicates(nums)
print(unique_characters)





