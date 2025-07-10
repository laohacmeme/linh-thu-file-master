import os
import shutil
from tkinter import Tk, filedialog, Button, Label, messagebox

# Phân loại theo phần mở rộng
FILE_TYPES = {
    'Ảnh': ['.jpg', '.jpeg', '.png', '.gif'],
    'Video': ['.mp4', '.mov', '.avi'],
    'Tài liệu': ['.pdf', '.docx', '.txt'],
    'Khác': []
}

def classify_and_rename(folder_path):
    count_map = {}

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1].lower()
            moved = False

            for type_name, extensions in FILE_TYPES.items():
                if ext in extensions:
                    target_folder = os.path.join(folder_path, type_name)
                    os.makedirs(target_folder, exist_ok=True)
                    count_map.setdefault(type_name, 0)
                    count_map[type_name] += 1

                    new_name = f"{type_name}_{count_map[type_name]:03d}{ext}"
                    shutil.move(full_path, os.path.join(target_folder, new_name))
                    moved = True
                    break

            if not moved:
                target_folder = os.path.join(folder_path, 'Khác')
                os.makedirs(target_folder, exist_ok=True)
                count_map.setdefault('Khác', 0)
                count_map['Khác'] += 1

                new_name = f"Khac_{count_map['Khác']:03d}{ext}"
                shutil.move(full_path, os.path.join(target_folder, new_name))

    messagebox.showinfo("Hoàn tất", "Đã phân loại và đổi tên thành công!")

def choose_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        classify_and_rename(folder_selected)

# GUI
root = Tk()
root.title("Linh Thư File Master")
root.geometry("400x200")

Label(root, text="Phân loại & đổi tên file tự động", font=("Arial", 14)).pack(pady=20)
Button(root, text="Chọn thư mục", command=choose_folder, font=("Arial", 12)).pack()

root.mainloop()
