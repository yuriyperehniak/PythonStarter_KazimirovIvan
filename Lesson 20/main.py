from module import *

while True:
    product = input()
    if product == "":
        break
    addProduct(product)

print(getShopping())

with open("shopping_list.txt", 
          "w", encoding="utf8") as file:
    file.write(getShopping())
