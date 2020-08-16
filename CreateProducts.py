import requests
from requests.auth import HTTPBasicAuth
import json

#response_auth = requests.get('https://ice-bear-has-to-stay-home.myshopify.com', auth=HTTPBasicAuth('daeb8815f46a65e9f500c91d4723d1ec', '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'))
#print(response_auth.text)

#response = requests.post('https://daeb8815f46a65e9f500c91d4723d1ec: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@ice-bear-has-to-stay-home.myshopify.com/admin/api/2020-04/#4928025034888.json', json={"product": {"title": "h 151"}})
headers = {'Content-type': 'application/json',
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}
url = 'https://daeb8815f46a65e9f500c91d4723d1ec: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@ice-bear-has-to-stay-home.myshopify.com/admin/api/2020-04/products.json'


data1 = {
  "product": {
    "title": "Super duper product",
    "body_html": "Description of super duper product",
    "variants": [
      {
        "title": "Default Title",
        "price": "10.00",
        "compare_at_price": "100.00",
        "sku": "1",
        "barcode": "23456",
        "cost_per_item": "12.00",
        "option1": "Default Title",
        "weight": "10.00",
        "inventory_management": "shopify",
        "inventory_quantity": "70"
         }
    ]
  }
}

list_for_product = []
variants = []
variant = {}
data = {}
for i in range(1,10):
    data['title'] = str(i)+ " Super duper product"
    data["body_html"] = str(i) + " Description of super duper product"

    variant['title'] = "Default Title"

    variant['price'] = str(i) +"10.00"

    variant['compare_at_price'] = str(i) +"100.00"

    variant['sku'] = str(i) + "1"

    variant['barcode'] = str(i) + "23456"

    variant['option1'] = "Default Title"

    variant['weight'] = str(i) + "10.00"

    variant["inventory_management"] = "shopify"

    variant['inventory_quantity'] = str(i) + "70"

    variants.append(variant)

    data['product'] = {"title": str(i) + " Super duper product", "body_html": str(i) + " Description of super duper product", "variants": variants}
    #print(data)
    variants = []
    #answer = requests.post(url, data=json.dumps(data), headers=headers)
#print(answer)
#response = answer.json()
#print(response)



response_auth = requests.get('https://online-wwd-4.testms.lognex.ru/api/remap/1.1/entity/product', auth=HTTPBasicAuth('admin@nborisenko', '121212'))
print(response_auth.text)
