#!/usr/bin/env python3
import os

def delete_by_ext():
    folder = input("Nhập thư mục (ví dụ: Desktop): ")
    ext = input("Nhập loại tập tin (ví dụ: txt): ")
    
    # Chuyển về đường dẫn đầy đủ
    target_dir = os.path.expanduser(f"~/{folder}")

    if os.path.isdir(target_dir):
        count = 0
        for item in os.listdir(target_dir):
            if item.endswith(f".{ext}"):
                os.remove(os.path.join(target_dir, item))
                count += 1
        print(f"Đã xóa thành công {count} tập tin .{ext}")
    else:
        print("Lỗi: Thư mục không tồn tại.")

if __name__ == "__main__":
    delete_by_ext()
