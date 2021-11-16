import data as list_product
import random
import pandas as pd


# def __init__(self, Id, Product_code, Product_name, Brand, Year, Size):
#     self.Id = Id
#     self.Product_code = Product_code
#     self.Product_name = Product_name
#     self.Brand = Brand
#     self.Year = Year
#     self.Size = Size

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
        "Size": "",
        "Status": ""
    }
    print("Nhập ID sản phẩm:")
    try:
        Id = int(input())
    except:
        print("ID phải là kiểu số, vui lòng nhập lại".upper())
        print("------------------------------------")
        try:
            AddProduct()
        except RuntimeError:
            print("Dừng chương trình!")
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
    str_id = "HKSP"
    if code_product <= 9:
        str_id += "0" + str(code_product)
    else:
        str_id += str(code_product)

    product["Product_code"] = str_id
    print("Nhập tên sản phẩm: ")
    product['Product_name'] = input()
    print("Nhập thương hiệu sản phẩm: ")
    product['Brand'] = input()
    print("Nhập giá sản phẩm: ")
    try:
        product['Price'] = float(input())
    except ValueError:
        print("Giá phải là kiểu số, vui lòng nhập lại")
        print("------------------------------------")
        try:
            print("Nhập giá sản phẩm: ")
            product['Price'] = float(input())
        except:
            next()
    print("Nhập năm sản xuất: ")
    try:
        product['Year'] = int(input())
    except ValueError:
        print("Năm phải là kiểu số, vui lòng nhập lại")
        try:
            print("Nhập năm sản xuất: ")
            product['Year'] = int(input())
        except:
            print('Dừng chương trình!')
    print("Nhập số lượng: ")
    try:
        product['Quantity'] = int(input())
    except ValueError:
        print("Số lượng phải là kiểu số, vui lòng nhập lại")
        try:
            print("Nhập số lượng: ")
            product['Quantity'] = int(input())
        except:
            print('Dừng chương trình!')
    print("Nhập size giày: ")
    product['Size'] = input() 
    print("Nhập tình trạng sản phẩm: ")
    product['Status'] = input()
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
        print("ID           : \t", list_product.list_product[i]['Id']),
        print("Mã sản phẩm  : \t",
              list_product.list_product[i]['Product_code']),
        print("Tên sản phẩm : \t",
              list_product.list_product[i]['Product_name']),
        print("Thương hiệu  : \t", list_product.list_product[i]['Brand']),
        print("Giá          : \t", list_product.list_product[i]['Price']),
        print("Năm xuất bản : \t", list_product.list_product[i]['Year']),
        print("Số lượng     : \t", list_product.list_product[i]['Quantity']),
        print("Size giày    : \t", list_product.list_product[i]['Size'])
        print("Tình trạng   : \t", list_product.list_product[i]['Status'])
        print("________________________________")

# Sửa thông tin sản phẩm


def UpdateProduct():
    print("*** CẬP NHẬT THÔNG TIN SẢN PHẨM ***")
    print("Nhập ID sản phẩm cần sửa")
    try:
        Id = int(input())
        product = FindProductDuplicate(Id)
    except:
        print("Vui lòng nhập đúng ID")
        try:
            UpdateProduct()
        except:
            print("Dừng chương trình!")
    if product == False:
        print("Không tìm thấy sản phẩm ID = ".upper(), Id)
        print("********************************")
    else:
        print("""Bạn muốn cập nhật mục nào ? :
        0. Thoát.
        1. Tên sản phẩm.
        2. Thương hiệu sản phẩm.
        3. Giá sản phẩm
        4. Size giày.
        5. Số lượng.
        6. Năm xuất bản.
        7. Tình trạng """)
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
            elif action == 7:
                UpdateStatus()

            def UpdateProductName():
                print("Nhập tên cập nhật của sản phẩm: ")
                name_product = input()
                product[1]['Product_name'] = name_product

            def UpdateProductBrand():
                print("Nhập thương hiệu muốn cập nhật: ")
                name_product = input()
                product[1]['Brand'] = name_product

            def UpdateProductPrice():
                print("Nhập giá muốn cập nhật: ")
                name_product = float(input())
                product[1]['Price'] = name_product

            def UpdateProductSize():
                print("Nhập size muốn cập nhật: ")
                name_product = input()
                product[1]['Size'] = name_product

            def UpdateProductYear():
                print("Nhập năm sản xuất muốn cập nhật: ")
                name_product = int(input())
                product[1]['Year'] = name_product
                list_product.list_product[product[0]] = product[1]

            def UpdateProductQuatity():
                print("Nhập số lượng muốn cập nhật: ")
                name_product = int(input())
                product[1]['Quantity'] = name_product
                list_product.list_product[product[0]] = product[1]

            def UpdateStatus():
                print("Nhập tình trạng muốn cập nhật: ")
                name_product = input()
                product[1]['Status'] = name_product
                list_product.list_product[product[0]] = product[1]
            action = int(input("Bạn chọn mục cập nhật nào? "))
            if action == 0:
                print("Không cập nhật mục nào".upper())
                print("********************************")
                break

