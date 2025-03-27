import os

# Đường dẫn đến thư mục chứa các tệp .tex
folder_path = "chapters"  # Thay bằng đường dẫn thực tế

# Lặp qua các số chương từ 33 đến 40
for old_num in range(33, 41):
    old_name = f"chapter{old_num}.tex"
    new_name = f"chapter{old_num + 4}.tex"

    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)

    # Kiểm tra xem file cũ có tồn tại không
    if os.path.exists(old_path):
        # Nếu file mới đã tồn tại, đổi tên khác hoặc bỏ qua
        if os.path.exists(new_path):
            print(f"⚠️ File {new_name} đã tồn tại, bỏ qua {old_name}.")
        else:
            os.rename(old_path, new_path)
            print(f"✅ Đã đổi tên {old_name} thành {new_name}.")
    else:
        print(f"❌ Không tìm thấy {old_name}.")
