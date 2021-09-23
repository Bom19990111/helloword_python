product = {
    "product_name" : "Iphone promax 13",
    "Brand"        : "Apple",
    "Year"         : 2021,
    "Color"        : ["xanh", "vàng", "hồng"]
}
print(product["product_name"])
product.update({"Year" : 2022})
product.update({"Kilogam" : str(1.3) + "kg"})
print(product)