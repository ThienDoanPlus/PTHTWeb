#!/usr/bin/env python3
import os

def list_only_files():
    folder = input("Nhập đường dẫn thư mục: ")
    
    if not os.path.isdir(folder):
        print("Lỗi: Thư mục không tồn tại.")
        return

    print(f"Các tập tin có trong '{folder}':")
    # Lấy danh sách nội dung trong thư mục
    for item in os.listdir(folder):
        full_path = os.path.join(folder, item)
        # Chỉ liệt kê nếu là tập tin (isfile)
        if os.path.isfile(full_path):
            print(f" - {item}")

if __name__ == "__main__":
    list_only_files():