# Xóa sản phẩm


def DeleteProduct():
    print("*** XÓA SẢN PHẨM ***")
    print("Nhập ID sản phẩm cần xóa:")
    Id = int(input())
    product = FindProductDuplicate(Id)
    if product == False:
        print("Không tìm thấy sản phẩm ID = ".upper(), Id)
        print("********************************")
    else:
        answer = input("Bạn có muốn xóa sản phẩm này không? Y/N ".upper())
        if answer == "y" or answer == "Y":
            if product != False:
                list_product.list_product.remove(product[1])
                print("Xóa sản phẩm thành công!".upper())
                print("********************************")
        else:
            print("Đã từ chối xóa sản phẩm này!".upper())
            print("********************************")


# Tìm kiếm sản phẩm
def FindProductByName():
    print("*** TÌM KIẾM SẢN PHẨM ***")
    if (len(list_product.list_product) == 0 or len(list_product.list_product) < 0):
        print("Chưa có sản phẩm nào trong giỏ!".upper())
        print("********************************")
    else:
        NameProduct = str(
            input("Nhập tên sản phẩm hoặc tên thương hiệu bạn muốn tìm kiếm: ")).upper()
        is_found = False
        for i in range(0, len(list_product.list_product)):
            if str(list_product.list_product[i]['Product_name']).upper() in NameProduct or str(list_product.list_product[i]['Brand']).upper() in NameProduct:
                is_found = True
                print("ID           : \t", list_product.list_product[i]['Id']),
                print("Mã sản phẩm  : \t",
                      list_product.list_product[i]['Product_code']),
                print("Tên sản phẩm : \t",
                      list_product.list_product[i]['Product_name']),
                print("Thương hiệu  : \t",
                      list_product.list_product[i]['Brand']),
                print("Giá          : \t",
                      list_product.list_product[i]['Price']),
                print("Năm xuất bản : \t",
                      list_product.list_product[i]['Year']),
                print("Số lượng     : \t",
                      list_product.list_product[i]['Quantity']),
                print("Size giày    : \t",
                      list_product.list_product[i]['Size'])
                print("Tình trạng   : \t",
                      list_product.list_product[i]['Status'])
                print("________________________________")
        if not is_found:
            print("Không tìm thấy sản phẩm này @@".upper())
            print("********************************")


def SortProductNameA_Z():
    list_product.list_product.sort(key=lambda item: item.get("Product_name"))


def SortProductNameZ_A():
    list_product.list_product.sort(
        key=lambda item: item.get("Product_name"), reverse=True)


def SortPriceAsc():
    list_product.list_product.sort(key=lambda item: item.get("Price"))


def SortPriceDesc():
    list_product.list_product.sort(
        key=lambda item: item.get("Price"), reverse=True)


def ExportExecel():
    xl = pd.ExcelFile('danhsachsanpham.xlsx')
    df = pd.read_excel(xl, header=None)
    print(df.head())


def ImportExecel():
    xl = pd.ExcelFile('danhsachsanpham.xlsx')
    df = pd.read_excel(xl, header=None)
    print(df.head())
