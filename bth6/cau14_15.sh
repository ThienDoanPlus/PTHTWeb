#!/bin/bash
# Câu 14: Lay tu doi so
if [ $# -gt 0 ]; then
    folder=$1
else
    # Câu 15: Nhap tu ban phim
    read -p "Nhap ten thu muc muon tao: " folder
fi

if [ -d "$folder" ]; then
    echo "Thư mục đã tồn tại."
else
    mkdir "$folder"
    echo "Đã tạo thư mục thành công."
fi
