def maxArea(self, height: List[int]) -> int:
    l, r = 0, len(height) - 1
    contain, hmax = 0, max(height)
    while hmax * (r - l) >= contain:
        if height[l] < height[r]:
            cur, l = height[l] * (r - l), l + 1
        else:
            cur, r = height[r] * (r - l), r - 1
        contain = max(contain, cur)
    return contain
