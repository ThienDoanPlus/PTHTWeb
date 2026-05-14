#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Nhập tên một file văn bản từ bàn phím.
#Đếm số dòng, số từ, số ký tự.
#Ghi các thông số thống kê này vào một file mới tên là thongke_file.txt.

import os

# 1. Nhập tên file từ bàn phím
fname = input("Nhap ten file can thong ke: ")

if os.path.exists(fname):
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
        
        # 2. Tính toán (Chương xử lý file)
        # Tách theo dấu xuống dòng để đếm dòng
        lines = content.splitlines()
        # Tách theo khoảng trắng để đếm từ
        words = content.split()
        # Đếm ký tự (bao gồm cả khoảng trắng)
        chars = len(content)

    # 3. Ghi kết quả vào file thongke_file.txt (Mode 'w')
    with open("thongke_file.txt", "w", encoding="utf-8") as f_out:
        f_out.write(f"Thong ke cho file: {fname}\n")
        f_out.write(f"So luong dong: {len(lines)}\n")
        f_out.write(f"So luong tu: {len(words)}\n")
        f_out.write(f"So luong ky tu: {chars}\n")
    
    print("Da thuc hien thong ke va luu vao thongke_file.txt")
else:
    print("Loi: Tap tin khong ton tai.")
