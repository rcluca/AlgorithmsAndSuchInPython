import math

class BinaryHeap:
    def __init__(self, list = None):
        if list == None:
            self.heap_list = []
        else:
            self.heap_list = []
            for each in list:
                self.insert(each)

    def __str__(self):
        return self.heap_list

    def get_max(self):
        return self.heap_list[0]

    def get_size(self):
        return len(self.heap_list)

    def insert(self, item):
        self.heap_list.append(item)
        self._swim(item)

    def remove(self, item_idx):
        if item_idx <= self.get_size() - 1 and item_idx >= 0:
            if self.get_size() > 1:
                self._swap_items(self.heap_list, item_idx, self.get_size() - 1)
                self.heap_list.pop()
                self._sink(item_idx, self.heap_list)
            elif self.get_size() == 1:
                self.heap_list.pop()

    def _swap_items(self, list, item_idx, other_idx):
        list[item_idx], list[other_idx] = list[other_idx], list[item_idx]

    def _swim(self, item):
        if self.get_size() > 1:
            item_idx = self.get_size() - 1
            parent_idx = int(math.floor(self.get_size() / 2) - 1)
            while parent_idx >= 0 and self.heap_list[item_idx] > self.heap_list[parent_idx]:
                self._swap_items(self.heap_list, item_idx, parent_idx)
                item_idx = parent_idx
                parent_idx = int(math.floor((parent_idx + 1) / 2) - 1)

    def _sink(self, item_idx, list):
        child1_idx = (item_idx + 1) * 2 - 1
        child2_idx = (item_idx + 1) * 2
        while child1_idx < self.get_size():
            if list[child1_idx] > list[item_idx]:
                self._swap_items(list, child1_idx, item_idx)
                item_idx = child1_idx
                child2_idx = (child1_idx + 1) * 2
                child1_idx = (child1_idx + 1) * 2 - 1
            elif child2_idx < self.get_size() and list[child2_idx] > list[item_idx]:
                self._swap_items(list, child2_idx, item_idx)
                item_idx = child2_idx
                child2_idx = (child1_idx + 1) * 2
                child1_idx = (child1_idx + 1) * 2 - 1
            else:
                return
              

game = BinaryHeap([4,2,1,4,24,55,5,25,11,23])
print game.__str__()