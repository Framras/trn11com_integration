# importing enum for enumerations
import enum


# creating enumerations using class
class TRn11com_SoapServiceWSDLAddress(enum.Enum):
    Category = "/ws/CategoryService.wsdl"
    Product = "/ws/ProductService.wsdl"
    Order = "/ws/OrderService.wsdl"
    City = "/ws/CityService.wsdl"
    ProductSelling = "/ws/ProductSellingService.wsdl"
    ProductStock = "/ws/ProductStockService.wsdl"
    ShipmentCompany = "/ws/ShipmentCompanyService.wsdl"
    Shipment = "/ws/ShipmentService.wsdl"
    Settlement = "/ws/SettlementService.wsdl"
    Ticket = "/ws/TicketService.wsdl"
