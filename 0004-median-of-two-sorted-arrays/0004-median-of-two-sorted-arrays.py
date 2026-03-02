class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # input: two sorted arrays
        # output: return median of the two arrays merged

        # cut to be taken between low and high 
        low = 0
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # taking high value of shorter array 
        high = len(nums1)
    
        total = len(nums1)+len(nums2)
        while low<=high:
            # cut1 -> start with midpt
            cut1 = (low+high)//2
            cut2 = (len(nums1)+len(nums2)+1)//2-cut1

            # l1 last element in arr1, l2 last element from arr2 -> from left half 
            # r1, r2 -> from right half
            l1 = nums1[cut1-1] if cut1 > 0 else float("-inf")
            r1 = nums1[cut1]   if cut1 < len(nums1) else float("inf")
            
            l2 = nums2[cut2-1] if cut2 > 0 else float("-inf")
            r2 = nums2[cut2]   if cut2 < len(nums2) else float("inf")
            
            if l1<=r2 and l2<=r1:
                if total%2 == 0:
                    return (max(l1, l2)+min(r1, r2))/2.0
                else:
                    return max(l1, l2)
            elif l1>r2:
                high = cut1-1
            else:
                low = cut1+1
        return 0.0

