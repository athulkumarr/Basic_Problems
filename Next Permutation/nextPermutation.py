def nextPermutation(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return nums
        flag = 0
        i = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                flag = 1
                break
        i = i-1
        for j in range(len(nums)-1, i, -1):
            if nums[j]>nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                break
        if flag == 0:
            nums.sort()
        else:
            nums[i+1:] = sorted(nums[i+1:])
        return nums
