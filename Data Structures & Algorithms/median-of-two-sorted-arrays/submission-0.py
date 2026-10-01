class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1, n2 = len(nums1), len(nums2)
        half = (n1 + n2 + 1) // 2

        lo, hi = 0, n1
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i

            l1 = nums1[i - 1] if i > 0 else float("-inf")
            r1 = nums1[i] if i < n1 else float("inf")
            l2 = nums2[j - 1] if j > 0 else float("-inf")
            r2 = nums2[j] if j < n2 else float("inf")

            if l1 > r2:
                hi = i - 1
            elif l2 > r1:
                lo = i + 1
            else:
                if (n1 + n2) % 2:
                    return max(l1, l2)
                return (max(l1, l2) + min(r1, r2)) / 2