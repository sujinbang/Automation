import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import zipfile
import threading
import configparser
import re
import shutil

# 변수 선언 : 3세대
App = "\\Application"
App_txt = "\\Application_Version.txt"
Critical = "\\Critical"
Critical_txt = "\\Critical_Version.txt"
Diagnosis = "\\Diagnosis"
Diagnosis_txt = "\\Diagnosis_Version.txt"
Diagnosis_CV = "\\Diagnosis_CV"
Diagnosis_CV_txt = "\\Diagnosis_CV_Version.txt"
ECU = "\\ECU"
ECU_txt = "\\ECU_Version.txt"
ECU_CV = "\\ECU_CV"
ECU_CV_txt = "\\ECU_CV_Version.txt"
Sys = "\\system"
Sys_txt = "\\System_Version.txt"

# 변수 선언 : 4세대
Rsc = "\\Resource"
Rsc_txt = "\\Resource_Version.txt"
SupportApp = "\\SupportApp"
SupportApp_txt = "\\SupportApp_Version.txt"

# 변수 선언 : Gscan
app = "\\application"
app_txt = "\\application_version.txt"
critical = "\\critical"
critical_txt = "\\critical_version.txt"
diagnosis = "\\diagnosis"
diagnosis_txt = "\\diagnosis_version.txt"
diagnosis_cv = "\\diagnosis_cv"
diagnosis_cv_txt = "\\diagnosis_cv_version.txt"
diagnosis_im = "\\diagnosis_im"
diagnosis_im_txt = "\\diagnosis_im_version.txt"
gscan_os = "\\os"
gscan_os_txt = "\\os_version.txt"
system = "\\system"
sys_txt = "\\system_version.txt"


