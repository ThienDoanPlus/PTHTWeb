#!/bin/bash

OUT_DIR="$HOME/Desktop/MAX"
mkdir -p "$OUT_DIR"

# 1. Kiểm tra số lượng đối số (3 <= $# <= 5)
if [ $# -lt 3 ] || [ $# -gt 5 ]; then
    echo "Loi: Chi cho phep tinh tu 3 den 5 con so."
    exit 1
fi

tong=0
for diem in "$@"; do
    tong=$((tong + diem))
done

# 2. Tính trung bình dùng bc (để lấy số thập phân - Chương 3 slide 50, 51)
trungbinh=$(echo "scale=2; $tong / $#" | bc)

# 3. Ghi file
echo "Cac con diem da nhap: $@" > "$OUT_DIR/diem.txt"
echo "Tong diem: $tong" >> "$OUT_DIR/diem.txt"
echo "Diem trung binh: $trungbinh" >> "$OUT_DIR/diem.txt"

echo "Da ghi ket qua vao Desktop/MAX/diem.txt"
