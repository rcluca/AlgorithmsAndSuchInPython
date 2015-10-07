class MergeSort():
    """Python implementation of classic Mergesort algorithm"""

    def merge_sort(self, list):
        if len(list) <= 1:
            return list
        else:
            mid = int(len(list)/2)
            leftList = self.merge_sort(list[:mid])
            rightList = self.merge_sort(list[mid:])
            return self._sort(leftList, rightList)

    def _sort(self, leftList, rightList):
        idxL = 0
        idxR = 0
        list = []
        while idxL < len(leftList) and idxR < len(rightList):
            if leftList[idxL] <= rightList[idxR]:
                list.append(leftList[idxL])
                idxL += 1
            else:
                list.append(rightList[idxR])
                idxR += 1
        while idxL < len(leftList):
            list.append(leftList[idxL])
            idxL += 1
        while idxR < len(rightList):
            list.append(rightList[idxR])
            idxR += 1
        return list