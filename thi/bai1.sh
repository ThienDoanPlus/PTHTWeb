#!/bin/bash

# 1. Định nghĩa đường dẫn lưu trữ theo yêu cầu (Desktop/MAX của user hiện tại)
DIR_PATH="$HOME/Desktop/MAX"
FILE="$DIR_PATH/max.txt"

# 2. Tạo thư mục nếu chưa có (-p để không báo lỗi nếu đã tồn tại)
mkdir -p "$DIR_PATH"

# 3. Ghi tiêu đề vào file (Dùng dấu > để làm mới file mỗi lần chạy)
echo "Chương trình tim so max" > "$FILE"
echo "=============================" >> "$FILE"

# 4. Kiểm tra số lượng đối số
if [ $# -lt 3 ]; then
    # Ghi thông báo không hợp lệ vào file theo yêu cầu của đề
    echo "So luong cac doi so duoc truyen vao: $# so. Khong hop le." >> "$FILE"
    
    # Thông báo ra màn hình terminal
    echo "Loi!! So luong doi so phai >= 3 (Hien tai chi co $#)"
    exit 1
fi

# 5. Nếu hợp lệ, tiến hành tìm MAX
echo "So luong cac doi so duoc truyen vao: $# so" >> "$FILE"

max=$1
for i in "$@"; do
    # Kiểm tra xem đối số có phải là số hay không (Senior touch)
    if [[ ! "$i" =~ ^-?[0-9]+$ ]]; then
        echo "Canh bao: '$i' khong phai la so, se bi bo qua."
        continue
    fi

    if [ "$i" -gt "$max" ]; then
        max=$i
    fi
done

# 6. Ghi kết quả cuối cùng vào file
echo "Vậy max la: $max" >> "$FILE"

echo "DONE. Ket qua da duoc luu tai: $FILE"
