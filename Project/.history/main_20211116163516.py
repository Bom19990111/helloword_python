import product as p

def choose():
    action = 0
    while action >= 0:
        if action == 1:
            p.AddProduct()
            print("--------------------------------")
        elif action == 2:
            p.DeleteProduct()
        elif action == 3:
            p.UpdateProduct()
        elif action == 4:
            p.ShowAllProduct()
        elif action == 5:
            p.FindProductByName()
        elif action == 6:
            p.SortProductNameA_Z()
            print("Đã sắp xếp thành công! Vui lòng chọn số 4 để xem kết quả".upper())
            print("********************************")
        elif action == 7:
            p.SortProductNameZ_A()
            print("Đã sắp xếp thành công! Vui lòng chọn số 4 để xem kết quả".upper())
            print("********************************")
        elif action == 8:
            p.SortPriceAsc()
            print("Đã sắp xếp thành công! Vui lòng chọn số 4 để xem kết quả".upper())
            print("********************************")
        elif action == 9:
            p.SortPriceDesc()
            print("Đã sắp xếp thành công! Vui lòng chọn số 4 để xem kết quả".upper())
            print("********************************")
        elif action == 10:
            p.ImportExecel()
        elif action == 11:
            p.ExportExecl()
        elif action ==12:
            print("Chức năng nă")
            
        print("Vui lòng chọn chức năng bạn muốn: ")
        print("0. Thoát khỏi chương trình. ")
        print("1. Thêm mới sản phẩm. ")
        print("2. Xóa sản phẩm. ")
        print("3. Cập nhật thông tin sản phẩm. ")
        print("4. Xem danh sách tất cả sản phẩm. ")
        print("5. Tìm kiếm sản phẩm theo tên hoặc theo thương hiệu. ")
        print("6. Sắp xếp tên sản phẩm A-Z. ")
        print("7. Sắp xếp tên sản phẩm Z-A. ")
        print("8. Sắp xếp giá sản phẩm tăng dần. ")
        print("9. Sắp xếp tên sản phẩm giảm dần. ")
        print("10. Import file excel. ")
        print("11. Export file excel. ")
        try:
            action = int(input("Bạn chọn chức năng? "))
        except ValueError:
            if action == 12:
                print("Chức năng này hiện chưa có, mời bạn chọn lại!".upper())
            else: 
                print("Không có chức năng bạn chọn, mời chọn lại!".upper())
            try:
                choose()
            except:
                print("Dừng chương trình!")
        if action == 0:
            print("Đã thoát chương trình")
            break

choose()
