#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def process_logs():
    input_file = "system.log"
    output_file = "urgent_errors.txt"
    
    # Tạo file mẫu nếu chưa có để test
    if not os.path.exists(input_file):
        with open(input_file, "w", encoding="utf-8") as f:
            f.write("INFO: System boot\nERROR: Disk failure\nINFO: User login\nWARNING: High memory\nERROR: Network down")

    error_count = 0
    warning_count = 0
    error_lines = []

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if "ERROR" in line.upper():
                error_count += 1
                error_lines.append(line)
            elif "WARNING" in line.upper():
                warning_count += 1

    # Ghi file lỗi khẩn cấp
    with open(output_file, "w", encoding="utf-8") as f_out:
        f_out.writelines(error_lines)

    print(f"Thống kê: {error_count} lỗi, {warning_count} cảnh báo.")
    if lines:
        print(f"Dòng cuối cùng: {lines[-1].strip()}")

if __name__ == "__main__":
    process_logs()

#Đọc file system.log.
#Đếm xem có bao nhiêu dòng chứa từ "ERROR" và bao nhiêu dòng chứa "WARNING".
#Trích xuất toàn bộ các dòng "ERROR" sang một file mới tên là urgent_errors.txt.
#In ra màn hình dòng cuối cùng của file log (tương tự lệnh tail -n 1).
