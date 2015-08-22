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

    def sort(self, list):
        if len(list) > 1:
            sorted_list = []
            while len(list) > 1:
                self._swap_items(list, 0, len(list) - 1)
                sorted_list.append(list.pop())
                self.sink(0, list)
            sorted_list.append(list.pop())
            return sorted_list
        else:
            return list

word = "hello"

for each in word:
    print each
    if each == "e":
        break



heap = BinaryHeap([34,1,254,2])
heap.insert(4)
heap.insert(2)
heap.insert(3)
heap.insert(1)
heap.insert(3)
heap.insert(4)
heap.insert(2)
heap.remove(1)
heap.remove(6)
heap.remove(0)
heap.remove(1)
heap.insert(10)
heap.insert(7)
heap.remove(4)
heap.insert(24)
print heap.get_size()
print heap.get_max()
print heap.__str__()
#mylist = [24, 4, 10, 1, 3, 7]
# print heap.sort(mylist)

