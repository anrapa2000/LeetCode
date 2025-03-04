from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left = 0
        right = len(nums1) - 1

        while True:
            a = (left + right) // 2
            b = half - a - 2

            Aleft = nums1[a] if a >= 0 else float("-inf")
            Aright = nums1[a + 1] if a + 1 < len(nums1) else float("inf")

            Bleft = nums2[b] if b >= 0 else float("-inf")
            Bright = nums2[b + 1] if b + 1 < len(nums2) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                return min(Aright, Bright)
            elif Aleft > Bright:
                right = a - 1

            else:
                left = a + 1
