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

    print("Vui lòng chọn một chức năng: ")
    print("0. Thoát khỏi chương trình")
    print("1. Thêm mới sản phẩm ")
    print("2. Xóa sản phẩm")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xem danh sách tất cả sản phẩm")
    action = int(input("Bạn chọn chức năng? "))
    if action == 0:
        print("Đã thoát chương trình")
        break
