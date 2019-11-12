import zeep

soapserver = 'https://api.n11.com'
soapservicepath = '/ws/CategoryService.wsdl'

wsdl = soapserver + soapservicepath
client = zeep.Client(wsdl)

# company = frappe.defaults.get_user_default("Company")
auth = [{
    # 'appKey': frappe.db.get_value("TR n11com Company Settings", "company", "appkey"),
    'appKey': 'df848c60-6f80-473b-b129-a00f379a21f1',
    # 'appSecret': frappe.db.get_value("TR n11com Company Settings", "company", "appsecret")
    'appSecret': 'lkuFEB2CxA5cUdun'
}]

print(client.service.GetTopLevelCategories(auth))
