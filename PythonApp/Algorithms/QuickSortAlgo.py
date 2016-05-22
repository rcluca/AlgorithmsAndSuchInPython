class QuickSortAlgo(object):
    """description of class"""

    @staticmethod
    def quick_sort(L, lo, hi):
        if lo >= hi:
            return L
        else:
            L, mid = QuickSortAlgo._partition(L, lo, hi)
            L = QuickSortAlgo.quick_sort(L, lo, mid - 1)
            L = QuickSortAlgo.quick_sort(L, mid + 1, hi)
            return L

    @staticmethod
    def _partition(L, lo, hi):
        mid = int((lo + hi) / 2)
        L[mid], L[hi] = L[hi], L[mid]
        while lo < hi:
            if L[lo] <= L[hi]:
                lo += 1
            else:
                L[lo], L[hi - 1], L[hi] = L[hi - 1], L[hi], L[lo]
                hi -= 1
        return L, hi