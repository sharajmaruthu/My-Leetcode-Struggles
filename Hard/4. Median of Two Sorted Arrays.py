#SOLUTION

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            maxLeftA = float('-inf') if i == 0 else nums1[i - 1]
            minRightA = float('inf') if i == m else nums1[i]

            maxLeftB = float('-inf') if j == 0 else nums2[j - 1]
            minRightB = float('inf') if j == n else nums2[j]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2.0
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                high = i - 1
            else:
                low = i + 1
