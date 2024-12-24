from enum import Enum

class DeliveryStatus(Enum):
    TESLIM_EDILDI = "Teslim Edildi"
    TESLIM_EDILMEDI = "Teslim Edilmedi"

class CargoStatus(Enum):
    ISLEME_ALINDI = "İşleme Alındı"
    TESLIMATTA = "Teslimatta"
    TESLIM_EDILDI = "Teslim Edildi"