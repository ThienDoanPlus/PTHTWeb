#!/usr/bin/env python3
import os

def read_content():
    path = input("Nhập đường dẫn tập tin (ví dụ: Desktop/vanban.txt): ")
    
    # Xử lý đường dẫn (hỗ trợ cả tương đối và tuyệt đối)
    if not path.startswith("/"):
        full_path = os.path.expanduser(f"~/{path}")
    else:
        full_path = path

    if os.path.exists(full_path) and os.path.isfile(full_path):
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                print("--- NỘI DUNG FILE ---")
                print(f.read())
                print("---------------------")
        except Exception as e:
            print(f"Lỗi khi đọc file: {e}")
    else:
        print("Thông báo: Tập tin không tồn tại.")

if __name__ == "__main__":
    read_content()
