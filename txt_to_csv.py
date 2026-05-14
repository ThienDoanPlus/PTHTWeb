#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Yêu cầu: Chuyển đổi danh sách thông tin từ file văn bản thuần túy sang file CSV để dễ quản lý trong Excel.
#File nguồn danhba.txt: HoTen:SoDienThoai (Ví dụ: An:0909123...)
#File đích danhba.csv: Có tiêu đề cột Tên và Số điện thoại.
import csv
import os

def convert():
    txt_file = "danhba.txt"
    csv_file = "danhba.csv"

    if not os.path.exists(txt_file):
        with open(txt_file, "w") as f: f.write("Binh:0123\nChi:0456\nDat:0789")

    data_to_convert = []
    
    # 1. Đọc Text và xử lý chuỗi (Chương 4 - Slide 38)
    with open(txt_file, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                parts = line.strip().split(":")
                data_to_convert.append(parts)

    # 2. Ghi vào CSV (Chương xử lý CSV)
    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Tên", "Số điện thoại"]) # Ghi tiêu đề
        writer.writerows(data_to_convert)

    print(f"Chuyển đổi thành công {len(data_to_convert)} liên hệ sang CSV.")

if __name__ == "__main__":
    convert()
