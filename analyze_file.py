import os

file_name = input("Nhap ten tap tin muon doc: ")
if not os.path.exists(file_name):
    print("Loi: Tap tin khong ton tai!")
else:
    try:
        n = int(input("Nhap so dong n muon hien thi: "))
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        num_lines = len(lines)
        all_text = "".join(lines)
        num_words = len(all_text.split())
        # Sửa dòng này để tránh lỗi Syntax:
        num_chars_no_space = len(all_text.replace(" ", "").replace("\n", "").replace("\t", ""))

        print(f"\n--- {n} dong dau tien ---")
        for line in lines[:n]:
            print(line.strip())

        # Ghi ket qua
        with open("ketqua.txt", "w", encoding='utf-8') as res:
            res.write("Thong tin tap tin " + file_name + "\n")
            res.write("So luong dong: " + str(num_lines) + " dong\n")
            res.write("So luong tu: " + str(num_words) + " tu\n")
            res.write("So ky tu (khong khoang trang): " + str(num_chars_no_space) + " ky tu\n")
            res.write(str(n) + " dong dau tien cua file " + file_name + "\n")
            res.write("Noi dung:\n")
            for line in lines[:n]:
                res.write(line)
        print("\nDa luu ket qua vao ketqua.txt")
    except ValueError:
        print("Loi: n phai la mot so nguyen!")

# ./backup.sh
# python3 analyze_file.py
