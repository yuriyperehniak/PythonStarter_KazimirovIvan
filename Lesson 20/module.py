shopping = {}

def addProduct(string):
    key, value = string.split()
    shopping[key] = value
    print(f"Пункт {key} додано")

def getShopping():
    productList = ""
    productList += "-------------------------\n"
    for key, value in shopping.items():
        productList += f"{key.capitalize()}:{value}\n"
    productList += "-------------------------\n"
    return productList
