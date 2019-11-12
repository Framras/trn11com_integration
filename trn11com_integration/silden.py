import zeep

wsdl = 'https://api.n11.com/ws/CategoryService.wsdl'
client = zeep.Client(wsdl)
auth = [{
    'appKey': 'df848c60-6f80-473b-b129-a00f379a21f1',
    'appSecret': 'lkuFEB2CxA5cUdun'
}]
print(client.service.GetTopLevelCategories(auth))
