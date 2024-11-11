class Solution:
    def removeElement(self, nums, val):
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
            j+=1
        return i
    
    
sol = Solution()
print(sol.removeElement([3,2,2,3], 3))
        