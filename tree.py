class CityNode:
    def __init__(self, city_id, city_name):
        self.city_id = city_id
        self.city_name = city_name
        self.children = []


class DeliveryTree:
    def __init__(self):
        self.root = None

    def add_city(self, parent_id, city_id, city_name):
        new_city = CityNode(city_id, city_name)

        if not self.root and parent_id is None:
            self.root = new_city
            return True

        if parent_id:
            parent = self._find_city(self.root, parent_id)
            if parent:
                parent.children.append(new_city)
                return True
        return False

    def _find_city(self, node, city_id):
        if not node:
            return None

        if node.city_id == city_id:
            return node

        for child in node.children:
            result = self._find_city(child, city_id)
            if result:
                return result
        return None

    def calculate_delivery_time(self, target_city_id):
        depth = self._calculate_depth(self.root, target_city_id, 0)
        return depth if depth >= 0 else None

    def _calculate_depth(self, node, target_id, current_depth):
        if not node:
            return -1

        if node.city_id == target_id:
            return current_depth

        for child in node.children:
            depth = self._calculate_depth(child, target_id, current_depth + 1)
            if depth >= 0:
                return depth
        return -1