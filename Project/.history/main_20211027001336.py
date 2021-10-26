import product as p

action = 0

while action >= 0:
    if action == 1:
        p.AddProduct()
    elif action == 2:
        p.DeleteProduct()
    elif action == 3:
        p.UpdateProduct()
    elif action == 4:
        p.ShowAllProduct()
    elif action == 5:       
        p.FindProductByName()
    elif action == 6:       
        p.SortProductNameABC()
        print("Đã sắp xếp thành công! Vui lòng chọn số 4 để xem kết quả")
  
    print("Vui lòng chọn chức năng bạn muốn: ")
    print("0. Thoát khỏi chương trình. ")
    print("1. Thêm mới sản phẩm. ")
    print("2. Xóa sản phẩm. ")
    print("3. Cập nhật thông tin sản phẩm. ")
    print("4. Xem danh sách tất cả sản phẩm. ")
    print("5. Tìm kiếm sản phẩm theo tên hoặc theo thương hiệu. ")
    print("6. Sắp xếp tên sản phẩm A-Z. ")
    print("7. Sắp xếp tên sản phẩm A-Z. ")
    action = int(input("Bạn chọn chức năng? "))
    if action == 0:
        print("Đã thoát chương trình")
        break
