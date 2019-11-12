import frappe
import zeep


@frappe.whitelist()
def test_integration(testappkey, testappsecret):
    soapserver = frappe.db.get_single_value("TR n11com Integration Settings", "server")
    soapservicepath = "/ws/CategoryService.wsdl"

    wsdl = soapserver + soapservicepath
    client = zeep.Client(str(wsdl))

    # company = frappe.defaults.get_user_default("Company")
    auth = [{
        # 'appKey': frappe.db.get_value("TR n11com Company Settings", "company", "appkey"),
        'appKey': str(testappkey),
        # 'appSecret': frappe.db.get_value("TR n11com Company Settings", "company", "appsecret")
        'appSecret': str(testappsecret)
    }]
    return client.service.GetTopLevelCategories(auth).result.status
