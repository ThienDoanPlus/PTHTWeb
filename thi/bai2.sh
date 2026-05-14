#!/bin/bash

# Sử dụng vòng lặp while true để menu luôn hiển thị lại sau mỗi thao tác
while true; do
    # Xóa màn hình cho sạch sẽ trước mỗi lần hiện menu (tùy chọn)
    # clear 

    echo "==============================="
    echo "  Chuong trinh Tao-Xoa thu muc"
    echo "==============================="
    echo "1. Tao thu muc"
    echo "2. Xoa thu muc"
    echo "3. Thoat chuong trinh"
    echo "-------------------------------"
    
    read -p "Moi ban nhap lua chon (1-3): " choice

    case $choice in
        1) 
            read -p "Nhap ten thu muc muon tao: " fol
            # Kiểm tra nếu chuỗi nhập vào bị rỗng
            if [ -z "$fol" ]; then
                echo "Loi: Ten thu muc khong duoc de trong!"
            elif [ -d "$fol" ]; then
                echo "Thong bao: Thu muc '$fol' DA TON TAI."
            else
                mkdir -p "$fol"
                echo "Thanh cong: Thu muc '$fol' da duoc tao."
            fi
            ;;
        2)
            read -p "Nhap ten thu muc muon xoa: " foldel
            if [ -z "$foldel" ]; then
                echo "Loi: Ten thu muc khong duoc de trong!"
            elif [ ! -d "$foldel" ]; then
                echo "Loi: Khong tim thay thu muc '$foldel'."
            else
                # rmdir chỉ xóa được thư mục rỗng. 
                # Để xóa thư mục có file, dùng rm -rf (nhưng cần cẩn thận)
                # Ở đây dùng rmdir theo đúng chuẩn bài học an toàn:
                if rmdir "$foldel" 2>/dev/null; then
                    echo "Thanh cong: Da xoa thu muc '$foldel'."
                else
                    echo "Loi: Thu muc khong rong hoặc khong co quyen xoa!"
                    read -p "Ban co muon xoa bat chap (xoa ca file ben trong)? (y/n): " force_del
                    if [ "$force_del" == "y" ]; then
                        rm -rf "$foldel"
                        echo "Da xoa toan bo thu muc '$foldel'."
                    fi
                fi
            fi
            ;;
        3)
            echo "Cam on ban da su dung. Thoat chuong trinh!!"
            exit 0 # Exit 0 cho trường hợp thoát thành công theo ý muốn
            ;;
        *) 
            echo "Lua chon khong hop le! Vui long nhap tu 1 den 3."
            ;;
    esac

    # Tạm dừng một chút để người dùng đọc thông báo trước khi quay lại menu
    echo ""
    read -p "Nhan Enter de quay lai Menu..." temp
done
