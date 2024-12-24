from datetime import datetime
from enums import DeliveryStatus, CargoStatus

class Shipment:
    _used_ids = set()

    def __init__(self, shipment_id, delivery_time):
        try:
            self.shipment_id = str(int(shipment_id))
            if self.shipment_id in Shipment._used_ids:
                raise ValueError(f"Bu Gönderi ID ({shipment_id}) zaten kullanımda!")

            self.delivery_time = delivery_time
            self.shipment_date = datetime.now().strftime("%d-%m-%Y %H:%M")
            self.delivery_status = DeliveryStatus.TESLIM_EDILMEDI
            self.cargo_status = CargoStatus.ISLEME_ALINDI
            Shipment._used_ids.add(self.shipment_id)
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                raise ValueError("Gönderi ID sadece sayı olabilir!")
            raise e

    def update_cargo_status(self, new_status):
        self.cargo_status = new_status
        if new_status == CargoStatus.TESLIM_EDILDI:
            self.delivery_status = DeliveryStatus.TESLIM_EDILDI