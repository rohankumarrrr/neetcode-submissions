class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        if len(nums2) < len(nums1):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        while True:

            pivotA = l + (r - l) // 2
            pivotB = half - pivotA - 2

            Aleft = A[pivotA] if pivotA >= 0 else float("-infinity")
            Aright = A[pivotA + 1] if pivotA + 1 < len(A) else float("infinity")
            Bleft = B[pivotB] if pivotB >= 0 else float("-infinity")
            Bright = B[pivotB + 1] if pivotB + 1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = pivotA - 1
            else:
                l = pivotA + 1
        
        return None