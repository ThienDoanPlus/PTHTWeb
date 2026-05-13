import os

def xu_ly():
    f1_name = "file1.txt"
    f2_name = "file2.txt"
    
    if not os.path.exists(f1_name) or not os.path.exists(f2_name):
        print("Loi: Thieu file dau vao (file1.txt hoac file2.txt)")
        return

    # 1. Doc noi dung 2 file
    with open(f1_name, 'r', encoding='utf-8') as f1:
        content1 = f1.read().split() # Tach thanh ds cac tu
    
    with open(f2_name, 'r', encoding='utf-8') as f2:
        content2 = f2.read().split()

    # 2. Tim tu co trong file 1 ma khong co trong file 2
    # Su dung List Comprehension de loc
    unique_words = [word for word in content1 if word not in content2]
    result_string = " ".join(unique_words)

    # 3. Tinh toan thong so
    num_words = len(unique_words)
    # Loai bo khoang trang de dem ky tu
    num_chars = len(result_string.replace(" ", ""))

    # 4. Ghi ket qua vao ketqua.txt theo dinh dang
    with open("ketqua.txt", "w", encoding='utf-8') as res:
        res.write("--- Ket qua so sanh file ---\n")
        res.write(f"Chuoi tim duoc: {result_string}\n")
        res.write(f"So luong tu: {num_words} tu\n")
        res.write(f"So ky tu (khong khoang trang): {num_chars} ky tu\n")

    print("Da xu ly xong. Vui long kiem tra file ketqua.txt")

if __name__ == "__main__":
    xu_ly()

#chmod +x tinh_tong.sh
#chmod +x folder_manager.sh
#./tinh_tong.sh 2 4 5 7 8 10
#cat tong.txt
#./folder_manager.sh
#python3 so_sanh.py
#Tao file file1.txt
#Tao file file2.txt
#cat ketqua.txt
