#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

file_name = input("Nhap ten tap tin muon doc: ")
if not os.path.exists(file_name):
    print("Loi: Tap tin khong ton tai!")
else:
    try:
        n = int(input("Nhap so dong n muon hien thi: "))
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        num_lines = len(lines)
        all_text = "".join(lines)
        num_words = len(all_text.split())
        # Loại bỏ tất cả các loại khoảng trắng (space, tab, newline)
        num_chars_no_space = len(all_text.replace(" ", "").replace("\n", "").replace("\t", ""))

        # Điều chỉnh n nếu n lớn hơn tổng số dòng
        dong_thuc_te = n if n <= num_lines else num_lines

        print(f"\n--- {dong_thuc_te} dong dau tien ---")
        for line in lines[:dong_thuc_te]:
            print(line.strip())

        # Ghi ket qua vào file sử dụng f-string cho chuyên nghiệp
        with open("ketqua.txt", "w", encoding='utf-8') as res:
            res.write(f"Thong tin tap tin {file_name}\n")
            res.write(f"So luong dong: {num_lines} dong\n")
            res.write(f"So luong tu: {num_words} tu\n")
            res.write(f"So ky tu (khong khoang trang): {num_chars_no_space} ky tu\n")
            res.write(f"{dong_thuc_te} dong dau tien cua file {file_name}\n")
            res.write("Noi dung:\n")
            for line in lines[:dong_thuc_te]:
                res.write(line)
                
        print("\nDa luu ket qua vao ketqua.txt")
    except ValueError:
        print("Loi: n phai la mot so nguyen!")

# ./backup.sh
# python3 analyze_file.py
