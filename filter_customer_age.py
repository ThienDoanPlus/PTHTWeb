#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

def process():
    input_file = "khachhang.txt"
    output_file = "nguoilon.txt"
    current_year = 2024

    # Kiểm tra file tồn tại
    if not os.path.exists(input_file):
        print(f"Lỗi: Không tìm thấy tập tin nguồn '{input_file}'", file=sys.stderr)
        return

    adults = []

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or "-" not in line:
                    continue
                
                # Tách tên và năm sinh
                parts = line.split("-")
                name = parts[0].strip()
                
                try:
                    birth_year = int(parts[1].strip())
                    # Tính tuổi và lọc >= 18 tuổi
                    if (current_year - birth_year) >= 18:
                        # Đếm số lượng từ trong tên
                        word_count = len(name.split())
                        adults.append(f"{name} - {word_count} tu")
                except ValueError:
                    print(f"Bỏ qua dòng lỗi định dạng năm sinh: {line}")

        # Ghi kết quả ra file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("--- DANH SACH NGUOI LON (>=18 TUOI) ---\n")
            for item in adults:
                f.write(item + "\n")
        
        print(f"Xử lý thành công! Đã lưu {len(adults)} người vào '{output_file}'.")

    except Exception as e:
        print(f"Đã xảy ra lỗi hệ thống: {e}", file=sys.stderr)

if __name__ == "__main__":
    process()
    
#echo -e "Nguyen Van An - 1990\nTran Thi Bich - 2010\nLe Van Cuong - 2005" > khachhang.txt
