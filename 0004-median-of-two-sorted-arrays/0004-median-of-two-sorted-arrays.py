from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Combine the two arrays
        arr = nums1 + nums2
        # Sort the combined array
        arr.sort()
        # Calculate the total length of the combined array
        total = len(arr)

        # If the total length is odd, return the middle element
        if total % 2 == 1:
            return float(arr[total // 2])
        else:
            # If the total length is even, return the average of the two middle elements
            middle1 = arr[total // 2 - 1]
            middle2 = arr[total // 2]
            return (middle1 + middle2) / 2.0
