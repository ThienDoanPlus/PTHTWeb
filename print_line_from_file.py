#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Sử dụng file tritue.txt đã tạo (có nội dung về Trí tuệ nhân tạo).
#Viết script Python để in ra màn hình dòng thứ 2 và dòng thứ 4 của file.
#Nếu file không đủ số dòng, thông báo cho người dùng.

import os

fname = "tritue.txt"

if os.path.exists(fname):
    with open(fname, "r", encoding="utf-8") as f:
        # Đọc tất cả các dòng vào một danh sách (readlines)
        lines = f.readlines()
        
        # Kiểm tra và in dòng thứ 2 (chỉ số 1)
        if len(lines) >= 2:
            print("Dong thu 2:", lines[1].strip())
        
        # Kiểm tra và in dòng thứ 4 (chỉ số 3)
        if len(lines) >= 4:
            print("Dong thu 4:", lines[3].strip())
        else:
            print("Thong bao: File khong co dong thu 4.")
else:
    print("Loi: File tritue.txt chua duoc tao.")
