import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import zipfile
import threading
import configparser
import re
import shutil

class handOperateApp:
    def __init__(self, root):
        self.root = root  # root를 인스턴스 변수로 저장
        self.config = configparser.ConfigParser()
        self.config_file = 'settings.ini'
        self.load_settings()

        root.title("수동 취합 프로그램")
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
        # root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def build_ui(self, root):
        self.label_frame = ttk.LabelFrame(root, text="설정")
        self.label_frame.pack(padx=10, pady=10, fill="x", expand=True)

        self.folder_path = tk.StringVar(value=self.config['DEFAULT'].get('folder_path', ''))
        ttk.Label(self.label_frame, text="수동 취합할 폴더").pack(anchor='w')
        self.folder_entry = ttk.Entry(self.label_frame, textvariable=self.folder_path)
        self.folder_entry.pack(fill="x")
        ttk.Button(self.label_frame, text="선택...", command=self.select_folder).pack(pady=5)

        self.output_path = tk.StringVar(value=self.config['DEFAULT'].get('output_path', ''))
        ttk.Label(self.label_frame, text="출력 경로").pack(anchor='w')
        self.output_entry = ttk.Entry(self.label_frame, textvariable=self.output_path)
        self.output_entry.pack(fill="x")
        ttk.Button(self.label_frame, text="선택...", command=self.select_output_folder).pack(pady=5)

        self.file_name = tk.StringVar(value=self.config['DEFAULT'].get('file_name', ''))
        ttk.Label(self.label_frame, text="압축 파일 이름").pack(anchor='w')
        self.file_name_entry = ttk.Entry(self.label_frame, textvariable=self.file_name)
        self.file_name_entry.pack(fill="x")

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(root, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(padx=10, pady=10, fill="x")

        ttk.Button(root, text="수동 취합 시작", command=self.start_handOperate).pack(pady=20)

    def select_folder(self):
        folder_path = filedialog.askdirectory(title="수동 취합할 폴더 선택", initialdir=self.folder_path.get())
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

    def handOperate_folder(self, folder_path, output_path, file_name):
        # 변수 선언
        sqlitedb = "/systemdb/system"
        auxFunc = "/AuxFunction"
        # binroot = "/BIN"

        sqlitedbList = ['ECU_mapping.sqlite', 'SoftwareInformation.sqlite', 'SpecialFunction.sqlite', 'GDSN_AUXmultilanguage.sqlite', 'GDSNmultilanguage.sqlite', 'GDSMultilanguage_CV.sqlite']
        auxFuncList = ['ECUMapping.git', 'ECUMapping.gwm']
        # binrootList = ['VCI1', 'VCI2', 'VCI2W', 'VMI1', 'TPMS', 'TPMS_NEW']

        dirList = []
        fileList_sqlitedb_all = []
        fileList_auxFunc_all = []
        fileList_sqlitedb = []
        fileList_auxFunc = []
        fileList_TF = []

        # 원본 폴더 복사
        src1 = folder_path
        dst1 = output_path+'/Resource'
        shutil.copytree(src1, dst1)

        for (root, dirs, files) in os.walk(folder_path):
            dirList.append(dirs)
        # print(dirList)

        # SYSTEM
        # sqlite
        if "systemdb" in dirList[0]:
            for (root, dirs, files) in os.walk(folder_path+sqlitedb):
                fileList_sqlitedb_all.append(files)
            for i in range(0, len(fileList_sqlitedb_all[0])):
                if fileList_sqlitedb_all[0][i] in sqlitedbList :
                    fileList_TF.append('True')
                    fileList_sqlitedb.append(fileList_sqlitedb_all[0][i])
            # print(fileList_sqlitedb)
            if 'True' in fileList_TF:
                os.makedirs(output_path+'/Resource'+'/system/'+sqlitedb)

            for i in range(0, len(fileList_sqlitedb)):
                src2 = dst1+'/'+sqlitedb+'/'+fileList_sqlitedb[i]
                dst2 = output_path+'/Resource'+'/system/'+sqlitedb
                shutil.move(src2, dst2)
            # 빈파일 삭제
            for (root, dirs, files) in os.walk(output_path+'/Resource/'+sqlitedb):
                if not dirs:
                    if not files:
                        shutil.rmtree(output_path+'/Resource/'+sqlitedb)
        else :
            pass
        # AuxFunction
        if "AuxFunction" in dirList[0]:
            for (root, dirs, files) in os.walk(folder_path+auxFunc):
                fileList_auxFunc_all.append(files)
            # print(fileList_auxFunc_all[0])
            for i in range(0, len(fileList_auxFunc_all[0])):
                if fileList_auxFunc_all[0][i] in auxFuncList :
                    os.makedirs(output_path+'/Resource'+'/system/'+auxFunc)
                    fileList_auxFunc.append(fileList_auxFunc_all[0][i])

            for i in range(0, len(fileList_auxFunc)):
                src3 = dst1+'/'+auxFunc+'/'+fileList_auxFunc[i]
                dst3 = output_path+'/Resource'+'/system/'+auxFunc
                shutil.move(src3, dst3)
            # 빈파일 삭제
            for (root, dirs, files) in os.walk(output_path+'/Resource/'+auxFunc):
                if not dirs:
                    if not files:
                        shutil.rmtree(output_path+'/Resource/'+auxFunc)
        else :
            pass

        # RESOURCE
        # os.makedirs(output_path+'/Resource/')
        os.makedirs(output_path+'/'+file_name)
        src4 = dst1
        dst4 = output_path+'/'+file_name
        shutil.move(src4, dst4)
        shutil.move(dst4+'/Resource'+'/system', dst4)

        self.root.after(0, self.reset_ui)  # Ensure UI reset is called in the main thread

    def reset_ui(self):
        # Reset UI elements to be editable after compression is complete
        self.folder_entry.config(state='normal')
        self.output_entry.config(state='normal')
        # self.max_size_entry.config(state='normal')
        self.file_name_entry.config(state='normal')
        messagebox.showinfo("압축 완료", "수동 취합이 완료되었습니다.")
        self.progress_var.set(0)  # Reset progress bar

    def start_handOperate(self):
        # 입력 필드 수정 불가능하게 설정
        self.folder_entry.config(state='disabled')
        self.output_entry.config(state='disabled')
        # self.max_size_entry.config(state='disabled')
        self.file_name_entry.config(state='disabled')

        # 작업 시작
        folder_path = self.folder_path.get()
        output_path = self.output_path.get()
        file_name = self.file_name.get()

        threading.Thread(target=self.handOperate_folder, args=(folder_path, output_path, file_name),
                         daemon=True).start()

    def load_settings(self):
        self.config.read(self.config_file)

    def save_settings(self):
        self.config['DEFAULT'] = {
            'folder_path': self.folder_path.get(),
            'output_path': self.output_path.get(),
            # 'max_size_mb': self.max_size_mb.get(),
            'file_name': self.file_name.get(),
        }
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def on_closing(self):
        self.save_settings()
        self.root.destroy()

root = tk.Tk()
app = handOperateApp(root)
root.mainloop()