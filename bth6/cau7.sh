#!/bin/bash
echo "CHUONG TRINH BE LAM TOAN"
echo "1- Be lam toan cong"
echo "2- Be lam toan tru"
echo "3- Be lam toan nhan"
echo "4- Be lam toan chia"
echo "0- Thoat chuong trinh"
read -p "Chon chuc nang: " chon

if [ $chon -eq 0 ]; then exit; fi

read -p "Nhap so thu nhat: " a
read -p "Nhap so thu hai: " b

case $chon in
    1) echo "Ket qua: $((a + b))" ;;
    2) echo "Ket qua: $((a - b))" ;;
    3) echo "Ket qua: $((a * b))" ;;
    4) echo "Ket qua: $(echo "scale=2; $a / $b" | bc)" ;;
    *) echo "Chon sai!" ;;
esac
