class PriorityQueue:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, shipment):
        """
        Kargoyu öncelik sırasına göre ekler
        Zaman Karmaşıklığı: O(log n)
        """
        self.heap.append(shipment)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i].delivery_time < self.heap[parent].delivery_time:
            self.swap(i, parent)
            self._sift_up(parent)

    def extract_min(self):
        """
        En yüksek öncelikli kargoyu çıkarır
        Zaman Karmaşıklığı: O(log n)
        """
        if not self.heap:
            return None

        min_shipment = self.heap[0]
        last_shipment = self.heap.pop()

        if self.heap:
            self.heap[0] = last_shipment
            self._sift_down(0)

        return min_shipment

    def _sift_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        if (left < len(self.heap) and
                self.heap[left].delivery_time < self.heap[min_index].delivery_time):
            min_index = left

        if (right < len(self.heap) and
                self.heap[right].delivery_time < self.heap[min_index].delivery_time):
            min_index = right

        if i != min_index:
            self.swap(i, min_index)
            self._sift_down(min_index)