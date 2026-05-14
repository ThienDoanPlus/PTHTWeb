#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#echo "MSSV,HoTen,Khoa
#234,Nguyen Binh,CNTT
#235,Le Van Tam,CNTT
#876,Nguyen Thi Be,Ke toan" > sinhvien.csv
import csv

# 1. Mở file CSV (Theo mẫu Cách 1 trong bài thực hành CSV)
with open('sinhvien.csv', 'r', encoding='utf-8') as f:
    # 2. Đọc file bằng csv.reader
    reader = csv.reader(f)
    
    print("Danh sach ho ten sinh vien:")
    # 3. Duyệt từng dòng và in cột thứ 2 (col[1])
    for col in reader:
        # Bỏ qua dòng tiêu đề nếu cần, hoặc in tất cả
        print(col[1])
