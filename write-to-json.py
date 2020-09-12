import json

data = {
    "SKU1001": {
        "name":"ACME Anvils",
        "cost":1200,
        "stock":5
    },
    "ABC101": {
        "name":"Toilet Roll",
        "cost":10.50,
        "stock":15
    }
}

with open('inventory.json', 'w') as fp: #fp is short for filepointer
    json.dump(data, fp)