!/usr/bin/env python3
import os
import sys

def check():
    # Kiểm tra xem có truyền đối số vào không
    if len(sys.argv) < 2:
        print("Vui lòng truyền đường dẫn làm đối số.")
        return

    path = sys.argv[1]

    # Câu 1: Kiểm tra thư mục
    if os.path.isdir(path):
        print(f"Thư mục '{path}' DA TON TAI.")
    # Câu 2: Kiểm tra tập tin
    elif os.path.isfile(path):
        print(f"Tập tin '{path}' DA TON TAI.")
    else:
        print(f"Đường dẫn '{path}' KHONG ton tai.")

if __name__ == "__main__":
    check()
