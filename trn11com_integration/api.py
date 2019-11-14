import frappe
from zeep import Client, Settings


def get_n11com_auth(servicecategory):
    company = frappe.defaults.get_user_default("Company")
    # This should only be used if the integration is enabled for the company
    if frappe.db.get_value("TR n11com Company Settings", company, "enable") == 1:
        factory = get_n11com_client(servicecategory).type_factory(
            frappe.db.get_single_value("TR n11com Integration Settings", "default_namespace"))
        return factory.Authentication(appKey=frappe.db.get_value("TR n11com Company Settings", "company", "appkey"),
                                      appSecret=frappe.db.get_value("TR n11com Company Settings", "company",
                                                                    "appsecret"))
    else:
        return ""


def get_n11com_client(servicecategory):
    company = frappe.defaults.get_user_default("Company")
    # This should only be used if the integration is enabled for the company
    if frappe.db.get_value("TR n11com Company Settings", company, "enable") == 1:
        strictsetting = False
        if frappe.db.get_single_value("TR n11com Integration Settings", "strict") == 1:
            strictsetting = True
        rawresponsesetting = False
        if frappe.db.get_single_value("TR n11com Integration Settings", "raw_response") == 1:
            rawresponsesetting = True

        wsdl = frappe.db.get_single_value("TR n11com Integration Settings", "server") + get_n11com_servicepath(
            servicecategory)
        settings = Settings(strict=strictsetting, raw_response=rawresponsesetting)
        return Client(wsdl, settings=settings)
    else:
        return ""


def get_n11com_typefactory(servicecategory):
    # Available types are:
    # CategoryData, SubCategoryData, SubCategory, ParentCategoryData, ParentCategory, CategoryAttributeList,
    # TopCategoryList, SubCategoryList, CategoryProductAttributeList, CategoryProductAttributeData,
    # CategoryProductAttributeValueData, CategoryProductAttributeValueList, CategoryAttributeData,
    # CategoryAttributeValueList, CategoryAttributeValueData, PagingData, RequestPagingData, BaseRequest,
    # Authentication, BaseResponse, ResultInfo
    return get_n11com_client(servicecategory).type_factory(
        frappe.db.get_single_value("TR n11com Integration Settings", "default_namespace"))


def get_n11com_service(servicecategory):
    service = ""
    port = ""
    if servicecategory == "Category":
        service = "CategoryServicePortService"
        port = "CategoryServicePortSoap11"
    elif servicecategory == "Product":
        service = "ProductServicePortService"
        port = "ProductServicePortSoap11"
    elif servicecategory == "Order":
        service = "OrderServicePortService"
        port = "OrderServicePortSoap11"

    return get_n11com_client(servicecategory).bind(service, port)


def get_n11com_servicepath(servicecategory):
    if servicecategory == "Category":
        return "/ws/CategoryService.wsdl"
    elif servicecategory == "Product":
        return "/ws/ProductService.wsdl"
    elif servicecategory == "Order":
        return "/ws/OrderService.wsdl"
    else:
        return ""


@frappe.whitelist()
def test_integration(testappkey, testappsecret):
    strictsetting = False
    if frappe.db.get_single_value("TR n11com Integration Settings", "strict") == 1:
        strictsetting = True
    rawresponsesetting = False
    if frappe.db.get_single_value("TR n11com Integration Settings", "raw_response") == 1:
        rawresponsesetting = True

    wsdl = frappe.db.get_single_value("TR n11com Integration Settings", "server") + get_n11com_servicepath(
        "Category")
    settings = Settings(strict=strictsetting, raw_response=rawresponsesetting)
    factory = Client(wsdl, settings=settings).type_factory(
        frappe.db.get_single_value("TR n11com Integration Settings", "default_namespace"))
    auth = factory.Authentication(appKey=testappkey, appSecret=testappsecret)

    return get_n11com_service("Category").GetTopLevelCategories(auth).result.status
