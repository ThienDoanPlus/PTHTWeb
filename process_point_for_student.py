#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import os

def process_grades():
    input_file = 'sinhvien.csv'
    output_file = 'bang_diem.txt'
    
    if not os.path.exists(input_file):
        print(f"Khong tim thay file {input_file}")
        return

    results = []

    # 1. Doc file CSV
    with open(input_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f) # Doc theo kieu Dictionary voi key la tieu de cot
        for row in reader:
            hoten = row['HoTen']
            # Chuyen doi kieu du lieu de tinh toan
            dtb = (float(row['DiemLT']) + float(row['DiemTH'])) / 2
            ketqua = "Dat" if dtb >= 5 else "Khong dat"
            
            results.append(f"{hoten} - {dtb:.1f} - {ketqua}")

    # 2. Ghi ra file TXT
    with open(output_file, mode='w', encoding='utf-8') as f:
        f.write("--- BANG DIEM TONG HOP ---\n")
        for line in results:
            f.write(line + "\n")
            
    print(f"Da xu ly xong {len(results)} sinh vien. Xem tai {output_file}")

if __name__ == "__main__":
    process_grades()


#echo "MSSV,HoTen,DiemLT,DiemTH 001,Nguyen An,8,9 002,Tran Binh,4,3 003,Le Chi,6,7" > sinhvien.csv
