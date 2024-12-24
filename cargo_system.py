
from customer import Customer
from shipment import Shipment
from tree import DeliveryTree
from priority_queue import PriorityQueue
from sorting import CargoSortSearch
from enums import DeliveryStatus


class CargoSystem:
    def __init__(self):
        self.customers = {}
        self.delivery_tree = DeliveryTree()
        self.priority_queue = PriorityQueue()
        self.all_shipments = []

    def add_customer(self, customer_id, name, surname):
        """Yeni müşteri ekler"""
        try:
            customer = Customer(customer_id, name, surname)
            self.customers[customer_id] = customer
            return True
        except ValueError as e:
            print(f"Hata: {e}")
            return False

    def add_shipment(self, shipment_id, customer_id, delivery_time):
        """Müşteriye yeni gönderi ekler ve öncelik sırasına alır"""
        if customer_id in self.customers:
            try:
                shipment = Shipment(shipment_id, delivery_time)
                self.customers[customer_id].add_shipment(shipment)
                self.priority_queue.insert(shipment)
                self.all_shipments.append(shipment)
                return True
            except ValueError as e:
                print(f"Hata: {e}")
                return False
        return False

    def get_customer_history(self, customer_id):
        """Müşterinin gönderim geçmişini sorgular"""
        if customer_id in self.customers:
            return self.customers[customer_id].get_shipping_history()
        return None

    def get_customer_recent_shipments(self, customer_id):
        """Müşterinin son gönderilerini sorgular"""
        if customer_id in self.customers:
            return self.customers[customer_id].get_recent_shipments()
        return "Hata: Müşteri bulunamadı!"

    def find_delivered_shipment(self, shipment_id):
        """Teslim edilmiş kargoyu ID'ye göre bulur"""
        delivered_shipments = [s for s in self.all_shipments
                               if s.delivery_status == DeliveryStatus.TESLIM_EDILDI]
        sorted_shipments = sorted(delivered_shipments, key=lambda x: x.shipment_id)
        return CargoSortSearch.binary_search(sorted_shipments, shipment_id)

    def get_undelivered_shipments_sorted(self):
        """Teslim edilmemiş kargoları teslimat süresine göre sıralar"""
        undelivered = [s for s in self.all_shipments
                       if s.delivery_status == DeliveryStatus.TESLIM_EDILMEDI]
        return CargoSortSearch.merge_sort(undelivered)

    def add_delivery_route(self, parent_id, city_id, city_name):
        """Teslimat rotası ekler"""
        return self.delivery_tree.add_city(parent_id, city_id, city_name)

    def calculate_delivery_time(self, city_id):
        """Belirli bir şehre teslimat süresini hesaplar"""
        return self.delivery_tree.calculate_delivery_time(city_id)

    def get_shipment_status(self, shipment_id):
        """
        Kargo durumunu sorgular (teslim edilmiş veya edilmemiş)
        """
        for shipment in self.all_shipments:
            if shipment.shipment_id == shipment_id:
                return shipment
        return None