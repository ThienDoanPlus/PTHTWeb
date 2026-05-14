#!/usr/bin/env python3
import os

def find_file():
    while True:
        filename = input("Nhập tên tập tin cần tìm (ví dụ: tintuc.txt): ")

        # Câu 4: Kiểm tra phần mở rộng (phải có dấu chấm)
        if "." not in filename:
            print("Lỗi: Bạn phải nhập cả phần mở rộng (extension). Vui lòng nhập lại!")
            continue
        
        print("Đang tìm kiếm trên hệ thống...")
        found = False
        # Tìm kiếm bắt đầu từ thư mục HOME để an toàn và nhanh
        for root, dirs, files in os.walk(os.path.expanduser("~")):
            if filename in files:
                print(f"Tìm thấy tập tin tại: {os.path.join(root, filename)}")
                found = True
                break # Dừng lại khi tìm thấy file đầu tiên
        
        if not found:
            print("Không tìm thấy tập tin.")
        break

if __name__ == "__main__":
    find_file()
