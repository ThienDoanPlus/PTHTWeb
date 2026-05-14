#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. Khai báo danh sách (Theo đề bài thực hành câu 7)
lst = ['Ca dao', 'Ca khong an muoi ca uong', 'Con cai cha me tram duong con hu']

# 2. Mở file với mode 'w' để ghi mới (Chương xử lý file)
file = open('cadao.txt', 'w', encoding='utf-8')

# 3. Vòng lặp ghi từng câu (Dựa trên cấu trúc vòng lặp for đã học)
for cau in lst:
    file.write(cau + "\n") # Thêm \n để xuống dòng theo yêu cầu

# 4. Đóng file (Bắt buộc theo tài liệu)
file.close()

print("Da luu danh sach vao file cadao.txt thanh cong.")
