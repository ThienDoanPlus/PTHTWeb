import os

def analyze():
    fin = "input.txt"
    fout = "report.txt"
    
    if not os.path.exists(fin):
        print(f"Loi: Khong tim thay file {fin}")
        return

    found_lines = []
    
    # 1. Doc va loc dong chua "Error"
    with open(fin, 'r', encoding='utf-8') as f:
        for line in f:
            if "error" in line.lower(): # .lower() de khong phan biet hoa thuong
                found_lines.append(line.strip())

    # 2. Xu ly thong ke tren cac dong tim duoc
    all_text = " ".join(found_lines)
    num_words = len(all_text.split())
    num_chars = len(all_text.replace(" ", ""))

    # 3. Ghi ket qua
    with open(fout, 'w', encoding='utf-8') as res:
        res.write("--- BAO CAO LOI HE THONG ---\n")
        res.write(f"So dong loi tim thay: {len(found_lines)}\n")
        res.write(f"Tong so tu trong cac dong loi: {num_words}\n")
        res.write(f"Tong so ky tu (khong khoang trang): {num_chars}\n")
        res.write("-" * 30 + "\n")
        res.write("Chi tiet cac dong loi:\n")
        for l in found_lines:
            res.write(f"- {l}\n")

    print(f"Da trich xuat {len(found_lines)} dong loi vao {fout}")

if __name__ == "__main__":
    analyze()
#echo -e "System start\nError: Disk full\nWarning: high temp\nERROR: CPU overload" > input.txt

#chmod +x tinh_le.sh system_tool.sh
#./tinh_le.sh 1 2 3 4 5
#./system_tool.sh
#python3 filter_error.py
