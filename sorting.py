class CargoSortSearch:
    @staticmethod
    def merge_sort(shipments):
        """
        Merge Sort ile kargoları teslimat süresine göre sıralar
        Zaman Karmaşıklığı: O(n log n)
        """
        if len(shipments) <= 1:
            return shipments

        mid = len(shipments) // 2
        left = CargoSortSearch.merge_sort(shipments[:mid])
        right = CargoSortSearch.merge_sort(shipments[mid:])

        return CargoSortSearch._merge(left, right)

    @staticmethod
    def _merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i].delivery_time <= right[j].delivery_time:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    @staticmethod
    def binary_search(sorted_shipments, target_id):
        """
        Binary Search ile kargo arar
        Zaman Karmaşıklığı: O(log n)
        """
        left, right = 0, len(sorted_shipments) - 1

        while left <= right:
            mid = (left + right) // 2
            if sorted_shipments[mid].shipment_id == target_id:
                return sorted_shipments[mid]
            elif sorted_shipments[mid].shipment_id < target_id:
                left = mid + 1
            else:
                right = mid - 1

        return None