# importing enum for enumerations
from enum import Enum, unique


@unique
# creating enumerations using class
class TRn11comSoapServicePort(Enum):
    Category = "CategoryServicePortSoap11"
    Product = "ProductServicePortSoap11"
    Order = "OrderServicePortSoap11"
    City = "CityServicePortSoap11"
    ProductSelling = "ProductSellingServicePortSoap11"
    ProductStock = "ProductStockServicePortSoap11"
    ShipmentCompany = "ShipmentCompanyServicePortSoap11"
    Shipment = "ShipmentServicePortSoap11"
    Settlement = "SettlementServicePortSoap11"
    Ticket = "TicketServicePortSoap11"
