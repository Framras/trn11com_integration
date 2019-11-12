import frappe
from zeep import Client, Settings


def communicate_with_n11com(servicepath):
    company = frappe.defaults.get_user_default("Company")
    # This should only be used if the integration is enabled
    if frappe.db.get_single_value("TR n11com Integration Settings", "enable") == 1:
        # Select the server according to the mode of the integration
        soapserver = frappe.db.get_single_value("TR n11com Integration Settings", "server")
        soapservicepath = servicepath

        auth = [{
            'appKey': frappe.db.get_value("TR n11com Company Settings", "company", "appkey"),
            'appSecret': frappe.db.get_value("TR n11com Company Settings", "company", "appsecret")
        }]
        wsdl = soapserver + soapservicepath
        settings = Settings(strict=False, raw_response=False)
        return Client(wsdl, settings=settings)


@frappe.whitelist()
def test_integration(testappkey, testappsecret):
    soapserver = frappe.db.get_single_value("TR n11com Integration Settings", "server")
    soapservicepath = "/ws/CategoryService.wsdl"

    wsdl = soapserver + soapservicepath
    settings = Settings(strict=False, raw_response=False)
    client = Client(wsdl, settings=settings)

    # company = frappe.defaults.get_user_default("Company")
    auth = [{
        # 'appKey': frappe.db.get_value("TR n11com Company Settings", "company", "appkey"),
        'appKey': testappkey,
        # 'appSecret': frappe.db.get_value("TR n11com Company Settings", "company", "appsecret")
        'appSecret': testappsecret
    }]

    return client.service.GetTopLevelCategories(auth).result.status
