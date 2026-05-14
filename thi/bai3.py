#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def process_text():
    # 1. Khai báo dữ liệu gốc
    nd = ("Cai trong truong em. Mua he cung nghi. Suot ba thang lien. "
          "Trong nam ngam nghi. Buon khong ha trong. Trong nhung ngay he. "
          "Bon minh di vang. Chi con tieng ve?")

    # 2. Xử lý ngắt dòng lần đầu (Dùng regex để tách theo cả . và ?)
    sentences = [s.strip() for s in re.split(r'([.?])', nd) if s.strip()]
    # Ghép lại cặp: nội dung + dấu câu
    formatted_nd = ""
    for i in range(0, len(sentences)-1, 2):
        formatted_nd += sentences[i] + sentences[i+1] + "\n"

    # Ghi file lần 1
    with open("baitho.txt", "w", encoding="utf-8") as f:
        f.write(formatted_nd.strip())

    # 3. Đọc và làm sạch dữ liệu (Data Cleaning)
    if os.path.exists("baitho.txt"):
        with open("baitho.txt", "r", encoding="utf-8") as f:
            content = f.read()

        # Loại bỏ từ "trong" (case-insensitive)
        content = re.sub(r'\btrong\b', '', content, flags=re.IGNORECASE)
        # Loại bỏ khoảng trắng thừa
        content = re.sub(r'\s{2,}', ' ', content)
        # Loại bỏ khoảng trắng trước dấu chấm, phẩy, hỏi
        content = re.sub(r'\s+([.,?])', r'\1', content).strip()
        
        # Format lại mỗi câu một dòng cho nội dung đã sạch
        lines_cleaned = [l.strip() for l in re.split(r'([.?])', content) if l.strip()]
        final_content = ""
        for i in range(0, len(lines_cleaned)-1, 2):
            final_content += lines_cleaned[i] + lines_cleaned[i+1] + "\n"

        # Ghi đè lại file baitho.txt
        with open("baitho.txt", "w", encoding="utf-8") as f:
            f.write(final_content)

    # 4. Thống kê (Chỉ mở file 1 lần để lấy mọi thông số)
    with open("baitho.txt", "r", encoding="utf-8") as f:
        data_lines = f.readlines()
        full_text = "".join(data_lines)
        
        so_luong_tu = len(full_text.split())
        # Cách đếm ký tự không khoảng trắng tối ưu nhất:
        so_ki_tu = len(re.sub(r'\s', '', full_text))
        so_dong = len(data_lines)

    # 5. Xuất kết quả
    thong_tin = (
        f"Thong tin sau khi xu ly:\n"
        f"{'='*39}\n"
        f"So luong tu: {so_luong_tu}\n"
        f"So ki tu (khong khoang trang): {so_ki_tu}\n"
        f"So dong: {so_dong}\n"
        f"{'='*39}\n"
    )
    
    with open("ketqua.txt", "w", encoding="utf-8") as f:
        f.write(thong_tin)
    
    print("Xử lý hoàn tất. Kiểm tra baitho.txt và ketqua.txt")

if __name__ == "__main__":
    process_text()
