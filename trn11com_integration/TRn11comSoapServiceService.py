# importing enum for enumerations
from enum import Enum, unique


@unique
# creating enumerations using class
class TRn11comSoapServiceService(Enum):
    Category = "CategoryServicePortService"
    Product = "ProductServicePortService"
    Order = "OrderServicePortService"
    City = "CityServicePortService"
    ProductSelling = "ProductSellingServicePortService"
    ProductStock = "ProductStockServicePortService"
    ShipmentCompany = "ShipmentCompanyServicePortService"
    Shipment = "ShipmentServicePortService"
    Settlement = "SettlementServicePortService"
    Ticket = "TicketServicePortService"
