from TRn11comSoapServiceWSDLAddress import *
from TRn11comSoapServiceService import *
from TRn11comSoapServicePort import *
from zeep import Client, Settings


def get_n11com_auth(servicecategory):
    appkey = "df848c60-6f80-473b-b129-a00f379a21f1"
    appsecret = "lkuFEB2CxA5cUdun"

    return get_n11com_typefactory(servicecategory).Authentication(appKey=appkey, appSecret=appsecret)


def get_n11com_client(servicecategory):
    soapserver = "https://api.n11.com"
    strictsetting = False
    rawresponsesetting = False

    wsdl = soapserver + get_n11com_servicepath(servicecategory)
    settings = Settings(strict=strictsetting, raw_response=rawresponsesetting)
    return Client(wsdl, settings=settings)


def get_n11com_typefactory(servicecategory):
    defaultnamespace = "http://www.n11.com/ws/schemas"
    return get_n11com_client(servicecategory).type_factory(defaultnamespace)


def get_n11com_service(servicecategory):
    service = TRn11comSoapServiceService[servicecategory].value
    port = TRn11comSoapServicePort[servicecategory].value

    return get_n11com_client(servicecategory).bind(service, port)


def get_n11com_servicepath(servicecategory):
    return TRn11comSoapServiceWSDLAddress[servicecategory].value


sellercode = "framras"

# GetTopLevelCategories(auth: ns0:Authentication)
# -> result: ns0:ResultInfo, categoryList: ns0:TopCategoryList
response = get_n11com_service("Category").GetTopLevelCategories(get_n11com_auth("Category"))
# ns0:TopCategoryList(category: ns0:SubCategory[])
# ns0:SubCategory(id: xsd:long, name: xsd:string)
# if rawresponsesetting:
#     print("1:" + response.text)
#     print("1:" + "not implemented")
# else:
print("1:" + response.result.status)
print(response["result"])
print(response["categoryList"])
for r in response.categoryList.category:
    print(r.id)
    print(r.name)

response = get_n11com_service("Product").GetProductBySellerCode(get_n11com_auth("Product"), sellerCode="RHW003301")
# if rawresponsesetting:
#     print("2:" + response.text)
#     print("2:" + "not implemented")
# else:
print("2:" + response.result.status)
print("2:" + str(response))

# ns0:OrderSearchPeriod(startDate: xsd:string, endDate: xsd:string)

# ns0:OrderDataListRequest(productId: xsd:long, status: xsd:string, buyerName: xsd:string, orderNumber: xsd:string,
# productSellerCode: xsd:string, recipient: xsd:string, sameDayDelivery: xsd:boolean, period: ns0:OrderSearchPeriod,
# sortForUpdateDate: xsd:boolean)
searchData = {'productID': 213386280,
              'buyerName': "",
              'orderNumber': "",
              'productSellerCode': "",
              'recipient': "",
              'period': {'startDate': "", 'endDate': ""},
              'sortForUpdateDate': ""}

orderdatalistrequest = get_n11com_client("Order").get_type("ns0:OrderDataListRequest")
searchData3 = orderdatalistrequest(searchData)

auth = get_n11com_auth("Order")

# DetailedOrderList(auth: ns0:Authentication, searchData: ns0:OrderDataListRequest, pagingData: ns0:PagingData)
# -> result: ns0:ResultInfo, orderList: ns0:DetailedOrderDataList, pagingData: ns0:PagingData
response = get_n11com_service("Order").DetailedOrderList(auth, searchData)
# ns0:ResultInfo(status: xsd:string, errorCode: xsd:string, errorMessage: xsd:string, errorCategory: xsd:string)

# ns0:DetailedOrderDataList(order: ns0:DetailedOrderData[])
# ns0:DetailedOrderData(id: xsd:long, invoiceType: xsd:string, status: xsd:integer, orderNumber: xsd:string,
# totalAmount: xsd:decimal, paymentType: xsd:integer, citizenshipId: xsd:string,
# orderItemList: ns0:DetailedOrderItemDataList, createDate: xsd:string)
# if rawresponsesetting:
#     print("3:" + response.text)
#     print("3:" + "not implemented")
# else:
print("3:" + response.result.status)
# ns3:DetailedOrderListResponse
print(response.orderList)
