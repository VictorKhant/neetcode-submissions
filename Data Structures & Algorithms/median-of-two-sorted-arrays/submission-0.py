class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):                        
            nums1, nums2 = nums2, nums1
        total = len(nums1) + len(nums2)
        l, r = -1, len(nums1) - 1                          
        while l <= r:
            m1 = (l + r) // 2
            m2 = (total // 2) - m1 - 2                      
            a_left  = nums1[m1]     if m1 >= 0             else float('-inf')  
            a_right = nums1[m1 + 1] if m1 + 1 < len(nums1) else float('inf')  
            b_left  = nums2[m2]     if m2 >= 0             else float('-inf') 
            b_right = nums2[m2 + 1] if m2 + 1 < len(nums2) else float('inf')   
            if a_left <= b_right and b_left <= a_right:
                if total % 2 != 0:
                    return min(b_right, a_right)
                else:
                    return (max(a_left, b_left) + min(b_right, a_right)) / 2   
            elif a_left > b_right:
                r = m1 - 1
            else:
                l = m1 + 1
        return -1
