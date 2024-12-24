class Node:
    def __init__(self, shipment):
        self.shipment = shipment
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_sorted(self, shipment):
        """Gönderiyi tarih sırasına göre ekler"""
        new_node = Node(shipment)

        if not self.head or self.head.shipment.shipment_date > shipment.shipment_date:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.shipment.shipment_date <= shipment.shipment_date:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def get_all(self):
        """Tüm gönderileri liste olarak döndürür"""
        shipments = []
        current = self.head
        while current:
            shipments.append(current.shipment)
            current = current.next
        return shipments