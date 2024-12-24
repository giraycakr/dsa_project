class ShipmentStack:
    def __init__(self):
        self.items = []
        self.max_size = 5

    def is_empty(self):
        return len(self.items) == 0

    def push(self, shipment):
        if len(self.items) >= self.max_size:
            self.items.pop(0)
        self.items.append(shipment)

    def get_recent_shipments(self):
        if self.is_empty():
            return "Hata: Gönderim geçmişi boş!"
        return list(reversed(self.items))

    def size(self):
        """Stack'teki kargo sayısını döndürür"""
        return len(self.items)