class rename_3:
    # 화면 가운데 위치
    def __init__(self, window1):
        window1.title("3세대 파일명 변경 프로그램")
        # window1.geometry("400x700")
        window1_width = 400
        window1_height = 700  # 높이 조정
        screen_width = window1.winfo_screenwidth()
        screen_height = window1.winfo_screenheight()
        center_x = int(screen_width / 2 - window1_width / 2)
        center_y = int(screen_height / 2 - window1_height / 2)
        window1.geometry(f"{window1_width}x{window1_height}+{center_x}+{center_y}")

        self.build_ui(window1)

    def build_ui(self, window1):
        # 파일 경로 입력
        self.label_title=Label(window1, text="*** 3세대 파일명 변경 프로그램 입니다 ***", fg="green", relief="groove")
        self.label_title.pack(fill='x', padx=5, pady=5)

        self.label_frame1 = ttk.LabelFrame(window1, text="설정")
        self.label_frame1.pack(padx=10, pady=10, fill="x", expand=True)

        # 파일 경로 입력
        self.label1=tk.Label(self.label_frame1, text="[Step 1] 파일 경로를 입력하세요")
        self.label1.pack(fill='x', padx=5, pady=5)

        self.entry_filePath=ttk.Entry(self.label_frame1, width=50, justify="center")
        self.entry_filePath.pack(fill='x', padx=5, pady=5)

        # 텍스트
        self.label2=tk.Label(self.label_frame1, text="[Step 2] 항목을 선택하세요")
        self.label2.pack(fill='x', padx=5, pady=5)

        # 항목값
        self.selected_item = tk.StringVar()
        items = (('Application', '1'),
                ('Critical', '2'),
                ('Diagnosis', '3'),
                ('Diagnosis_CV', '4'),
                ('ECU', '5'),
                ('ECU_CV', '6'),
                ('System', '7'))        

        # 라디오 버튼을 팩에 배치
        for item in items:
            r = ttk.Radiobutton(
                self.label_frame1,
                text=item[0],
                value=item[1],
                variable=self.selected_item
            )
            # 팩에 배치
            r.pack(padx=5, pady=5)

        # new file명 입력
        self.label3=tk.Label(self.label_frame1, text="[Step 3] 바꿀 파일명을 입력하세요")
        self.label3.pack(fill='x', padx=5, pady=5)

        self.entry_newName=ttk.Entry(self.label_frame1, width=50, justify="center")
        self.entry_newName.pack(fill='x', padx=5, pady=5)

        # 버튼
        btn_Rename = ttk.Button(self.label_frame1, text = "파일명 변경", command = self.Rename)
        btn_Rename.pack(fill='x', padx=5, pady=5)

        # new file명 입력
        self.label3=tk.Label(self.label_frame1, text="[Step 4] 버전을 확인하세요")
        self.label3.pack(fill='x', padx=5, pady=5)

        btn_versionCheck = ttk.Button(self.label_frame1, text = "버전 확인", command = self.VersionCheck)
        btn_versionCheck.pack(fill='x', padx=5, pady=5)

        # 프레임
        self.frame = LabelFrame(self.label_frame1, text="결과")
        self.frame.pack(padx=5, pady=5, fill="x", expand=True)

        self.label4 = Label(self.frame)
        self.label4.pack(padx=0.01, pady=0.01)

        btn_cls = ttk.Button(self.label_frame1, text="초기화", command = self.clear_frame)
        btn_cls.pack(padx=5, pady=5)

    # 폴더명 변경

    ### Rename
    # Application
    def rename_app(self):
        # file_path
        file_path = self.entry_filePath.get()
        # new_name
        new_name = self.entry_newName.get()

        # 폴더명 추출
        for item in os.listdir(file_path+App):
            if '.txt' not in item :
                old_name = os.path.join(file_path+App, item) # 폴더경로 + 폴더명

        # txt 파일 변경
        txt_file = file_path+App+App_txt
        txt = open(txt_file, 'w')
        txt.write(new_name)

        new_name = file_path + App + "\\" + new_name
        os.rename(old_name, new_name)

    # Critical
    def rename_critical(self):
        # file_path
        file_path = self.entry_filePath.get()
        # new_name
        new_name = self.entry_newName.get()

        # txt 파일 변경
        txt_file = file_path+Critical+Critical_txt
        txt = open(txt_file, 'w')
        txt.write(new_name)

        # 폴더명 추출
        zip_files = []
        # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
        for root, dirs, files in os.walk(file_path+Critical):
            for file in files:
                if file.endswith('.zip'):
                    # 확장자가 .zip인 파일은 리스트에 추가
                    zip_files.append(os.path.join(file))

        zip_split = zip_files[0].split("-")
        # split_str_old = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]  # old_name은 split X
        split_str_new = zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1]  # new_name

        old_name = file_path + Critical + "\\" + zip_files[0]
        new_name = file_path + Critical + "\\" + new_name + "-" + split_str_new

        os.rename(old_name, new_name)

    # Diagnosis
    def rename_diag(self):
        # file_path
        file_path = self.entry_filePath.get()
        # new_name
        new_name = self.entry_newName.get()
        
        # txt 파일 변경
        txt_file = file_path+Diagnosis+Diagnosis_txt
        txt = open(txt_file, 'w')
        txt.write(new_name)

        # 폴더명 추출
        zip_files = []
        # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
        for root, dirs, files in os.walk(file_path+Diagnosis):
            for file in files:
                if file.endswith('.zip'):
                    # 확장자가 .zip인 파일은 리스트에 추가
                    zip_files.append(os.path.join(file))

        # ZIP 파일 목록 출력
        if len(zip_files) >= 2:
            split_str_new_list = []
            old_name = old_name = file_path + Diagnosis + "\\"
            new_name = file_path + Diagnosis + "\\" + new_name + "-"
            old_name_list = []
            new_name_list = []
            
            for i in range(0,len(zip_files)):
                zip_split = zip_files[i].split("-")
                # split_str_old = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]  # old_name은 split X
                split_str_new = zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1]  # new_name
                split_str_new_list.append(split_str_new)  
                old_name_list.append(old_name + zip_files[i])
                new_name_list.append(new_name + split_str_new_list[i])

            for i in range(0, len(old_name_list)):
                os.rename(old_name_list[i], new_name_list[i])

        elif len(zip_files) == 1:
            zip_split = zip_files[0].split("-")
            # split_str_old = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]  # old_name은 split X
            split_str_new = zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1]  # new_name

            old_name = file_path + Diagnosis + "\\" + zip_files[0]
            new_name = file_path + Diagnosis + "\\" + new_name + "-" + split_str_new

            os.rename(old_name, new_name)

    # Diagnosis_CV
    def rename_diag_CV(self):

        # file_path
        file_path = self.entry_filePath.get()
        # new_name
        new_name = self.entry_newName.get()

        # txt 파일 변경
        txt_file = file_path+Diagnosis_CV+Diagnosis_CV_txt
        txt = open(txt_file, 'w')
        txt.write(new_name)

        # 폴더명 추출
        zip_files = []
        # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
        for root, dirs, files in os.walk(file_path+Diagnosis_CV):
            for file in files:
                if file.endswith('.zip'):
                    # 확장자가 .zip인 파일은 리스트에 추가
                    zip_files.append(os.path.join(file))

        # ZIP 파일 목록 출력
        if len(zip_files) >= 2:
            split_str_new_list = []
            old_name = old_name = file_path + Diagnosis_CV + "\\"
            new_name = file_path + Diagnosis_CV + "\\" + new_name + "-"
            old_name_list = []
            new_name_list = []
            
            for i in range(0,len(zip_files)):
                zip_split = zip_files[i].split("-")
                # split_str_old = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]  # old_name은 split X
                split_str_new = zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1]  # new_name
                split_str_new_list.append(split_str_new)  
                old_name_list.append(old_name + zip_files[i])
                new_name_list.append(new_name + split_str_new_list[i])

            for i in range(0, len(old_name_list)):
                os.rename(old_name_list[i], new_name_list[i])

        elif len(zip_files) == 1:
            zip_split = zip_files[0].split("-")
            # split_str_old = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]  # old_name은 split X
            split_str_new = zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1]  # new_name

            old_name = file_path + Diagnosis_CV + "\\" + zip_files[0]
            new_name = file_path + Diagnosis_CV + "\\" + new_name + "-" + split_str_new

            os.rename(old_name, new_name)

    # ECU
    def rename_ECU(self):

        # file_path
        file_path = self.entry_filePath.get()
        # new_name
        new_name = self.entry_newName.get()

        # txt 파일 변경
        txt_file = file_path+ECU+ECU_txt
        txt = open(txt_file, 'w')
        txt.write(new_name)

        # 폴더명 추출
        zip_files = []
        # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
        for root, dirs, files in os.walk(file_path+ECU):
            for file in files:
                if file.endswith('.zip'):
                    # 확장자가 .zip인 파일은 리스트에 추가
                    zip_files.append(os.path.join(file))

        zip_split = zip_files[0].split("-")
        # split_str_old = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]  # old_name은 split X
        split_str_new = zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1]  # new_name

        old_name = file_path + ECU + "\\" + zip_files[0]
        new_name = file_path + ECU + "\\" + new_name + "-" + split_str_new

        os.rename(old_name, new_name)

    # ECU_CV
    def rename_ECU_CV(self):

        # file_path
        file_path = self.entry_filePath.get()
        # new_name
        new_name = self.entry_newName.get()

        # txt 파일 변경
        txt_file = file_path+ECU_CV+ECU_CV_txt
        txt = open(txt_file, 'w')
        txt.write(new_name)

        # 폴더명 추출
        zip_files = []
        # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
        for root, dirs, files in os.walk(file_path+ECU_CV):
            for file in files:
                if file.endswith('.zip'):
                    # 확장자가 .zip인 파일은 리스트에 추가
                    zip_files.append(os.path.join(file))

        zip_split = zip_files[0].split("-")
        # split_str_old = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]  # old_name은 split X
        split_str_new = zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1]  # new_name

        old_name = file_path + ECU_CV + "\\" + zip_files[0]
        new_name = file_path + ECU_CV + "\\" + new_name + "-" + split_str_new

        os.rename(old_name, new_name)

    # System
    def rename_sys(self):

        # file_path
        file_path = self.entry_filePath.get()
        # new_name
        new_name = self.entry_newName.get()

        # txt 파일 변경
        txt_file = file_path+Sys+Sys_txt
        txt = open(txt_file, 'w')
        txt.write(new_name)

        # 폴더명 추출
        zip_files = []
        # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
        for root, dirs, files in os.walk(file_path+Sys):
            for file in files:
                if file.endswith('.zip'):
                    # 확장자가 .zip인 파일은 리스트에 추가
                    zip_files.append(os.path.join(file))

        zip_split = zip_files[0].split("-")
        # split_str_old = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]  # old_name은 split X
        split_str_new = zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1]  # new_name

        old_name = file_path + Sys + "\\" + zip_files[0]
        new_name = file_path + Sys + "\\" + new_name + "-" + split_str_new

        os.rename(old_name, new_name)


    ### Check
    # Application
    def Check_app(self):

        file_path = self.entry_filePath.get()

        if "Application" in os.listdir(file_path):

            item_list = []

            # 폴더명 추출
            for item in os.listdir(file_path+App):
                sub_folder = os.path.join(file_path+App, item) # 폴더경로 + 폴더명
                if os.path.isdir(sub_folder):
                    if '.txt' not in item:
                        item_list.append(item)
                        # print("Application = " + item)
                        label=Label(self.frame, text="Application = " + item).pack()


            # 파일 열기
            with open(file_path+App+App_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
                # print("Version_txt = " + file_content)
                label=Label(self.frame, text="Version_txt = " + file_content).pack()
        
        else:
            label=Label(self.frame, text="파일이 존재하지 않습니다.", fg='red').pack()

        return

    def Check_Crit(self):

        file_path = self.entry_filePath.get()

        if "Critical" in os.listdir(file_path):
            # 폴더명 추출
            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+Critical):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            split_str_new_list = []
            # ZIP 파일 목록 출력
            # print("Critical = " + zip_files[0])
            zip_split = str(zip_files[0]).split("-")
            split_str_new = str(zip_files[0]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
            split_str_new_list.append(split_str_new)
            label=Label(self.frame, text="Critical = " + zip_files[0]).pack()
            
            # 파일 열기
            with open(file_path+Critical+Critical_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()
        
        else:
            label=Label(self.frame, text="파일이 존재하지 않습니다.", fg='red').pack()

        return

    def Check_Diag(self):

        file_path = self.entry_filePath.get()

        if "Diagnosis" in os.listdir(file_path):

            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+Diagnosis):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))
            
            split_str_new_list = []
            # ZIP 파일 목록 출력
            if len(zip_files) >= 2:
                for i in range(0,len(zip_files)):
                    # print("Diagnosis = " + zip_files[i])
                    label=Label(self.frame, text="Diagnosis = " + zip_files[i]).pack()
                    zip_split = zip_files[i].split("-")
                    split_str_new = str(zip_files[i]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                    split_str_new_list.append(split_str_new)

            elif len(zip_files) == 1:
                # print("Diagnosis = " + zip_files[0])
                label=Label(self.frame, text="Diagnosis = " + zip_files[0]).pack()
                zip_split = zip_files[0].split("-")
                split_str_new = str(zip_files[0]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                split_str_new_list.append(split_str_new)
            
            
            # 파일 열기
            with open(file_path+Diagnosis+Diagnosis_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()
        
        else:
            label=Label(self.frame, text="파일이 존재하지 않습니다.", fg='red').pack()

        return

    def Check_Diag_CV(self):

        file_path = self.entry_filePath.get()

        if "Diagnosis_CV" in os.listdir(file_path):

            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+Diagnosis_CV):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            split_str_new_list = []
            # ZIP 파일 목록 출력
            if len(zip_files) >= 2:
                for i in range(0,len(zip_files)):
                    # print("Diagnosis_CV = " + zip_files[i])
                    label=Label(self.frame, text="Diagnosis_CV = " + zip_files[i]).pack()
                    zip_split = zip_files[i].split("-")
                    split_str_new = str(zip_files[i]).replace("-"+zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                    split_str_new_list.append(split_str_new)

            elif len(zip_files) == 1:
                # print("Diagnosis_CV = " + zip_files[0])
                label=Label(self.frame, text="Diagnosis_CV = " + zip_files[0]).pack()
                zip_split = zip_files[0].split("-")
                split_str_new = str(zip_files[0]).replace("-"+zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                split_str_new_list.append(split_str_new)
            
            # 파일 열기
            with open(file_path+Diagnosis_CV+Diagnosis_CV_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()
        
        else :
            label=Label(self.frame, text="파일이 존재하지 않습니다.", fg='red').pack()

        return

    def Check_ECU(self):

        file_path = self.entry_filePath.get()

        if "ECU" in os.listdir(file_path):

            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+ECU):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            split_str_new_list = []
            # ZIP 파일 목록 출력
            # print("ECU = " + zip_files[0])
            zip_split = str(zip_files[0]).split("-")
            split_str_new = str(zip_files[0]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
            split_str_new_list.append(split_str_new)
            label=Label(self.frame, text="ECU = " + zip_files[0]).pack()
            
            # 파일 열기
            with open(file_path+ECU+ECU_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()
        
        else :
            label=Label(self.frame, text="파일이 존재하지 않습니다.", fg='red').pack()

        return

    def Check_ECU_CV(self):

        file_path = self.entry_filePath.get()
        if "ECU_CV" in os.listdir(file_path):
            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+ECU_CV):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            split_str_new_list = []
            # ZIP 파일 목록 출력
            # print("ECU_CV = " + zip_files[0])
            zip_split = zip_files[0].split("-")
            split_str_new = str(zip_files[0]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
            split_str_new_list.append(split_str_new)
            label=Label(self.frame, text="ECU_CV = " + zip_files[0]).pack()

            
            # 파일 열기
            with open(file_path+ECU_CV+ECU_CV_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

        else:
            label=Label(self.frame, text="파일이 존재하지 않습니다.", fg='red').pack()

        return

    def Check_sys(self):

        file_path = self.entry_filePath.get()

        if "System" in os.listdir(file_path) or "system" in os.listdir(file_path):
            
            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+Sys):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            split_str_new_list = []
            # ZIP 파일 목록 출력
            # print("System = " + zip_files[0])
            label=Label(self.frame, text="System = " + zip_files[0]).pack()
            zip_split = zip_files[0].split("-")
            split_str_new = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]
            split_str_new_list.append(split_str_new)

            # 파일 열기
            with open(file_path+Sys+Sys_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()
        
        else :
            label=Label(self.frame, text="파일이 존재하지 않습니다.", fg='red').pack()

        return 


    # tkinter

    # 프레임 내용 삭제
    def clear_frame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

    # 메인 함수
    def Rename(self):
        if self.selected_item.get() == '1':
            self.rename_app()
        elif self.selected_item.get() == '2':
            self.rename_critical()
        elif self.selected_item.get() == '3':
            self.rename_diag()
        elif self.selected_item.get() == '4':
            self.rename_diag_CV()
        elif self.selected_item.get() == '5':
            self.rename_ECU()
        elif self.selected_item.get() == '6':
            self.rename_ECU_CV()
        elif self.selected_item.get() == '7':
            self.rename_sys()

        self.info()   # 메세지 박스 open

    # 메시지 박스
    def info(self):
        messagebox.showinfo("알림", "파일명이 변경되었습니다")

    def VersionCheck(self):
        if self.selected_item.get() == '1':
            self.Check_app()
        elif self.selected_item.get() == '2':
            self.Check_Crit()
        elif self.selected_item.get() == '3':
            self.Check_Diag()
        elif self.selected_item.get() == '4':
            self.Check_Diag_CV()
        elif self.selected_item.get() == '5':
            self.Check_ECU()
        elif self.selected_item.get() == '6':
            self.Check_ECU_CV()
        elif self.selected_item.get() == '7':
            self.Check_sys()

class rename_4:
    def __init__(self, window2):
        # 화면 가운데 위치
        window2.title("4세대 파일명 변경 프로그램")
        # window2.geometry("400x700")
        window2_width = 400
        window2_height = 700  # 높이 조정
        screen_width = window2.winfo_screenwidth()
        screen_height = window2.winfo_screenheight()
        center_x = int(screen_width / 2 - window2_width / 2)
        center_y = int(screen_height / 2 - window2_height / 2)
        window2.geometry(f"{window2_width}x{window2_height}+{center_x}+{center_y}")

        self.build_ui(window2)
    
    def build_ui(self, window2):

        # 파일 경로 입력
        self.label_title=tk.Label(window2, text="*** 4세대 파일명 변경 프로그램 입니다 ***", fg="blue", relief="groove")
        self.label_title.pack(fill='x', padx=5, pady=5)

        self.label_frame1 = ttk.LabelFrame(window2, text="설정")
        self.label_frame1.pack(padx=10, pady=10, fill="x", expand=True)

        # 파일 경로 입력
        self.label1=tk.Label(self.label_frame1, text="[Step 1] 파일 경로를 입력하세요")
        self.label1.pack(fill='x', padx=5, pady=5)

        self.entry_filePath=ttk.Entry(self.label_frame1, width=50, justify="center")
        self.entry_filePath.pack(fill='x', padx=5, pady=5)

        # 텍스트
        self.label2=tk.Label(self.label_frame1, text="[Step 2] 항목을 선택하세요")
        self.label2.pack(fill='x', padx=5, pady=5)

        # 항목값
        self.selected_item = tk.StringVar()
        items = (('Application', '1'),
                ('Resource', '2'),
                ('SupportApp', '3'),
                ('System', '4'))        

        # radio buttons
        for item in items:
            r = ttk.Radiobutton(
                self.label_frame1,
                text=item[0],
                value=item[1],
                variable=self.selected_item
            )
            r.pack(padx=5, pady=5)

        # new file명 입력
        self.label3=tk.Label(self.label_frame1, text="[Step 3] 바꿀 파일명을 입력하세요")
        self.label3.pack(fill='x', padx=5, pady=5)

        self.entry_newName=ttk.Entry(self.label_frame1, width=50, justify="center")
        self.entry_newName.pack(fill='x', padx=5, pady=5)

        # 버튼
        btn_Rename = ttk.Button(self.label_frame1, text = "파일명 변경", command = self.Rename)
        btn_Rename.pack(fill='x', padx=5, pady=5)

        # new file명 입력
        self.label3=tk.Label(self.label_frame1, text="[Step 4] 버전을 확인하세요")
        self.label3.pack(fill='x', padx=5, pady=5)

        btn_versionCheck = ttk.Button(self.label_frame1, text = "버전 확인", command = self.VersionCheck)
        btn_versionCheck.pack(fill='x', padx=5, pady=5)

        # 프레임
        self.frame = LabelFrame(self.label_frame1, text="결과")
        self.frame.pack(padx=5, pady=5, fill="x", expand=True)

        self.label4 = Label(self.frame)
        self.label4.pack(padx=0.01, pady=0.01)

        btn_cls = ttk.Button(self.label_frame1, text="초기화", command = self.clear_frame)
        btn_cls.pack(padx=5, pady=5)

    ### Rename
    # Application
    def rename_app(self):
        # file_path
        file_path = self.entry_filePath.get()
        # new_name
        new_name = self.entry_newName.get()

        # 폴더명 추출
        for item in os.listdir(file_path+App):
            if '.txt' not in item :
                old_name = os.path.join(file_path+App, item) # 폴더경로 + 폴더명

        # txt 파일 변경
        txt_file = file_path+App+App_txt
        txt = open(txt_file, 'w')
        txt.write(new_name)

        new_name = file_path + App + "\\" + new_name
        os.rename(old_name, new_name)

    # Resource
    def rename_rsc(self):
        # file_path
        file_path = self.entry_filePath.get()
        # new_name
        new_name = self.entry_newName.get()

        # txt 파일 변경
        txt_file = file_path+Rsc+Rsc_txt
        txt = open(txt_file, 'w')
        txt.write(new_name)

        # 폴더명 추출
        zip_files = []
        # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
        for root, dirs, files in os.walk(file_path+Rsc):
            for file in files:
                if file.endswith('.zip'):
                    # 확장자가 .zip인 파일은 리스트에 추가
                    zip_files.append(os.path.join(file))

        # ZIP 파일 목록 출력
        if len(zip_files) >= 2:
            split_str_new_list = []
            old_name = old_name = file_path + Rsc + "\\"
            new_name = file_path + Rsc + "\\" + new_name + "-"
            old_name_list = []
            new_name_list = []
            
            for i in range(0,len(zip_files)):
                zip_split = zip_files[i].split("-")
                # split_str_old = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]  # old_name은 split X
                split_str_new = zip_split[3]+"-"+zip_split[4]+"-"+zip_split[5]  # new_name
                split_str_new_list.append(split_str_new)  
                old_name_list.append(old_name + zip_files[i])
                new_name_list.append(new_name + split_str_new_list[i])

            for i in range(0, len(old_name_list)):
                os.rename(old_name_list[i], new_name_list[i])

        elif len(zip_files) == 1:
            zip_split = zip_files[0].split("-")
            # split_str_old = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]  # old_name은 split X
            split_str_new = zip_split[3]+"-"+zip_split[4]+"-"+zip_split[5]  # new_name

            old_name = file_path + Rsc + "\\" + zip_files[0]
            new_name = file_path + Rsc + "\\" + new_name + "-" + split_str_new

            os.rename(old_name, new_name)

    # SupportApp
    def rename_supportApp(self):
        # file_path
        file_path = self.entry_filePath.get()
        # new_name
        new_name = self.entry_newName.get()

        # 폴더명 추출
        for item in os.listdir(file_path + SupportApp):
            if '.txt' not in item :
                old_name = os.path.join(file_path + SupportApp, item) # 폴더경로 + 폴더명

        # txt 파일 변경
        txt_file = file_path+SupportApp+SupportApp_txt
        txt = open(txt_file, 'w')
        txt.write(new_name)

        new_name = file_path + SupportApp + "\\" + new_name
        os.rename(old_name, new_name)

    # System
    def rename_sys(self):
        # file_path
        file_path = self.entry_filePath.get()
        # new_name
        new_name = self.entry_newName.get()

        # txt 파일 변경
        txt_file = file_path+Sys+Sys_txt
        txt = open(txt_file, 'w')
        txt.write(new_name)

        # 폴더명 추출
        zip_files = []
        # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
        for root, dirs, files in os.walk(file_path+Sys):
            for file in files:
                if file.endswith('.zip'):
                    # 확장자가 .zip인 파일은 리스트에 추가
                    zip_files.append(os.path.join(file))

        zip_split = zip_files[0].split("-")
        # split_str_old = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]  # old_name은 split X
        split_str_new = zip_split[3]+"-"+zip_split[4]+"-"+zip_split[5]  # new_name

        old_name = file_path + Sys + "\\" + zip_files[0]
        new_name = file_path + Sys + "\\" + new_name + "-" + split_str_new

        os.rename(old_name, new_name)

    ### Check
    # Application
    def Check_app(self):

        file_path = self.entry_filePath.get()
        item_list = []

        # 폴더명 추출
        for item in os.listdir(file_path+App):
            sub_folder = os.path.join(file_path+App, item) # 폴더경로 + 폴더명
            if os.path.isdir(sub_folder):
                if '.txt' not in item:
                    item_list.append(item)
                    # print("Application = " + item)
                    label=Label(self.frame, text="Application = " + item).pack()


        # 파일 열기
        with open(file_path+App+App_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

    def Check_rsc(self):

        file_path = self.entry_filePath.get()

        # 폴더명 추출
        zip_files = []
        # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
        for root, dirs, files in os.walk(file_path+Rsc):
            for file in files:
                if file.endswith('.zip'):
                    # 확장자가 .zip인 파일은 리스트에 추가
                    zip_files.append(os.path.join(file))

        split_str_new_list = []
        # ZIP 파일 목록 출력
        if len(zip_files) >= 2:
            for i in range(0,len(zip_files)):
                # print("Resource = " + zip_files[i])
                label=Label(self.frame, text="Resource = " + zip_files[i]).pack()
                zip_split = zip_files[i].split("-")
                split_str_new = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]
                split_str_new_list.append(split_str_new)

        elif len(zip_files) == 1:
            # print("Resource = " + zip_files[0])
            label=Label(self.frame, text="Resource = " + zip_files[0]).pack()
            zip_split = zip_files[0].split("-")
            split_str_new = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]
            split_str_new_list.append(split_str_new)
        
        # 파일 열기
        with open(file_path+Rsc+Rsc_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("Version_txt = " + file_content)
        label=Label(self.frame, text="Version_txt = " + file_content).pack()

    def Check_SupportApp(self):

        file_path = self.entry_filePath.get()
        item_list = []

        # 폴더명 추출
        for item in os.listdir(file_path+SupportApp):
            sub_folder = os.path.join(file_path+SupportApp, item) # 폴더경로 + 폴더명
            if os.path.isdir(sub_folder):
                if '.txt' not in item:
                    item_list.append(item)
                    # print("SupportApp = " + item)
                    label=Label(self.frame, text="SupportApp = " + item).pack()

        # 파일 열기
        with open(file_path+SupportApp+SupportApp_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("Version_txt = " + file_content)
        label=Label(self.frame, text="Version_txt = " + file_content).pack()

        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)          
        if item_list[0] != file_content:
            # print("!!!!!!!! FAIL !!!!!!!!")
            label=Label(self.frame, text="FAIL", fg="red").pack()
            # print(item_list[0], file_content)
            label=Label(self.frame, text=(item_list[0], file_content), fg="red").pack()
        else :
            # print("PASS") 
            label=Label(self.frame, text="PASS", fg="blue").pack()

    def Check_sys(self):

        file_path = self.entry_filePath.get()
        zip_files = []

        # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
        for root, dirs, files in os.walk(file_path+Sys):
            for file in files:
                if file.endswith('.zip'):
                    # 확장자가 .zip인 파일은 리스트에 추가
                    zip_files.append(os.path.join(file))

        split_str_new_list = []
        # ZIP 파일 목록 출력
        # print("System = " + zip_files[0])
        label=Label(self.frame, text="System = " + zip_files[0]).pack()
        zip_split = zip_files[0].split("-")
        split_str_new = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]
        split_str_new_list.append(split_str_new)

        # 파일 열기
        with open(file_path+Sys+Sys_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("Version_txt = " + file_content)
        label=Label(self.frame, text="Version_txt = " + file_content).pack()

    # tkinter

    # 프레임 내용 삭제
    def clear_frame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

    # 메인 함수
    def Rename(self):
        if self.selected_item.get() == '1':
            self.rename_app()
        elif self.selected_item.get() == '2':
            self.rename_rsc()
        elif self.selected_item.get() == '3':
            self.rename_supportApp()
        elif self.selected_item.get() == '4':
            self.rename_sys()

        self.info()   # 메세지 박스 open

    # 메시지 박스
    def info(self):
        messagebox.showinfo("알림", "파일명이 변경되었습니다")

    def VersionCheck(self):
        if self.selected_item.get() == '1':
            self.Check_app()
        elif self.selected_item.get() == '2':
            self.Check_rsc()
        elif self.selected_item.get() == '3':
            self.Check_SupportApp()
        elif self.selected_item.get() == '4':
            self.Check_sys() 

class versionCheck:
    def __init__(self,window3):
        # 화면 가운데 위치
        window3.title("파일 버전 확인 프로그램")
        # window3.geometry("400x700")
        window3_width = 400
        window3_height = 600  # 높이 조정
        screen_width = window3.winfo_screenwidth()
        screen_height = window3.winfo_screenheight()
        center_x = int(screen_width / 2 - window3_width / 2)
        center_y = int(screen_height / 2 - window3_height / 2)
        window3.geometry(f"{window3_width}x{window3_height}+{center_x}+{center_y}")

        self.build_ui(window3)
    
    def build_ui(self, window3):
        self.label_title=tk.Label(window3, text="*** 파일 버전 확인 프로그램 입니다 ***", fg="blue", relief="groove")
        self.label_title.pack(fill='x', padx=5, pady=5)

        self.label_frame1 = ttk.LabelFrame(window3, text="설정")
        self.label_frame1.pack(padx=10, pady=10, fill="x", expand=True)

        self.label1=tk.Label(self.label_frame1, text="[Step 1] 프로젝트를 선택하세요")
        self.label1.pack(padx=5, pady=5)

        self.selected_project = tk.StringVar()
        projects = (('3세대', '1'),
                ('4세대', '2'),
                ('Gscan', '3'))

        # radio buttons
        for project in projects:
            r = ttk.Radiobutton(
                self.label_frame1,
                text=project[0],
                value=project[1],
                variable=self.selected_project
            )
            r.pack(padx=5, pady=5)

        self.label2=tk.Label(self.label_frame1, text="[Step 2] 파일 경로를 입력하세요")
        self.label2.pack(fill='x', padx=5, pady=5)

        self.entry=ttk.Entry(self.label_frame1, width=50, justify="center")
        self.entry.pack(fill='x', padx=5, pady=5)

        self.label2=tk.Label(self.label_frame1, text="[Step 3] 버전을 확인 하세요")
        self.label2.pack(fill='x', padx=5, pady=5)

        btn_versionCheck = ttk.Button(self.label_frame1, text = "버전 확인", command = self.main_function)
        btn_versionCheck.pack(fill='x', padx=5, pady=5)

        self.frame = LabelFrame(self.label_frame1, text="결과")
        self.frame.pack(padx=5, pady=5, fill="x", expand=True)

        self.label3 = Label(self.frame)
        self.label3.pack(padx=0.01, pady=0.01)

        btn_cls = ttk.Button(self.label_frame1, text = "초기화", command=self.clear_frame)
        btn_cls.pack(padx=5, pady=5)


    def GDSN(self):

        # file_path = input("♥♥♥ 파일경로를 입력하세요 : ")
        file_path = self.entry.get()

        # Application-----------------------------------

        if "Application" in os.listdir(file_path):

            item_list = []

            # 폴더명 추출
            for item in os.listdir(file_path+App):
                sub_folder = os.path.join(file_path+App, item) # 폴더경로 + 폴더명
                if os.path.isdir(sub_folder):
                    if '.txt' not in item:
                        item_list.append(item)
                        # print("Application = " + item)
                        label=Label(self.frame, text="Application = " + item).pack()

            # 파일 열기
            with open(file_path+App+App_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
                # print("Version_txt = " + file_content)
                label=Label(self.frame, text="Version_txt = " + file_content).pack()

            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)  
            if item_list[0] != file_content:
                # print("!!!!!!!! FAIL !!!!!!!!")
                label=Label(self.frame, text="FAIL", fg="red").pack()
            else :
                # print("PASS")
                label=Label(self.frame, text="PASS", fg="blue").pack()

        else:
            pass
            


        # Resource-----------------------------------
        
        if "Resource" in os.listdir(file_path):
            # 폴더명 추출
            zip_files = []
            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+Rsc):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            split_str_new_list = []
            # ZIP 파일 목록 출력
            if len(zip_files) >= 2:
                for i in range(0,len(zip_files)):
                    # print("Resource = " + zip_files[i])
                    label=Label(self.frame, text="Resource = " + zip_files[i]).pack()
                    zip_split = zip_files[i].split("-")
                    split_str_new = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]
                    split_str_new_list.append(split_str_new)

            elif len(zip_files) == 1:
                # print("Resource = " + zip_files[0])
                label=Label(self.frame, text="Resource = " + zip_files[0]).pack()
                zip_split = zip_files[0].split("-")
                split_str_new = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]
                split_str_new_list.append(split_str_new)
            
            # 파일 열기
            with open(file_path+Rsc+Rsc_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()
            
            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
            pass_list=[]

            for i in range(0,len(split_str_new_list)):
                if split_str_new_list[i] == file_content:
                    pass_list.append("PASS")
            
            if len(pass_list) == len(split_str_new_list) :
                # print(pass_list)
                # print("PASS")
                label=Label(self.frame, text="PASS", fg="blue").pack()
            else :
                # print("!!!!!!!!! FAIL !!!!!!!!!")
                label=Label(self.frame, text="FAIL", fg="red").pack()

        else:
            pass

        # SupportApp----------------------------------
        
        if "SupportApp" in os.listdir(file_path):

            item_list = []

            # 폴더명 추출
            for item in os.listdir(file_path+SupportApp):
                sub_folder = os.path.join(file_path+SupportApp, item) # 폴더경로 + 폴더명
                if os.path.isdir(sub_folder):
                    if '.txt' not in item:
                        item_list.append(item)
                        # print("SupportApp = " + item)
                        label=Label(self.frame, text="SupportApp = " + item).pack()

            # 파일 열기
            with open(file_path+SupportApp+SupportApp_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)          
            if item_list[0] != file_content:
                # print("!!!!!!!! FAIL !!!!!!!!")
                label=Label(self.frame, text="FAIL", fg="red").pack()
                # print(item_list[0], file_content)
                label=Label(self.frame, text=(item_list[0], file_content), fg="red").pack()
            else :
                # print("PASS") 
                label=Label(self.frame, text="PASS", fg="blue").pack()           

        else:
            pass


        # System--------------------------------------
        
        if "system" in os.listdir(file_path) or "System" in os.listdir(file_path):

            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+Sys):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            split_str_new_list = []
            # ZIP 파일 목록 출력
            # print("System = " + zip_files[0])
            label=Label(self.frame, text="System = " + zip_files[0]).pack()
            zip_split = zip_files[0].split("-")
            split_str_new = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]
            split_str_new_list.append(split_str_new)

            # 파일 열기
            with open(file_path+Sys+Sys_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

            pass_list=[]

            for i in range(0,len(split_str_new_list)):
                if split_str_new_list[i] == file_content:
                    pass_list.append("PASS")
            
            if len(pass_list) == len(split_str_new_list) :
                # print(pass_list)
                # print("PASS")
                label=Label(self.frame, text="PASS", fg="blue").pack()
            else :
                # print("!!!!!!!!! FAIL !!!!!!!!!")
                label=Label(self.frame, text="FAIL", fg="red").pack()            
        else:
            pass
        
        return

    def GDSM(self):

        file_path = self.entry.get()

        # Application-----------------------------------

        if "Application" in os.listdir(file_path):

            item_list = []

            # 폴더명 추출
            for item in os.listdir(file_path+App):
                sub_folder = os.path.join(file_path+App, item) # 폴더경로 + 폴더명
                sub_folder2 = os.path.join(item) # 폴더명만
                if os.path.isdir(sub_folder):
                    if '.txt' not in item:
                        item_list.append(item)
                        # print("Application = " + item)
                        label=Label(self.frame, text="Application = " + item).pack()
            # 파일 열기
            with open(file_path+App+App_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
                # print("Version_txt = " + file_content)
                label=Label(self.frame, text="Version_txt = " + file_content).pack()

            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)  
            if item_list[0] != file_content:
                # print("!!!!!!!! FAIL !!!!!!!!")
                label=Label(self.frame, text="FAIL", fg="red").pack()
            else :
                # print("PASS")
                label=Label(self.frame, text="PASS", fg="blue").pack()

        else:
            pass

        # Critical----------------------------------
        
        if "Critical" in os.listdir(file_path):
            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+Critical):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            split_str_new_list = []
            # ZIP 파일 목록 출력
            # print("Critical = " + zip_files[0])
            zip_split = str(zip_files[0]).split("-")
            split_str_new = str(zip_files[0]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
            split_str_new_list.append(split_str_new)
            label=Label(self.frame, text="Critical = " + zip_files[0]).pack()
            
            # 파일 열기
            with open(file_path+Critical+Critical_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
            pass_list=[]

            for i in range(0,len(split_str_new_list)):
                if split_str_new_list[i] == file_content:
                    pass_list.append("PASS")
            
            if "PASS" in pass_list :
                # print(pass_list)
                # print("PASS")
                label=Label(self.frame, text="PASS", fg="blue").pack()
            else :
                # print("!!!!!!!!! FAIL !!!!!!!!!")
                label=Label(self.frame, text="FAIL", fg="red").pack()

        else:
            pass

        # Diagnosis----------------------------------
        
        if "Diagnosis" in os.listdir(file_path):
            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+Diagnosis):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))
            
            split_str_new_list = []
            # ZIP 파일 목록 출력
            if len(zip_files) >= 2:
                for i in range(0,len(zip_files)):
                    # print("Diagnosis = " + zip_files[i])
                    label=Label(self.frame, text="Diagnosis = " + zip_files[i]).pack()
                    zip_split = zip_files[i].split("-")
                    split_str_new = str(zip_files[i]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                    split_str_new_list.append(split_str_new)

            elif len(zip_files) == 1:
                # print("Diagnosis = " + zip_files[0])
                label=Label(self.frame, text="Diagnosis = " + zip_files[0]).pack()
                zip_split = zip_files[0].split("-")
                split_str_new = str(zip_files[0]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                split_str_new_list.append(split_str_new)
            
            
            # 파일 열기
            with open(file_path+Diagnosis+Diagnosis_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()


            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
            pass_list=[]

            for i in range(0,len(split_str_new_list)):
                if split_str_new_list[i] == file_content:
                    pass_list.append("PASS")
            
            if "PASS" in pass_list :
                # print(pass_list)
                # print("PASS")
                label=Label(self.frame, text="PASS", fg="blue").pack()
            else :
                # print("!!!!!!!!! FAIL !!!!!!!!!")
                label=Label(self.frame, text="FAIL", fg="red").pack()


        else:
            pass

        # Diagnosis_CV----------------------------------
        
        if "Diagnosis_CV" in os.listdir(file_path):
            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+Diagnosis_CV):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            split_str_new_list = []
            # ZIP 파일 목록 출력
            if len(zip_files) >= 2:
                for i in range(0,len(zip_files)):
                    # print("Diagnosis_CV = " + zip_files[i])
                    label=Label(self.frame, text="Diagnosis_CV = " + zip_files[i]).pack()
                    zip_split = zip_files[i].split("-")
                    split_str_new = str(zip_files[i]).replace("-"+zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                    split_str_new_list.append(split_str_new)

            elif len(zip_files) == 1:
                # print("Diagnosis_CV = " + zip_files[0])
                label=Label(self.frame, text="Diagnosis_CV = " + zip_files[0]).pack()
                zip_split = zip_files[0].split("-")
                split_str_new = str(zip_files[0]).replace("-"+zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                split_str_new_list.append(split_str_new)
            
            # 파일 열기
            with open(file_path+Diagnosis_CV+Diagnosis_CV_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
            pass_list=[]

            for i in range(0,len(split_str_new_list)):
                if split_str_new_list[i] == file_content:
                    pass_list.append("PASS")
            
            if "PASS" in pass_list :
                # print(pass_list)
                # print("PASS")
                label=Label(self.frame, text="PASS", fg="blue").pack()
            else :
                # print("!!!!!!!!! FAIL !!!!!!!!!")
                label=Label(self.frame, text="FAIL", fg="red").pack()


        else:
            pass

        # ECU----------------------------------
        
        if "ECU" in os.listdir(file_path):
            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+ECU):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            split_str_new_list = []
            # ZIP 파일 목록 출력
            # print("ECU = " + zip_files[0])
            label=Label(self.frame, text="ECU = " + zip_files[0]).pack()
            zip_split = str(zip_files[0]).split("-")
            split_str_new = str(zip_files[0]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
            split_str_new_list.append(split_str_new)
            
            
            # 파일 열기
            with open(file_path+ECU+ECU_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
            pass_list=[]

            for i in range(0,len(split_str_new_list)):
                if split_str_new_list[i] == file_content:
                    pass_list.append("PASS")
            
            if "PASS" in pass_list :
                # print(pass_list)
                # print("PASS")
                label=Label(self.frame, text="PASS", fg="blue").pack()
            else :
                # print("!!!!!!!!! FAIL !!!!!!!!!")
                label=Label(self.frame, text="FAIL", fg="red").pack()

        else:
            pass

        # ECU_CV----------------------------------
        
        if "ECU_CV" in os.listdir(file_path):

            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+ECU_CV):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            split_str_new_list = []
            # ZIP 파일 목록 출력
            # print("ECU_CV = " + zip_files[0])
            label=Label(self.frame, text="ECU_CV = " + zip_files[0]).pack()
            zip_split = zip_files[0].split("-")
            split_str_new = str(zip_files[0]).replace("-"+zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
            split_str_new_list.append(split_str_new)
            

            # 파일 열기
            with open(file_path+ECU_CV+ECU_CV_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
            pass_list=[]

            for i in range(0,len(split_str_new_list)):
                if split_str_new_list[i] == file_content:
                    pass_list.append("PASS")
            
            if "PASS" in pass_list :
                # print(pass_list)
                # print("PASS")
                label=Label(self.frame, text="PASS", fg="blue").pack()
            else :
                # print("!!!!!!!!! FAIL !!!!!!!!!")
                label=Label(self.frame, text="FAIL", fg="red").pack()

        else:
            pass

        # System--------------------------------------
        
        if "System" in os.listdir(file_path) or "system" in os.listdir(file_path):

            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+Sys):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            split_str_new_list = []
            # ZIP 파일 목록 출력
            # print("System = " + zip_files[0])
            label=Label(self.frame, text="System = " + zip_files[0]).pack()
            zip_split = zip_files[0].split("-")
            split_str_new = str(zip_files[0]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
            split_str_new_list.append(split_str_new)

            # 파일 열기
            with open(file_path+Sys+Sys_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
            pass_list=[]

            for i in range(0,len(split_str_new_list)):
                if split_str_new_list[i] == file_content:
                    pass_list.append("PASS")
            
            if "PASS" in pass_list :
                # print(pass_list)
                # print("PASS")
                label=Label(self.frame, text="PASS", fg="blue").pack()
            else :
                # print("!!!!!!!!! FAIL !!!!!!!!!")
                label=Label(self.frame, text="FAIL", fg="red").pack()

        else:
            pass
        
        return

    def Gscan(self):

        file_path = self.entry.get()

        # application-----------------------------------

        if "application" in os.listdir(file_path):

            # 폴더명 추출
            for item in os.listdir(file_path+app):
                sub_folder = os.path.join(file_path+app, item) # 폴더경로 + 폴더명
                if os.path.isdir(sub_folder):
                    # print("application = " + item)
                    label=Label(self.frame, text="Application = " + item).pack()

            # 파일 열기
            with open(file_path+app+app_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
                # print("application_version_txt = " + file_content)
                label=Label(self.frame, text="Version_txt = " + file_content).pack()

        else:
            pass

        # critical----------------------------------
        
        if "critical" in os.listdir(file_path):
            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+critical):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            # ZIP 파일 목록 출력
            # print("critical = " + zip_files[0])
            label=Label(self.frame, text="critical = " + zip_files[0]).pack()
            
            # 파일 열기
            with open(file_path+critical+critical_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

        else:
            pass

        # diagnosis----------------------------------
        
        if "diagnosis" in os.listdir(file_path):
            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+diagnosis):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            # ZIP 파일 목록 출력
            # print("diagnosis = " + zip_files[0])
            label=Label(self.frame, text="diagnosis = " + zip_files[0]).pack()
            
            # 파일 열기
            with open(file_path+diagnosis+diagnosis_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("diagnosis_version_txt = " + file_content)
            label=Label(self.frame, text="diagnosis_version_txt = " + file_content).pack()

        else:
            pass

        # diagnosis_cv----------------------------------
        
        if "diagnosis_cv" in os.listdir(file_path):
            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+diagnosis_cv):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            # ZIP 파일 목록 출력
            # print("diagnosis_cv = " + zip_files[0])
            label=Label(self.frame, text="diagnosis_cv = " + zip_files[0]).pack()
            
            # 파일 열기
            with open(file_path+diagnosis_cv+diagnosis_cv_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

        else:
            pass

        # diagnosis_im----------------------------------
        
        if "diagnosis_im" in os.listdir(file_path):
            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+diagnosis_im):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            # ZIP 파일 목록 출력
            # print("diagnosis_im = " + zip_files[0])
            label=Label(self.frame, text="diagnosis_im = " + zip_files[0]).pack()
            
            # 파일 열기
            with open(file_path+diagnosis_im+diagnosis_im_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

        else:
            pass

        # gscan_os----------------------------------
        
        if "os" in os.listdir(file_path):
            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+gscan_os):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            # ZIP 파일 목록 출력
            # print("os = " + zip_files[0])
            label=Label(self.frame, text="os = " + zip_files[0]).pack()
            
            # 파일 열기
            with open(file_path+gscan_os+gscan_os_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("os_version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()
            
        else:
            pass

        # system--------------------------------------
        
        if "system" in os.listdir(file_path):

            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+system):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            # ZIP 파일 목록 출력
            # print("system = " + zip_files[0])
            label=Label(self.frame, text="system = " + zip_files[0]).pack()

            # 파일 열기
            with open(file_path+system+sys_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("system_version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

        else:
            pass

        return

    def clear_frame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

    # 메인 함수
    def main_function(self):
        if self.selected_project.get() == '1':
            self.GDSM()
        elif self.selected_project.get() == '2':
            self.GDSN()
        elif self.selected_project.get() == '3':
            self.Gscan()

class CompressApp:
    def __init__(self, window4):
        self.window4 = window4  # window4를 인스턴스 변수로 저장
        self.config = configparser.ConfigParser()
        self.config_file = 'settings.ini'
        self.load_settings()

        window4.title("분할 압축 프로그램")
        window4.geometry("400x500")  # 높이 조정

        # 화면 가운데 위치
        window_width = 400
        window_height = 500  # 높이 조정
        screen_width = window4.winfo_screenwidth()
        screen_height = window4.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        window4.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        self.build_ui(window4)
        # window4.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def build_ui(self, window4):
        self.label_title=tk.Label(window4, text="*** 분할 압축 프로그램 입니다 ***", fg="blue", relief="groove")
        self.label_title.pack(fill='x', padx=5, pady=5)

        self.label_frame = ttk.LabelFrame(window4, text="설정")
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
        self.progress_bar = ttk.Progressbar(window4, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(padx=10, pady=10, fill="x")

        ttk.Button(window4, text="압축 시작", command=self.start_compression).pack(pady=20)

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
        self.window4.update_idletasks()  # window4 대신 self.window4 사용

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
        self.window4.after(0, self.reset_ui)  # Ensure UI reset is called in the main thread

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

    # def on_closing(self):
    #     self.save_settings()
    #     window4.destroy()

class nullCheck:
    def __init__(self, window5):
        # 화면 가운데 위치
        window5.title("빈 파일 확인 프로그램")
        # window.geometry("400x700")
        window_width = 400
        window_height = 500  # 높이 조정
        screen_width = window5.winfo_screenwidth()
        screen_height = window5.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        window5.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        self.build_ui(window5)

    def build_ui(self, window5):
        # 파일 경로 입력
        label_title=tk.Label(window5, text="*** 빈 파일 확인 프로그램 입니다 ***", fg="green", relief="groove")
        label_title.pack(fill='x', padx=5, pady=5)

        self.label_frame1 = ttk.LabelFrame(window5, text="설정")
        self.label_frame1.pack(padx=10, pady=10, fill="x", expand=True)

        self.label1 = Label(self.label_frame1, text="프로젝트를 선택하세요")
        self.label1.pack(anchor='w')

        # 항목값
        self.selected_item = tk.StringVar(value='2')  # 기본값으로 4세대 선택
        items = (('3세대 진단SW [GDSM]', '1'),
                ('4세대 진단SW [GDSN]', '2'))

        # 프로젝트 선택 라디오 버튼
        for item in items:
            r = ttk.Radiobutton(
                self.label_frame1,
                text=item[0],
                value=item[1],
                variable=self.selected_item,
                command=self.update_rsc_folder
            )
            r.pack(padx=5, pady=5)

        self.label2 = Label(self.label_frame1, text="파일 경로:")
        self.label2.pack(anchor='w')

        self.entry_filePath = ttk.Entry(self.label_frame1, width=50, justify="center")
        self.entry_filePath.pack(padx=5, pady=5)

        btn_Check = ttk.Button(self.label_frame1, text="Resource 빈 파일 확인", command=self.main_function)
        btn_Check.pack(padx=5, pady=5)

        # btn_delete = ttk.Button(label_frame1, text="압축 해제한 파일 삭제", command=delete_extracted_files)
        # btn_delete.pack(fill='x', padx=5, pady=5)

        # 프레임
        self.frame = LabelFrame(self.label_frame1, text="결과")
        self.frame.pack(padx=5, pady=5, fill="x", expand=True)

        self.label3 = Label(self.frame)
        self.label3.pack()

        btn_cls = ttk.Button(self.label_frame1, text="초기화", command=self.clear_frame)
        btn_cls.pack(padx=5, pady=5)

    # 폴더명 추출
    zip_files = []
    empty_folders = []

    def clear_frame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

    def update_rsc_folder(self):
        global Rsc
        if self.selected_item.get() == '1':
            Rsc = Diagnosis
        elif self.selected_item.get() == '2':
            Rsc = Rsc

    def rsc_fileList(self):
        self.zip_files.clear()  # 리스트 초기화
        file_path = self.entry_filePath.get()
        # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
        for root, dirs, files in os.walk(file_path + Rsc):
            for file in files:
                if file.endswith('.zip'):
                    # 확장자가 .zip인 파일은 리스트에 추가
                    self.zip_files.append(os.path.join(file))
        return

    def fileCheck(self):
        self.empty_folders.clear()  # 리스트 초기화
        file_path = self.entry_filePath.get()
        rsc_path = file_path + Rsc
        for i in range(0, len(self.zip_files)):
            zip_file_rep = self.zip_files[i].replace('.zip', '')
            file_name = file_path + Rsc + "\\" + zip_file_rep

            # 압축 파일 해제
            dirsList = []
            for dirs in os.listdir(rsc_path):
                dirsList.append(dirs)
            if zip_file_rep not in dirsList:
                os.makedirs(file_name, exist_ok=True)  # 폴더 생성
                zipfile.ZipFile(file_path + Rsc + "\\" + self.zip_files[i]).extractall(file_path + Rsc + "\\" + zip_file_rep)
            elif zip_file_rep in dirs:
                shutil.rmtree(file_name)  # 폴더 전체 삭제
                os.makedirs(file_name, exist_ok=True)  # 폴더 생성
                zipfile.ZipFile(file_path + Rsc + "\\" + self.zip_files[i]).extractall(file_path + Rsc + "\\" + zip_file_rep)

            # 빈 파일 확인
            for (root, dirs, files) in os.walk(file_name):
                if not dirs:
                    if not files:
                        self.empty_folders.append(root)

        if len(self.empty_folders) == 0:
            label = Label(self.frame, text="빈 파일이 없습니다", fg="blue")
            label.pack()
        else:
            for i in range(0, len(self.empty_folders)):
                label = Label(self.frame, text=self.empty_folders[i] + " 파일을 확인하세요", fg="red", wraplength=400)
                label.pack()


        file_path = self.entry_filePath.get()
        response = messagebox.askyesno("확인", "압축 해제한 파일을 삭제하시겠습니까?")
        if response == 1:  # 사용자가 '확인'을 클릭한 경우
            for i in range(0, len(self.zip_files)):
                zip_file_rep = self.zip_files[i].replace('.zip', '')
                shutil.rmtree(file_path + Rsc + "\\" + zip_file_rep)
            messagebox.showinfo("알림", "압축 해제한 파일이 성공적으로 삭제되었습니다.")
        else:
            messagebox.showinfo("알림", "파일 삭제가 취소되었습니다.")


    def main_function(self):
        self.rsc_fileList()  # 리소스 파일 리스트
        self.fileCheck()  # 파일 확인


# 메인 Window ------------------------------------
def createNewWindow1():
    window1 = tk.Toplevel(mainWindow)
    app = rename_3(window1)
    window1.mainloop()

def createNewWindow2():
    window2 = tk.Toplevel(mainWindow)
    app = rename_4(window2)
    window2.mainloop()

def createNewWindow3():
    window3 = tk.Toplevel(mainWindow)
    app = versionCheck(window3)
    window3.mainloop()

def createNewWindow4():
    window4 = tk.Toplevel(mainWindow)
    app = CompressApp(window4)
    window4.mainloop()

def createNewWindow5():
    window5 = tk.Toplevel(mainWindow)
    app = nullCheck(window5)
    window5.mainloop()

mainWindow = Tk()
mainWindow.title("AutomationTool")

# 화면 비율
window_width = 300
window_height = 300  # 높이 조정
screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
mainWindow.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

label_frame = ttk.LabelFrame(mainWindow, text="프로그램")
label_frame.pack(padx=10, pady=10, fill="x", expand=True)

# 버튼
button1 = ttk.Button(label_frame, text="3세대 파일명 변경 프로그램", command=createNewWindow1)
button1.pack(padx=7, pady=7)
button2 = ttk.Button(label_frame, text="4세대 파일명 변경 프로그램", command=createNewWindow2)
button2.pack(padx=7, pady=7)
button3 = ttk.Button(label_frame, text="파일 버전 확인 프로그램", command=createNewWindow3)
button3.pack(padx=7, pady=7)
button4 = ttk.Button(label_frame, text="자동 분할 압축 프로그램", command=createNewWindow4)
button4.pack(padx=7, pady=7)
button5 = ttk.Button(label_frame, text="빈 파일 확인 프로그램", command=createNewWindow5)
button5.pack(padx=7, pady=7)


mainWindow.mainloop()