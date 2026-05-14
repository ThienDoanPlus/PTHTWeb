#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Yêu cầu: Bạn có file kho_hang.csv với cấu trúc: TenSP, SoLuong, DonGia.
#Tính Tổng giá trị của từng mặt hàng (SoLuong * DonGia).
#Tìm mặt hàng có Tổng giá trị lớn nhất.
#Ghi kết quả vào file bao_cao_kho.txt theo định dạng: Tên SP - Tổng giá trị.

import csv
import os

def report_inventory():
    csv_file = "kho_hang.csv"
    
    # Tạo dữ liệu mẫu
    if not os.path.exists(csv_file):
        with open(csv_file, "w", encoding="utf-8") as f:
            f.write("TenSP,SoLuong,DonGia\nLaptop,5,1500\nMouse,50,20\nMonitor,10,200")

    max_val = 0
    max_sp = ""
    results = []

    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total = int(row['SoLuong']) * float(row['DonGia'])
            results.append(f"{row['TenSP']} - {total}")
            
            if total > max_val:
                max_val = total
                max_sp = row['TenSP']

    with open("bao_cao_kho.txt", "w", encoding="utf-8") as f_out:
        f_out.write("--- BAO CAO TONG GIA TRI ---\n")
        for line in results:
            f_out.write(line + "\n")
        f_out.write(f"\nMat hang gia tri nhat: {max_sp} ({max_val})")

    print("Đã xuất báo cáo kho hàng.")

if __name__ == "__main__":
    report_inventory()
