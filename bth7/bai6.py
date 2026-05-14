#!/usr/bin/env python3
import os

def bulk_create():
    base_name = input("Nhập tên tập tin (ví dụ: taptin): ")
    try:
        soluong = int(input("Nhập số lượng file muốn tạo: "))
        
        for i in range(10, 10 + soluong):
            fname = f"{base_name}{i}.txt"
            # Tạo file rỗng
            with open(fname, 'w') as f:
                pass 
            print(f"Đã tạo: {fname}")
    except ValueError:
        print("Lỗi: Số lượng phải là số nguyên.")

if __name__ == "__main__":
    bulk_create()
