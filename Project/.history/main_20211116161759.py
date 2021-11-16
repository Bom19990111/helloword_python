import product as p

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
        p.ImportExecel()()
    elif action == 11:
        p.ExportExecl()

    try:
        action = int(input("Bạn chọn chức năng? "))
    except:
        action = int(input("Không có chức năng bạn chọn, mời chọn lại!"))
            
    if action == 0:
        print("Đã thoát chương trình")
        break
