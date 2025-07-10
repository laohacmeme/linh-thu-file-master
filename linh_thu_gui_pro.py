import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Setup theme
ctk.set_appearance_mode("System")  # "Dark", "Light", or "System"
ctk.set_default_color_theme("blue")

# File types
FILE_TYPES = {
    'Ảnh': ['.jpg', '.jpeg', '.png', '.gif'],
    'Video': ['.mp4', '.mov', '.avi'],
    'Tài liệu': ['.pdf', '.docx', '.txt'],
    'Khác': []
}

class FileMasterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Linh Thư File Master Pro")
        self.geometry("500x320")
        self.resizable(False, False)

        self.label = ctk.CTkLabel(self, text="🎀 Chọn thư mục để phân loại & đổi tên", font=("Arial", 18))
        self.label.pack(pady=20)

        self.select_btn = ctk.CTkButton(self, text="📁 Chọn thư mục", command=self.choose_folder)
        self.select_btn.pack(pady=10)

        self.folder_label = ctk.CTkLabel(self, text="", font=("Arial", 14), wraplength=400)
        self.folder_label.pack(pady=5)

        self.start_btn = ctk.CTkButton(self, text="🚀 Bắt đầu xử lý", command=self.process, state="disabled")
        self.start_btn.pack(pady=15)

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path = folder
            self.folder_label.configure(text=f"📂 {folder}")
            self.start_btn.configure(state="normal")

    def process(self):
        count_map = {}
        folder_path = self.folder_path

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

        messagebox.showinfo("Hoàn tất", "🎉 Đã phân loại và đổi tên thành công!")

if __name__ == "__main__":
    app = FileMasterApp()
    app.mainloop()
