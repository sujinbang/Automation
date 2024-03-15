import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import zipfile
import threading
import configparser
import re

class CompressApp:
    def __init__(self, root):
        self.root = root  # root를 인스턴스 변수로 저장
        self.config = configparser.ConfigParser()
        self.config_file = 'settings.ini'
        self.load_settings()

        root.title("분할 압축 프로그램")
        root.geometry("400x500")  # 높이 조정

        # 화면 가운데 위치
        window_width = 400
        window_height = 500  # 높이 조정
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        self.build_ui(root)
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def build_ui(self, root):
        self.label_frame = ttk.LabelFrame(root, text="설정")
        self.label_frame.pack(padx=10, pady=10, fill="x", expand=True)

        self.folder_path = tk.StringVar(value=self.config['DEFAULT'].get('folder_path', ''))
        ttk.Label(self.label_frame, text="압축할 폴더:").pack(anchor='w')
        self.folder_entry = ttk.Entry(self.label_frame, textvariable=self.folder_path)
        self.folder_entry.pack(fill="x")
        ttk.Button(self.label_frame, text="선택...", command=self.select_folder).pack(pady=5)

        self.output_path = tk.StringVar(value=self.config['DEFAULT'].get('output_path', ''))
        ttk.Label(self.label_frame, text="출력 경로:").pack(anchor='w')
        self.output_entry = ttk.Entry(self.label_frame, textvariable=self.output_path)
        self.output_entry.pack(fill="x")
        ttk.Button(self.label_frame, text="선택...", command=self.select_output_folder).pack(pady=5)

        self.max_size_mb = tk.StringVar(value=self.config['DEFAULT'].get('max_size_mb', ''))
        ttk.Label(self.label_frame, text="최대 크기(MB):").pack(anchor='w')
        self.max_size_entry = ttk.Entry(self.label_frame, textvariable=self.max_size_mb)
        self.max_size_entry.pack(fill="x")

        self.file_name = tk.StringVar(value=self.config['DEFAULT'].get('file_name', ''))
        ttk.Label(self.label_frame, text="압축 파일 이름:").pack(anchor='w')
        self.file_name_entry = ttk.Entry(self.label_frame, textvariable=self.file_name)
        self.file_name_entry.pack(fill="x")

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(root, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(padx=10, pady=10, fill="x")

        ttk.Button(root, text="압축 시작", command=self.start_compression).pack(pady=20)

    def select_folder(self):
        folder_path = filedialog.askdirectory(title="압축할 폴더 선택", initialdir=self.folder_path.get())
        if folder_path:
            self.folder_path.set(folder_path)

    def select_output_folder(self):
        output_path = filedialog.askdirectory(title="출력 경로 선택", initialdir=self.output_path.get())
        if output_path:
            self.output_path.set(output_path)

    def update_progress(self, processed, total):
        progress = (processed / total) * 100
        self.progress_var.set(progress)
        self.root.update_idletasks()  # root 대신 self.root 사용

    def compress_folder(self, folder_path, output_path, max_size, file_name):
        total_size = sum([os.path.getsize(os.path.join(dirpath, filename))
                          for dirpath, _, filenames in os.walk(folder_path)
                          for filename in filenames])
        processed_size = 0

        if len(file_name.split('-')[0]) == 3:
            date_part = file_name.split('-')[-3]
            file_version = file_name.split('-')[0] + '-' + file_name.split('-')[1] + '-' + file_name.split('-')[2]
            last_file = file_name.split('-')[-2] + '-' + file_name.split('-')[-1] + '.zip'
        
        else :
            date_part = file_name.split('-')[-3]
            file_version = file_name.split('-')[0] + '-' + file_name.split('-')[1] + '-' + file_name.split('-')[2] + '-' + file_name.split('-')[3] + '-' + file_name.split('-')[4] + '-' + file_name.split('-')[5]
            last_file = file_name.split('-')[-2] + '-' + file_name.split('-')[-1] + '.zip'

        zip_counter = 1
        new_file_name = file_version + '-'+ date_part + '-' + last_file
        zip_file_name = f"{output_path}/{new_file_name}"
        # zip_file_name = f"{output_path}/{file_name}{zip_counter:02d}.zip"
        zip_file = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)

        for foldername, _, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zip_file.write(file_path, os.path.relpath(file_path, folder_path))
                file_size = os.path.getsize(file_path)
                processed_size += file_size
                self.update_progress(processed_size, total_size)

                # Check if the current zip part exceeds the maximum size and start a new part if needed
                if zip_file.fp.tell() + file_size > max_size:

                    zip_file.close()
                    zip_counter += 1
                    if zip_counter < 100:
                        date_part_rep = date_part.replace(date_part[-2:], f"{zip_counter:02d}")
                        # zip_file_name = f"{output_path}/{file_name}{zip_counter:02d}.zip"
                    else:
                        date_part_rep = date_part.replace(date_part[-2:], f"{zip_counter:03d}")
                        # zip_file_name = f"{output_path}/{file_name}{zip_counter:03d}.zip"

                    new_file_name = file_version + '-'+ date_part_rep + '-' + last_file
                    zip_file_name = f"{output_path}/{new_file_name}"
                    zip_file = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)

        zip_file.close()
        self.root.after(0, self.reset_ui)  # Ensure UI reset is called in the main thread

    def reset_ui(self):
        # Reset UI elements to be editable after compression is complete
        self.folder_entry.config(state='normal')
        self.output_entry.config(state='normal')
        self.max_size_entry.config(state='normal')
        self.file_name_entry.config(state='normal')
        messagebox.showinfo("압축 완료", "분할 압축이 완료되었습니다.")
        self.progress_var.set(0)  # Reset progress bar

    def start_compression(self):
        # 입력 필드 수정 불가능하게 설정
        self.folder_entry.config(state='disabled')
        self.output_entry.config(state='disabled')
        self.max_size_entry.config(state='disabled')
        self.file_name_entry.config(state='disabled')

        # 압축 작업 시작
        folder_path = self.folder_path.get()
        output_path = self.output_path.get()
        max_size = int(self.max_size_mb.get()) * 1024 * 1024
        file_name = self.file_name.get()

        threading.Thread(target=self.compress_folder, args=(folder_path, output_path, max_size, file_name),
                         daemon=True).start()

    def load_settings(self):
        self.config.read(self.config_file)

    def save_settings(self):
        self.config['DEFAULT'] = {
            'folder_path': self.folder_path.get(),
            'output_path': self.output_path.get(),
            'max_size_mb': self.max_size_mb.get(),
            'file_name': self.file_name.get(),
        }
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def on_closing(self):
        self.save_settings()
        root.destroy()


root = tk.Tk()
app = CompressApp(root)
root.mainloop()