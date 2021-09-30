def search(self, nums: List[int], target: int) -> int:
    def binSearch(nums, target, start, end):
        mid = (start+end)//2
        if start>end:
            return -1
        elif nums[mid] == target:
            return mid
        elif nums[mid]<target:
            return binSearch(nums, target, mid+1, end)
        else:
            return binSearch(nums, target, start, mid-1)
    return binSearch(nums, target, 0, len(nums)-1)
