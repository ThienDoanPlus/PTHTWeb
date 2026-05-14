#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Yêu cầu: Viết script Python nhập vào tên một file văn bản từ bàn phím. Kiểm tra file có tồn tại không. Nếu có, đếm số dòng, số chữ và in ra màn hình.
import os

# 1. Nhập tên file từ bàn phím (Bài thực hành 7 - Câu 3)
fname = input("Nhap ten tap tin (.txt): ")

# 2. Kiểm tra tồn tại (Bài thực hành 7 - Câu 2)
if os.path.exists(fname):
    # 3. Mở file để đọc (Chương xử lý file text)
    with open(fname, "r", encoding="utf-8") as f:
        data = f.read()
        lines = data.split("\n")
        words = data.split()
        
        # 4. Xuất nội dung ra màn hình (Câu 6 bài thực hành Python)
        print("--- Noi dung file ---")
        print(data)
        print("--------------------")
        print("So dong:", len(lines))
        print("So chu:", len(words))
        print("So ky tu:", len(data))
else:
    print("Thong bao: Tap tin khong ton tai.")
