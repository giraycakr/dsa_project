from linked_list import LinkedList
from stack import ShipmentStack


class Customer:
    _used_ids = set()

    def __init__(self, customer_id, name, surname):

        try:
            self.customer_id = str(int(customer_id))
            if self.customer_id in Customer._used_ids:
                raise ValueError(f"Bu Müşteri ID ({customer_id}) zaten kullanımda!")

            self.name = name
            self.surname = surname
            self.shipping_history = LinkedList()
            self.recent_shipments = ShipmentStack()
            Customer._used_ids.add(self.customer_id)
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                raise ValueError("Müşteri ID sadece sayı olabilir!")
            raise e

    def add_shipment(self, shipment):
        """Yeni gönderiyi hem geçmişe hem de stack'e ekler"""
        self.shipping_history.add_sorted(shipment)
        self.recent_shipments.push(shipment)

    def get_shipping_history(self):
        """Müşterinin tüm gönderilerini döndürür"""
        return self.shipping_history.get_all()

    def get_recent_shipments(self):
        """Son 5 gönderiyi sorgular"""
        return self.recent_shipments.get_recent_shipments()