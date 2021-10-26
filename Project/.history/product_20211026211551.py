import data as list_product
import random


def __init__(self, Id, Product_code, Product_name, Brand, Year, Size):
    self.Id = Id
    self.Product_code = Product_code
    self.Product_name = Product_name
    self.Brand = Brand
    self.Year = Year
    self.Size = Size

# Thêm sản phẩm


def AddProduct():
    print("THÊM SẢN PHẨM")
    product = {
        "Id": "",
        "Product_code": "",
        "Product_name": "",
        "Brand": "",
        "Price": "",
        "Year": "",
        "Quantity": "",
        "Size": ""
    }
    print("Nhập ID sản phẩm:")
    Id = int(input())
    while True:
        student = FindProductDuplicate(Id)
        if student != False:
            print("ID đã tồn tại, vui lòng nhập lại ID:")
            Id = int(input())
        else:
            break
    product['Id'] = Id
    # Mã sản phẩm random
    code_product = random.randint(1, 99)
    str_id = "HKS"
    if code_product >= 9:
        str_id += "0" + str(code_product)
    else:
        str_id += str(code_product)

    product["Product_code"] = str_id
    print("Nhập tên sản phẩm: ")
    product['Product_name'] = input()
    print("Nhập thương hiệu sản phẩm: ")
    product['Brand'] = input()
    print("Nhập giá sản phẩm: ")
    product['Price'] = float(input())
    print("Nhập năm sản xuất: ")
    product['Year'] = int(input())
    print("Nhập số lượng: ")
    product['Quantity'] = int(input())
    print("Nhập size giày: ")
    product['Size'] = input()
    list_product.list_product.append(product)

    answer = input("Bạn có muốn nhập tiếp không? Y/N ")
    if answer == "y" or answer == "Y":
        AddProduct()

# Tìm kiếm ID trùng lặp


def FindProductDuplicate(Id):
    for i in range(0, len(list_product.list_product)):
        if list_product.list_product[i]['Id'] == Id:
            return [i, list_product.list_product[i]]
    return False

# Hiển thị tất cả sản phẩm


def ShowAllProduct():
    print("*** HIỂN THỊ TẤT CẢ SẢN PHẨM ***")
    if len(list_product.list_product) == 0 or len(list_product.list_product) < 0:
        print("Chưa có sản phẩm nào để hiển thị! ".upper())
    for i in range(0, len(list_product.list_product)):
        print("ID: ", list_product.list_product[i]['Id']),
        print("Mã sản phẩm: ", list_product.list_product[i]['Product_code']),
        print("Tên sản phẩm: ", list_product.list_product[i]['Product_name']),
        print("Thương hiệu: ", list_product.list_product[i]['Brand']),
        print("Giá: ", list_product.list_product[i]['Price']),
        print("Năm xuất bản: ", list_product.list_product[i]['Year']),
        print("Số lượng: ", list_product.list_product[i]['Quantity']),
        print("Size giày: ", list_product.list_product[i]['Size'])
        print("________________________________")

# Sửa thông tin sản phẩm


def UpdateProduct():
    print("*** CẬP NHẬT THÔNG TIN SẢN PHẨM ***")
    print("Nhập ID sản phẩm cần sửa")
    Id = int(input())
    product = FindProductDuplicate(Id)
    if product == False:
        print("Không tìm thấy sản phẩm ID = ", Id)
    else:
        print("""Bạn muốn cập nhật mục nào ? : 
        0. Thoát.
        1. Tên sản phẩm.
        2. Thương hiệu sản phẩm.
        3. Giá sản phẩm
        4. Size giày.
        5. Số lượng.
        6. Năm xuất bản. """)
    action = 0
    while action >= 0:
        if action == 1:
            UpdateProductName()
        elif action == 2:
            UpdateProductBrand()
        elif action == 3:
            UpdateProductPrice()
        elif action == 4:
            UpdateProductSize()
        elif action == 5:
            UpdateProductQuatity()
        elif action == 6:
            UpdateProductYear()

        def UpdateProductName():
            print("Nhập tên sản phẩm")
            name_product = input()
            product[1]['Product_name'] = name_product

        def UpdateProductBrand():
            print("Nhập thương hiệu của sản phẩm")
            name_product = input()
            product[1]['Brand'] = name_product

        def UpdateProductPrice():
            print("Nhập giá mới của sản phẩm")
            name_product = float(input())
            product[1]['Price'] = name_product

        def UpdateProductSize():
            print("Nhập size của sản phẩm")
            name_product = input()
            product[1]['Size'] = name_product

        def UpdateProductYear():
            print("Nhập năm sản xuất của sản phẩm")
            name_product = int(input())
            product[1]['Year'] = name_product
            list_product.list_product[product[0]] = product[1]

        def UpdateProductQuatity():
            print("Nhập số lượng sản phẩm")
            name_product = int(input())
            product[1]['Quantity'] = name_product
            list_product.list_product[product[0]] = product[1]
        action = int(input("Bạn chọn mục cập nhật nào? "))
        if action == 0:
            print("Không cập nhật mục nào")
            break

# Xóa sản phẩm


def DeleteProduct():
    print("*** XÓA SẢN PHẨM ***")
    print("Nhập ID sản phẩm cần xóa:")
    Id = int(input())
    product = FindProductDuplicate(Id)
    if product != False:
        list_product.list_product.remove(product[1])
        print("Xóa sản phẩm thành công!")
    else:
        print("Không tìm thấy sản phẩm muốn xóa!")

# Tìm kiếm sản phẩm


def FindProductByName():
    print("*** TÌM KIẾM SẢN PHẨM ***")
    NameProduct = str(
        input("Nhập tên sản phẩm hoặc tên thương hiệu bạn muốn tìm kiếm: ")).upper() 
    for i in range(0, len(list_product.list_product)):
        if str(list_product.list_product[i]['Product_name']).upper() in NameProduct or str(list_product.list_product[i]['Brand']).upper() in NameProduct:
            print("ID: ", list_product.list_product[i]['Id']),
            print("Mã sản phẩm: ",
                  list_product.list_product[i]['Product_code']),
            print("Tên sản phẩm: ",
                  list_product.list_product[i]['Product_name']),
            print("Thương hiệu: ", list_product.list_product[i]['Brand']),
            print("Giá: ", list_product.list_product[i]['Price']),
            print("Năm xuất bản: ", list_product.list_product[i]['Year']),
            print("Số lượng: ", list_product.list_product[i]['Quantity']),
            print("Size giày: ", list_product.list_product[i]['Size'])
            print("________________________________")
        else:
            print("Không tìm thấy sản phẩm này @@".upper())

# Sắp xếp sản phẩm
# def SortProductAsc():

