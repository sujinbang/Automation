# -- 전체 통합 프로그램 입니다
import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import zipfile
import threading
import configparser
import re
import shutil

# GIMS Description 크롤링으로 자동화 구현
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
# tkinter
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
import chromedriver_autoinstaller

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
        self.label3=tk.Label(self.label_frame1, text="[Step 3] 버전을 확인하세요")
        self.label3.pack(fill='x', padx=5, pady=5)

        btn_versionCheck = ttk.Button(self.label_frame1, text = "버전 확인", command = self.VersionCheck)
        btn_versionCheck.pack(fill='x', padx=5, pady=5)

        # 프레임
        self.frame = LabelFrame(self.label_frame1, text="결과")
        self.frame.pack(padx=5, pady=5, fill="x", expand=True)

        self.label4 = Label(self.frame)
        self.label4.pack(padx=0.01, pady=0.01)

        btn_cls = ttk.Button(self.label_frame1, text="초기화", command = self.clear_frame)
        btn_cls.pack(fill='x', padx=5, pady=5)

        # new file명 입력
        self.label4=tk.Label(self.label_frame1, text="[Step 4] 변경할 파일명을 입력하세요")
        self.label4.pack(fill='x', padx=5, pady=5)

        self.entry_newName=ttk.Entry(self.label_frame1, width=50, justify="center")
        self.entry_newName.pack(fill='x', padx=5, pady=5)

        # 버튼
        btn_Rename = ttk.Button(self.label_frame1, text = "파일명 변경", command = self.Rename)
        btn_Rename.pack(padx=5, pady=5)

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
                split_str_new = zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1]  # new_name
                split_str_new_list.append(split_str_new)  
                old_name_list.append(old_name + zip_files[i])
                new_name_list.append(new_name + split_str_new_list[i])

            for i in range(0, len(old_name_list)):
                os.rename(old_name_list[i], new_name_list[i])

        elif len(zip_files) == 1:
            zip_split = zip_files[0].split("-")
            # split_str_old = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]  # old_name은 split X
            split_str_new = zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1]  # new_name

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
        split_str_new = zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1]  # new_name

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
                        entry=self.entry_newName.insert(0, item)


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
            entry=self.entry_newName.insert(0, split_str_new)
            
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
                entry=self.entry_newName.insert(0, split_str_new)

            elif len(zip_files) == 1:
                # print("Diagnosis = " + zip_files[0])
                label=Label(self.frame, text="Diagnosis = " + zip_files[0]).pack()
                zip_split = zip_files[0].split("-")
                split_str_new = str(zip_files[0]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                split_str_new_list.append(split_str_new)
                entry=self.entry_newName.insert(0, split_str_new)
            
            
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
                entry=self.entry_newName.insert(0, split_str_new)

            elif len(zip_files) == 1:
                # print("Diagnosis_CV = " + zip_files[0])
                label=Label(self.frame, text="Diagnosis_CV = " + zip_files[0]).pack()
                zip_split = zip_files[0].split("-")
                split_str_new = str(zip_files[0]).replace("-"+zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                split_str_new_list.append(split_str_new)
                entry=self.entry_newName.insert(0, split_str_new)
            
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
            entry=self.entry_newName.insert(0, split_str_new)
            
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
            entry=self.entry_newName.insert(0, split_str_new)

            
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
            split_str_new = str(zip_files[0]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
            split_str_new_list.append(split_str_new)
            entry=self.entry_newName.insert(0, split_str_new)

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
            self.entry_newName.delete(0, END)

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
        self.label3=tk.Label(self.label_frame1, text="[Step 3] 버전을 확인하세요")
        self.label3.pack(fill='x', padx=5, pady=5)

        btn_versionCheck = ttk.Button(self.label_frame1, text = "버전 확인", command = self.VersionCheck)
        btn_versionCheck.pack(fill='x', padx=5, pady=5)

        # 프레임
        self.frame = LabelFrame(self.label_frame1, text="결과")
        self.frame.pack(padx=5, pady=5, fill="x", expand=True)

        self.label4 = Label(self.frame)
        self.label4.pack(padx=0.01, pady=0.01)

        btn_cls = ttk.Button(self.label_frame1, text="초기화", command = self.clear_frame)
        btn_cls.pack(fill='x', padx=5, pady=5)

        # new file명 입력
        self.label4=tk.Label(self.label_frame1, text="[Step 4] 변경할 파일명을 입력하세요")
        self.label4.pack(fill='x', padx=5, pady=5)

        self.entry_newName=ttk.Entry(self.label_frame1, width=50, justify="center")
        self.entry_newName.pack(fill='x', padx=5, pady=5)

        # 버튼
        btn_Rename = ttk.Button(self.label_frame1, text = "파일명 변경", command = self.Rename)
        btn_Rename.pack(padx=5, pady=5)

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
                    entry=self.entry_newName.insert(0, item)


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
            entry=self.entry_newName.insert(0, split_str_new)

        elif len(zip_files) == 1:
            # print("Resource = " + zip_files[0])
            label=Label(self.frame, text="Resource = " + zip_files[0]).pack()
            zip_split = zip_files[0].split("-")
            split_str_new = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]
            split_str_new_list.append(split_str_new)
            entry=self.entry_newName.insert(0, split_str_new)
        
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
                    entry=self.entry_newName.insert(0, item)

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
        entry=self.entry_newName.insert(0, split_str_new)

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
            self.entry_newName.delete(0, END)

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

            item_list = []

            # 폴더명 추출
            for item in os.listdir(file_path+app):
                sub_folder = os.path.join(file_path+app, item) # 폴더경로 + 폴더명
                if os.path.isdir(sub_folder):
                    if '.txt' not in item:
                        item_list.append(item)
                        # print("Application = " + item)
                        label=Label(self.frame, text="Application = " + item).pack()

            # 파일 열기
            with open(file_path+app+app_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
                # print("application_version_txt = " + file_content)
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

        # critical----------------------------------
        
        if "critical" in os.listdir(file_path):
            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+critical):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            split_str_new_list = []
            # ZIP 파일 목록 출력
            # print("critical = " + zip_files[0])
            zip_split = str(zip_files[0]).split("-")
            split_str_new = str(zip_files[0]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
            split_str_new_list.append(split_str_new)
            label=Label(self.frame, text="critical = " + zip_files[0]).pack()
            
            # 파일 열기
            with open(file_path+critical+critical_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
            pass_list=[]

            for i in range(0,len(split_str_new_list)):
                if split_str_new_list[i] == file_content:
                    pass_list.append("PASS")
            
            if "PASS" in pass_list :
                label=Label(self.frame, text="PASS", fg="blue").pack()
            else :
                label=Label(self.frame, text="FAIL", fg="red").pack()

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

            split_str_new_list = []
            # ZIP 파일 목록 출력
            if len(zip_files) >= 2:
                for i in range(0,len(zip_files)):
                    # print("Diagnosis = " + zip_files[i])
                    label=Label(self.frame, text="diagnosis = " + zip_files[i]).pack()
                    zip_split = zip_files[i].split("-")
                    split_str_new = str(zip_files[i]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                    split_str_new_list.append(split_str_new)

            elif len(zip_files) == 1:
                # print("Diagnosis = " + zip_files[0])
                label=Label(self.frame, text="diagnosis = " + zip_files[0]).pack()
                zip_split = zip_files[0].split("-")
                split_str_new = str(zip_files[0]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                split_str_new_list.append(split_str_new)
            
            # 파일 열기
            with open(file_path+diagnosis+diagnosis_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("diagnosis_version_txt = " + file_content)
            label=Label(self.frame, text="diagnosis_version_txt = " + file_content).pack()

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

        # diagnosis_cv----------------------------------
        
        if "diagnosis_cv" in os.listdir(file_path):
            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+diagnosis_cv):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            split_str_new_list = []
            # ZIP 파일 목록 출력
            if len(zip_files) >= 2:
                for i in range(0,len(zip_files)):
                    # print("Diagnosis_CV = " + zip_files[i])
                    label=Label(self.frame, text="diagnosis_CV = " + zip_files[i]).pack()
                    zip_split = zip_files[i].split("-")
                    split_str_new = str(zip_files[i]).replace("-"+zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                    split_str_new_list.append(split_str_new)

            elif len(zip_files) == 1:
                # print("Diagnosis_CV = " + zip_files[0])
                label=Label(self.frame, text="diagnosis_CV = " + zip_files[0]).pack()
                zip_split = zip_files[0].split("-")
                split_str_new = str(zip_files[0]).replace("-"+zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                split_str_new_list.append(split_str_new)

            # 파일 열기
            with open(file_path+diagnosis_cv+diagnosis_cv_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
            pass_list=[]

            for i in range(0,len(split_str_new_list)):
                if split_str_new_list[i] == file_content:
                    pass_list.append("PASS")
            
            if "PASS" in pass_list :
                label=Label(self.frame, text="PASS", fg="blue").pack()
            else :
                label=Label(self.frame, text="FAIL", fg="red").pack()

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

            split_str_new_list = []
            # ZIP 파일 목록 출력
            if len(zip_files) >= 2:
                for i in range(0,len(zip_files)):
                    # print("Diagnosis_CV = " + zip_files[i])
                    label=Label(self.frame, text="diagnosis_im = " + zip_files[i]).pack()
                    zip_split = zip_files[i].split("-")
                    split_str_new = str(zip_files[i]).replace("-"+zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                    split_str_new_list.append(split_str_new)

            elif len(zip_files) == 1:
                # print("Diagnosis_CV = " + zip_files[0])
                label=Label(self.frame, text="diagnosis_im = " + zip_files[0]).pack()
                zip_split = zip_files[0].split("-")
                split_str_new = str(zip_files[0]).replace("-"+zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                split_str_new_list.append(split_str_new)
            
            # 파일 열기
            with open(file_path+diagnosis_im+diagnosis_im_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
            pass_list=[]

            for i in range(0,len(split_str_new_list)):
                if split_str_new_list[i] == file_content:
                    pass_list.append("PASS")
            
            if "PASS" in pass_list :
                label=Label(self.frame, text="PASS", fg="blue").pack()
            else :
                label=Label(self.frame, text="FAIL", fg="red").pack()

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

            split_str_new_list = []
            # ZIP 파일 목록 출력
            if len(zip_files) >= 2:
                for i in range(0,len(zip_files)):
                    # print("Diagnosis_CV = " + zip_files[i])
                    label=Label(self.frame, text="os = " + zip_files[i]).pack()
                    zip_split = zip_files[i].split("-")
                    split_str_new = str(zip_files[i]).replace("-"+zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                    split_str_new_list.append(split_str_new)

            elif len(zip_files) == 1:
                # print("Diagnosis_CV = " + zip_files[0])
                label=Label(self.frame, text="os = " + zip_files[0]).pack()
                zip_split = zip_files[0].split("-")
                split_str_new = str(zip_files[0]).replace("-"+zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                split_str_new_list.append(split_str_new)
            
            # 파일 열기
            with open(file_path+gscan_os+gscan_os_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("os_version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()
            
            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
            pass_list=[]

            for i in range(0,len(split_str_new_list)):
                if split_str_new_list[i] == file_content:
                    pass_list.append("PASS")
            
            if "PASS" in pass_list :
                label=Label(self.frame, text="PASS", fg="blue").pack()
            else :
                label=Label(self.frame, text="FAIL", fg="red").pack()
            
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

            split_str_new_list = []
            # ZIP 파일 목록 출력
            # print("system = " + zip_files[0])
            label=Label(self.frame, text="system = " + zip_files[0]).pack()
            zip_split = zip_files[0].split("-")
            split_str_new = str(zip_files[0]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
            split_str_new_list.append(split_str_new)

            # 파일 열기
            with open(file_path+system+sys_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            # print("system_version_txt = " + file_content)
            label=Label(self.frame, text="Version_txt = " + file_content).pack()

            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
            pass_list=[]

            for i in range(0,len(split_str_new_list)):
                if split_str_new_list[i] == file_content:
                    pass_list.append("PASS")
            
            if "PASS" in pass_list :
                label=Label(self.frame, text="PASS", fg="blue").pack()
            else :
                # print("!!!!!!!!! FAIL !!!!!!!!!")
                label=Label(self.frame, text="FAIL", fg="red").pack()

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
        ttk.Label(self.label_frame, text="압축할 폴더").pack(anchor='w')
        self.folder_entry = ttk.Entry(self.label_frame, textvariable=self.folder_path)
        self.folder_entry.pack(fill="x")
        ttk.Button(self.label_frame, text="선택", command=self.select_folder).pack(pady=5)

        self.output_path = tk.StringVar(value=self.config['DEFAULT'].get('output_path', ''))
        ttk.Label(self.label_frame, text="출력 경로").pack(anchor='w')
        self.output_entry = ttk.Entry(self.label_frame, textvariable=self.output_path)
        self.output_entry.pack(fill="x")
        ttk.Button(self.label_frame, text="선택", command=self.select_output_folder).pack(pady=5)

        self.max_size_mb = tk.StringVar(value=self.config['DEFAULT'].get('max_size_mb', ''))
        ttk.Label(self.label_frame, text="최대 크기(MB)").pack(anchor='w')
        self.max_size_entry = ttk.Entry(self.label_frame, textvariable=self.max_size_mb)
        self.max_size_entry.pack(fill="x")

        self.file_name = tk.StringVar(value=self.config['DEFAULT'].get('file_name', ''))
        ttk.Label(self.label_frame, text="압축 파일 이름").pack(anchor='w')
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

        # 파일명 변경
        if len(file_name.split('-')[0]) == 3:  # 4세대
            date_part = file_name.split('-')[-3]
            file_version = file_name.split('-')[0] + '-' + file_name.split('-')[1] + '-' + file_name.split('-')[2]
            last_file = file_name.split('-')[-2] + '-' + file_name.split('-')[-1] + '.zip'
        
        else :  # 3세대
            if "CV" in file_name: # 상용(CV) 조건 추가
                date_part = file_name.split('-')[-4]
                last_file = file_name.split('-')[-3] + '-' + file_name.split('-')[-2] + '-' + file_name.split('-')[-1] + '.zip'
            else:
                date_part = file_name.split('-')[-3]
                last_file = file_name.split('-')[-2] + '-' + file_name.split('-')[-1] + '.zip'
            file_version = file_name.split('-')[0] + '-' + file_name.split('-')[1] + '-' + file_name.split('-')[2] + '-' + file_name.split('-')[3] + '-' + file_name.split('-')[4] + '-' + file_name.split('-')[5]

        zip_counter = int(date_part[-2:])
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
                        date_part_rep = date_part[:-2] + date_part[-2:].replace(date_part[-2:], f"{zip_counter:02d}")
                        # zip_file_name = f"{output_path}/{file_name}{zip_counter:02d}.zip"
                    else:
                        date_part_rep = date_part[:-2] + date_part[-2:].replace(date_part[-2:], f"{zip_counter:03d}")
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

        self.config = configparser.ConfigParser()
        self.config_file = 'settings.ini'
        self.load_settings()

        # 화면 가운데 위치
        window5.title("빈폴더 확인 프로그램")
        window_width = 500
        window_height = 500  # 높이 조정
        screen_width = window5.winfo_screenwidth()
        screen_height = window5.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        window5.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        self.build_ui(window5)

    def build_ui(self, window5):
        # 파일 경로 입력
        label_title = tk.Label(window5, text="*** 빈폴더 확인 프로그램 입니다 ***", fg="green", relief="groove")
        label_title.pack(fill='x', padx=5, pady=5)

        self.label_frame1 = ttk.LabelFrame(window5, text="설정")
        self.label_frame1.pack(padx=10, pady=10, fill="x", expand=True)

        self.folder_path = tk.StringVar(value=self.config['DEFAULT'].get('folder_path', ''))
        ttk.Label(self.label_frame1, text="확인할 폴더").pack(anchor='w')
        self.folder_entry = ttk.Entry(self.label_frame1, width=50, textvariable=self.folder_path)
        self.folder_entry.pack(fill="x")
        ttk.Button(self.label_frame1, text="선택", command=self.select_folder).pack(pady=5)

        btn_Check = ttk.Button(self.label_frame1, text="빈폴더 확인", command=self.main_func)
        btn_Check.pack(padx=5, pady=5)

        # 프레임
        self.frame = LabelFrame(self.label_frame1, text="결과")
        self.frame.pack(padx=5, pady=5, fill="x", expand=True)

        self.label3 = Label(self.frame)
        self.label3.pack()

        btn_cls = ttk.Button(self.label_frame1, text="초기화", command=self.clear_frame)
        btn_cls.pack(padx=5, pady=5)

    def select_folder(self):
        folder_path = filedialog.askdirectory(title="확인할 폴더 선택", initialdir=self.folder_path.get())
        if folder_path:
            self.folder_path.set(folder_path)

    def clear_frame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

    def main_func(self):
        # 폴더명 추출
        zip_files = []
        file_path = self.folder_entry.get()

        # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
        for root, dirs, files in os.walk(file_path):
            for file in files:
                if file.endswith('.zip'):
                    # 확장자가 .zip인 파일은 리스트에 추가
                    zip_files.append(os.path.join(file))

        if len(zip_files) == 1:
            for i in range(0, len(zip_files)):
                zip_file_rep = zip_files[i].replace('.zip', '')
                file_name = file_path + "\\" + zip_file_rep

                # 압축 파일 해제
                empty_folders = []
                dirsList = []
                
                for dirs in os.listdir(file_path):
                    dirsList.append(dirs)
                if zip_file_rep not in dirsList:
                    os.makedirs(file_name, exist_ok=True)  # 폴더 생성
                    # zipfile 모듈에서 빈폴더를 파일로 인식한 경우 예외 처리
                    with zipfile.ZipFile(file_path + "\\" + zip_files[i],'r') as zip_ref:
                        for member in zip_ref.infolist():
                            if (member.external_attr == 0x10) and (member.internal_attr ==1) and (member.file_size == 0):
                                member_filename = member.filename.replace('/', '\\')
                                empty_folders.append(file_path + "\\" + zip_file_rep + "\\" + member_filename)
                    zipfile.ZipFile(file_path + "\\" + zip_files[i]).extractall(file_path + "\\" + zip_file_rep)

                elif zip_file_rep in dirs:
                    shutil.rmtree(file_name)  # 폴더 전체 삭제
                    os.makedirs(file_name, exist_ok=True)  # 폴더 생성
                    zipfile.ZipFile(file_path + "\\" + zip_files[i]).extractall(file_path + "\\" + zip_file_rep)

                # 빈 파일 확인
                for (root, dirs, files) in os.walk(file_name):
                    if not dirs :
                        if not files:
                            empty_folders.append(root)

            if len(empty_folders) == 0:
                label = Label(self.frame, text="빈폴더가 없습니다", fg="blue")
                label.pack()
            else:
                for i in range(0, len(empty_folders)):
                    label = Label(self.frame, text=empty_folders[i] + " 폴더를 확인하세요", fg="red", wraplength=400)
                    label.pack()

            response = messagebox.askyesno("확인", "압축 해제한 파일을 삭제하시겠습니까?")
            if response == 1:
                for i in range(0, len(zip_files)):
                    zip_file_rep = zip_files[i].replace('.zip', '')
                    shutil.rmtree(file_path + "\\" + zip_file_rep)
                messagebox.showinfo("알림", "압축 해제한 파일이 성공적으로 삭제되었습니다.")
            else:
                messagebox.showinfo("알림", "파일 삭제가 취소되었습니다.")

        elif len(zip_files) >= 2:
            zip_file_rep = []
            empty_folders = []
            dirsList = []
            for i in range(0, len(zip_files)):
                zip_file_rep.append(zip_files[i].replace('.zip', ''))
                file_name = file_path + "\\" + zip_file_rep[i]

                # 압축 파일 해제
                for dirs in os.listdir(file_path):
                    dirsList.append(dirs)
                if zip_file_rep[i] not in dirsList:
                    os.makedirs(file_name, exist_ok=True)  # 폴더 생성
                    # zipfile 모듈에서 빈폴더를 파일로 인식한 경우 예외 처리
                    with zipfile.ZipFile(file_path + "\\" + zip_files[i],'r') as zip_ref:
                        for member in zip_ref.infolist():
                            if (member.external_attr == 0x10) and (member.internal_attr == 1) and (member.file_size == 0):
                                member_filename = member.filename.replace('/', '\\')
                                empty_folders.append(file_name + "\\" + member_filename)
                    zipfile.ZipFile(file_path + "\\" + zip_files[i]).extractall(file_name)
                    # 빈 파일 확인
                    for (root, dirs, files) in os.walk(file_path + "\\" + zip_file_rep[i]):
                        if not dirs :
                            if not files:
                                empty_folders.append(root)

                elif zip_file_rep[i] in dirs:
                    shutil.rmtree(file_name)  # 폴더 전체 삭제
                    os.makedirs(file_name, exist_ok=True)  # 폴더 생성
                    zipfile.ZipFile(file_path + "\\" + zip_files[i]).extractall(file_name)

            if len(empty_folders) == 0:
                label = Label(self.frame, text="빈폴더가 없습니다", fg="blue")
                label.pack()
            else:
                for i in range(0, len(empty_folders)):
                    label = Label(self.frame, text=empty_folders[i] + " 폴더를 확인하세요", fg="red", wraplength=400)
                    label.pack()

            response = messagebox.askyesno("확인", "압축 해제한 파일을 삭제하시겠습니까?")
            if response == 1:
                zip_file_rep = []
                for i in range(0, len(zip_files)):
                    zip_file_rep.append(zip_files[i].replace('.zip', ''))
                    file_name = file_path + "\\" + zip_file_rep[i]
                    shutil.rmtree(file_name)
                messagebox.showinfo("알림", "압축 해제한 파일이 성공적으로 삭제되었습니다.")
            else:
                messagebox.showinfo("알림", "파일 삭제가 취소되었습니다.")

    def load_settings(self):
        self.config.read(self.config_file)


class rscCheck:

    def __init__(self, window8):
        window8.title("4세대 리소스 정합성 확인 프로그램")
        # window.geometry("400x700")
        window_width = 400
        window_height = 400  # 높이 조정
        screen_width = window8.winfo_screenwidth()
        screen_height = window8.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        window8.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        self.build_ui(window8)

    def build_ui(self, window8):
        # 파일 경로 입력
        self.label_title=tk.Label(window8, text="*** 수동 취합 검증 프로그램 ***", fg="blue", relief="groove")
        self.label_title.pack(fill='x', padx=5, pady=5)

        self.label_frame1 = ttk.LabelFrame(window8, text="설정")
        self.label_frame1.pack(padx=10, pady=10, fill="x", expand=True)

        self.label1 = Label(self.label_frame1, text="확인이 필요한 항목을 선택하세요")
        self.label1.pack(anchor='w')

        # 항목값
        self.selected_item = tk.StringVar()
        items = (('Resource', '1'),
                ('System', '2'))

        # 프로젝트 선택 라디오 버튼
        for item in items:
            r = ttk.Radiobutton(
                self.label_frame1,
                text=item[0],
                value=item[1],
                variable=self.selected_item
            )
            r.pack(padx=5, pady=5)

        self.label2 = Label(self.label_frame1, text="파일 경로:")
        self.label2.pack(anchor='w')

        self.entry_filePath = ttk.Entry(self.label_frame1, width=50, justify="center")
        self.entry_filePath.pack(padx=5, pady=5)

        btn_Check = ttk.Button(self.label_frame1, text="파일 확인", command=self.main_func)
        btn_Check.pack(padx=5, pady=5)

        # 프레임
        self.frame = ttk.LabelFrame(self.label_frame1, text="Output")
        self.frame.pack(fill="x")

        self.label3 = Label(self.frame, text="")
        self.label3.pack()

        btn_cls = ttk.Button(self.label_frame1, text="초기화", command=self.clear_frame)
        btn_cls.pack(padx=5, pady=5)

    def main_func(self):

        # 변수 선언
        sqlitedb = "\\systemdb\\system"
        auxFunc = "\\AuxFunction"
        binroot = "\\BIN"

        sqlitedbList = ['ECU_mapping.sqlite', 'SoftwareInformation.sqlite', 'SpecialFunction.sqlite', 'GDSN_AUXmultilanguage.sqlite', 'GDSNmultilanguage.sqlite', 'GDSMultilanguage_CV.sqlite']
        auxFuncList = ['ECUMapping.git', 'ECUMapping.gwm']
        binrootList = ['VCI1', 'VCI2', 'VCI2W', 'VMI1', 'TPMS', 'TPMS_NEW']

        global Rsc
        file_path = self.entry_filePath.get()
        zip_files = []
        zip_files.clear()  # 리스트 초기화
        if self.selected_item.get() == '1':
            Rsc = "\\Resource" # Resource 선택 시
        elif self.selected_item.get() == '2':
            Rsc = "\\system" # system 선택 시

        # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
        for root, dirs, files in os.walk(file_path + Rsc):
            for file in files:
                if file.endswith('.zip'):
                    # 확장자가 .zip인 파일은 리스트에 추가
                    zip_files.append(os.path.join(file))

        rsc_path = file_path + Rsc
        for i in range(0, len(zip_files)):
            zip_file_rep = zip_files[i].replace('.zip', '')
            file_name = file_path + Rsc + "\\" + zip_file_rep

            # 압축 파일 해제
            dirsList = []
            for dirs in os.listdir(rsc_path):
                dirsList.append(dirs)
            if zip_file_rep not in dirsList:
                os.makedirs(file_name, exist_ok=True)  # 폴더 생성
                zipfile.ZipFile(file_path + Rsc + "\\" + zip_files[i]).extractall(file_path + Rsc + "\\" + zip_file_rep)
            elif zip_file_rep in dirs:
                shutil.rmtree(file_name)  # 폴더 전체 삭제
                os.makedirs(file_name, exist_ok=True)  # 폴더 생성
                zipfile.ZipFile(file_path + Rsc + "\\" + zip_files[i]).extractall(file_path + Rsc + "\\" + zip_file_rep)

            # sqlite, AuxFunction, BIN
            fileList_sqlite = []
            fileList_auxFunc = []
            fileList_bin = []
            for (root, dirs, files) in os.walk(file_name+sqlitedb):
                fileList_sqlite.append(files)
            for (root, dirs, files) in os.walk(file_name+auxFunc):
                fileList_auxFunc.append(files)
            # for (root, dirs, files) in os.walk(file_name+binroot):
            #     fileList_bin.append(files)

            # 파일 확인
            # Resource
            if self.selected_item.get() == '1':
                fileFail_sqlite = []
                fileFail_auxFunc = []
                fileFail_bin = []
                # sqlite
                if len(fileList_sqlite) != 0:
                    for i in range(0, len(fileList_sqlite[0])):
                        if fileList_sqlite[0][i] in sqlitedbList :
                            fileFail_sqlite.append(fileList_sqlite[0][i])
                    if len(fileFail_sqlite) != 0:
                        for j in range(0, len(fileFail_sqlite)):
                            label = Label(self.frame, text = "systemdb\system : " + fileFail_sqlite[j] + " 파일 확인!!!!!!" + '\n', fg="red").pack()
                    elif len(fileFail_sqlite) == 0:
                        label = Label(self.frame, text="systemdb\system : " + 'PASS' + '\n', fg="blue").pack()
                else:
                    pass
                # auxFunc
                if len(fileList_auxFunc) != 0:
                    for i in range(0, len(fileList_auxFunc[0])):
                        if fileList_auxFunc[0][i] in auxFuncList :
                            fileFail_auxFunc.append(fileList_auxFunc[0][i])
                    if len(fileFail_auxFunc) != 0:
                        for j in range(0, len(fileFail_auxFunc)):
                            label = Label(self.frame, text = "AuxFunction : " + fileFail_auxFunc[j] + " 파일 확인!!!!!!" + '\n', fg="red").pack()
                    elif len(fileFail_auxFunc) == 0:
                        label = Label(self.frame, text="AuxFunction : " + 'PASS' + '\n', fg="blue").pack()
                else:
                    pass
                # # BIN
                # if len(fileList_bin) != 0:
                #     for i in range(0, len(fileList_bin[0])):
                #         if fileList_bin[0][i] in binrootList :
                #             fileFail_bin.append(fileList_bin[0][i])
                #     if len(fileFail_bin) != 0:
                #         for j in range(0, len(fileFail_bin)):
                #             label = Label(frame, text = "BIN : " + fileFail_bin[j] + " 파일 확인!!!!!!" + '\n', fg="red").pack()
                #     elif len(fileFail_bin) == 0:
                #         label = Label(frame, text="BIN : " + 'PASS' + '\n', fg="blue").pack()
                # else :
                #     pass

            # System
            elif self.selected_item.get() == '2':
                fileFail_sqlite = []
                fileFail_auxFunc = []
                fileFail_bin = []
                # sqlite
                if len(fileList_sqlite) != 0:
                    for i in range(0, len(fileList_sqlite[0])):
                        if fileList_sqlite[0][i] not in sqlitedbList :
                            fileFail_sqlite.append(fileList_sqlite[0][i])
                    if len(fileFail_sqlite) != 0:
                        for j in range(0, len(fileFail_sqlite)):
                            label = Label(self.frame, text = "systemdb\system : " + fileFail_sqlite[j] + " 파일 확인!!!!!!" + '\n', fg="red").pack()
                    elif len(fileFail_sqlite) == 0: # System에 sqlite 파일이 없으면
                        label = Label(self.frame, text="systemdb\system : " + 'PASS' + '\n', fg="blue").pack()
                else :
                    pass
                # auxFunc
                if len(fileList_auxFunc) != 0:
                    for i in range(0, len(fileList_auxFunc[0])):
                        if fileList_auxFunc[0][i] not in auxFuncList :
                            fileFail_auxFunc.append(fileList_auxFunc[0][i])
                    if len(fileFail_auxFunc) != 0:
                        for j in range(0, len(fileFail_auxFunc)):
                            label = Label(self.frame, text = "AuxFunction : " + fileFail_auxFunc[j] + " 파일 확인!!!!!!" + '\n', fg="red").pack()
                    elif len(fileFail_auxFunc) == 0:
                        label = Label(self.frame, text="AuxFunction : " + 'PASS' + '\n', fg="blue").pack()
                else :
                    pass
                # # BIN
                # if len(fileList_bin) != 0:
                #     for i in range(0, len(fileList_bin[0])):
                #         if fileList_bin[0][i] not in binrootList :
                #             fileFail_bin.append(fileList_bin[0][i])
                #     if len(fileFail_bin) != 0: # BIN
                #         for j in range(0, len(fileFail_bin)):
                #             label = Label(frame, text = "BIN : " + fileFail_bin[j] + " 파일 확인!!!!!!" + '\n', fg="red").pack()
                #     elif len(fileFail_bin) == 0:
                #         label = Label(frame, text="BIN : " + 'PASS' + '\n', fg="blue").pack()
                # else :
                #     pass
            
        response = messagebox.askyesno("확인", "압축 해제한 파일을 삭제하시겠습니까?")
        if response == 1:  # 사용자가 '확인'을 클릭한 경우
            for i in range(0, len(zip_files)):
                zip_file_rep = zip_files[i].replace('.zip', '')
                shutil.rmtree(file_path + Rsc + "\\" + zip_file_rep)
            messagebox.showinfo("알림", "압축 해제한 파일이 성공적으로 삭제되었습니다.")
        else:
            messagebox.showinfo("알림", "파일 삭제가 취소되었습니다.")

    def clear_frame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

class handOperateApp:
    def __init__(self, window9):
        self.root = window9  # root를 인스턴스 변수로 저장
        self.config = configparser.ConfigParser()
        self.config_file = 'settings.ini'
        self.load_settings()

        window9.title("수동 취합 프로그램")
        window9.geometry("400x500")  # 높이 조정

        # 화면 가운데 위치
        window_width = 400
        window_height = 500  # 높이 조정
        screen_width = window9.winfo_screenwidth()
        screen_height = window9.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        window9.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        self.build_ui(window9)
        # window9.protocol("WM_DELETE_WINDOW", self.on_closing)

    def build_ui(self, window9):
        self.label_frame = ttk.LabelFrame(window9, text="설정")
        self.label_frame.pack(padx=10, pady=10, fill="x", expand=True)

        self.folder_path = tk.StringVar(value=self.config['DEFAULT'].get('folder_path', ''))
        ttk.Label(self.label_frame, text="수동 취합할 폴더").pack(anchor='w')
        self.folder_entry = ttk.Entry(self.label_frame, textvariable=self.folder_path)
        self.folder_entry.pack(fill="x")
        ttk.Button(self.label_frame, text="선택", command=self.select_folder).pack(pady=5)

        self.output_path = tk.StringVar(value=self.config['DEFAULT'].get('output_path', ''))
        ttk.Label(self.label_frame, text="출력 경로").pack(anchor='w')
        self.output_entry = ttk.Entry(self.label_frame, textvariable=self.output_path)
        self.output_entry.pack(fill="x")
        ttk.Button(self.label_frame, text="선택", command=self.select_output_folder).pack(pady=5)

        self.file_name = tk.StringVar(value=self.config['DEFAULT'].get('file_name', ''))
        ttk.Label(self.label_frame, text="압축 파일 이름").pack(anchor='w')
        self.file_name_entry = ttk.Entry(self.label_frame, textvariable=self.file_name)
        self.file_name_entry.pack(fill="x")

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(window9, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(padx=10, pady=10, fill="x")

        ttk.Button(window9, text="수동 취합 시작", command=self.start_handOperate).pack(pady=20)

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
        self.window9.update_idletasks()  # root 대신 self.root 사용

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
        self.window9.destroy()

class korea:

    def __init__(self, window6):
        window6.title("업데이트 문서 자동 작성 프로그램")
        # window1.geometry("400x700")
        window_width = 400
        window_height = 700  # 높이 조정
        screen_width = window6.winfo_screenwidth()
        screen_height = window6.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        window6.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        self.build_ui(window6)       

    def build_ui(self, window6):
        self.label_title=Label(window6, text="*** [한국] 업데이트 문서 자동 작성 프로그램 입니다 ***", fg="purple", relief="groove")
        self.label_title.pack(fill='x', padx=5, pady=5)

        self.label_frame1 = ttk.LabelFrame(window6, text="설정")
        self.label_frame1.pack(padx=10, pady=10, fill="x", expand=True)

        # 계정 정보 입력
        self.label_id=ttk.Label(self.label_frame1, text="아이디 : ")
        self.label_id.pack(anchor='w')

        self.entry_id = ttk.Entry(self.label_frame1, width=50, justify="center")
        self.entry_id.pack(padx=5, pady=5)

        self.label_pw=ttk.Label(self.label_frame1, text="비밀번호 : ")
        self.label_pw.pack(anchor='w')

        self.entry_pw = ttk.Entry(self.label_frame1, width=50, justify="center")
        self.entry_pw.pack(padx=5, pady=5)

        # 현대/기아 선택
        self.label_project=ttk.Label(self.label_frame1, text="현대/기아 중 선택")
        self.label_project.pack(anchor='w')

        # 라디오 버튼
        self.selected_item1 = tk.StringVar()
        items = (('현대', '1'),
                ('기아', '2'))

        # 라디오 버튼을 팩에 배치
        for item in items:
            r = ttk.Radiobutton(
                self.label_frame1,
                text=item[0],
                value=item[1],
                variable=self.selected_item1
            )
            # 팩에 배치
            r.pack(padx=5, pady=5)

        # 센터/협력사 선택
        self.label_gbn=ttk.Label(self.label_frame1, text="센터/협력사 중 선택")
        self.label_gbn.pack(anchor='w')

        # 라디오 버튼
        self.selected_item2 = tk.StringVar()
        items = (('센터', '1'),
                ('협력사', '2'))

        # 라디오 버튼을 팩에 배치
        for item in items:
            r = ttk.Radiobutton(
                self.label_frame1,
                text=item[0],
                value=item[1],
                variable=self.selected_item2
            )
            # 팩에 배치
            r.pack(padx=5, pady=5)

        self.label_frame2=ttk.Label(self.label_frame1, text="[GIMS 이슈 번호 입력]")
        self.label_frame2.pack(anchor='w')

        # GIMS 이슈 번호 입력
        self.label_gims1=ttk.Label(self.label_frame1, text="1) 승용 : ")
        self.label_gims1.pack(anchor='w')

        self.entry_gims1 = ttk.Entry(self.label_frame1, width=50, justify="center")
        self.entry_gims1.pack(padx=5, pady=5)

        self.label_gims2=ttk.Label(self.label_frame1, text="2) 상용 : ")
        self.label_gims2.pack(anchor='w')

        self.entry_gims2 = ttk.Entry(self.label_frame1, width=50, justify="center")
        self.entry_gims2.pack(padx=5, pady=5)

        self.label_gims3=ttk.Label(self.label_frame1, text="3) ECU 업그레이드 : ")
        self.label_gims3.pack(anchor='w')

        self.entry_gims3 = ttk.Entry(self.label_frame1, width=50, justify="center")
        self.entry_gims3.pack(padx=5, pady=5)

        # 저장 파일 경로
        self.label_filePath=ttk.Label(self.label_frame1, text="저장 파일 경로 : ")
        self.label_filePath.pack(anchor='w')

        self.entry_filePath = ttk.Entry(self.label_frame1, width=50, justify="center")
        self.entry_filePath.pack(padx=5, pady=5)

        Btn = ttk.Button(self.label_frame1, text="시작...", command=self.main_func).pack(pady=5)

    def main_func(self):

        # # 현대/기아 선택
        # project = input("현대/기아 중 선택해주세요[현대 or 기아 로 입력] : ")
        if self.selected_item1.get() == '1':
            project = '현대'
        elif self.selected_item1.get() == '2':
            project = '기아'

        # # 서비스센터/협력사 선택
        # customer = input("센터/협력사 중 선택해주세요[센터 or 협력사 로 입력] :")
        if self.selected_item2.get() == '1':
            customer = '센터'
        elif self.selected_item2.get() == '2':
            customer = '협력사'

        # # ticket 기반
        ticket = 'https://gims.gitauto.com:8080/jira/browse/'
        # issue1 = input('진단에 넣을 승용 GIMS 이슈 번호를 입력하세요 : ')
        issue1 = self.entry_gims1.get()
        result_url1 = ticket + issue1
        # issue2 = input('진단에 넣을 상용 GIMS 이슈 번호를 입력하세요 : ')
        issue2 = self.entry_gims2.get()
        result_url2 = ticket + issue2
        # issue_ecu = input('ECU 업그레이드에 넣을 GIMS 이슈 번호를 입력하세요 : ')
        issue_ecu = self.entry_gims3.get()
        ecu_url = ticket + issue_ecu

        # 현대와 기아 결과값 나누기
        return_list = self.result_out(result_url1, result_url2, ecu_url)

        result = return_list[0]
        num_res = result.find('KMC')
        if (project == '현대' and customer == '센터') :
            result = result[:num_res-1]
        elif (project == '기아' and customer == '센터') :
            result = result[num_res-1:]
        else :
            result = result

        ecu = return_list[1]
        num_ecu = ecu.find('KMC')
        if (project == '현대' and customer == '센터'):
            ecu = ecu[:num_ecu-1]
        elif (project == '기아' and customer == '센터'):
            ecu = ecu[num_ecu-1:]
        else :
            ecu = ecu

        #연구소 내부 공유 삭제
        if (result.find('연구소 내부') != -1) :
            num_res2 = result.find('연구소 내부')
            result = result[:num_res2-1] + result[num_res-1:]
        else : 
            result = result

        if (ecu.find('연구소 내부') != -1) :
            num_ecu2 = ecu.find('연구소 내부')
            ecu = ecu[:num_ecu2-1] + ecu[num_ecu-1:]
        else :
            ecu = ecu

        # 이미지 로고
        if (project == '현대') :
            GITimg = "https://image.gitauto.com/gitauto/kor/popup/logo_gdssmart_test_bang.png"
            GITstring = "GDS SMART를"
        elif(project == '기아') :
            GITimg = "https://image.gitauto.com/gitauto/kor/popup/logo_kds_2_test_bang.png"
            GITstring = "KDS 2.0을"

        # html 결과문
        
        updateCss = """  
        <br>
        <br>
        <div> <!-- 업데이트 문서 시작 -->
        <style>
            
            /* 상단 img 속성*/
            .GITimg {
            color: #555;
            display: flex;
            align-items: center; /* 가운데 정렬 */
            text-align: left;
            margin-left: 10%;
            margin-right: 10%;
            }
            
            /* 목차 */
            .GITContents {
            margin: 10px;
            margin-left: 10%;
            font-size: 18px;
            }
            
            /* 상단 안내문 */
            .GITstring {
            margin: 10px;
            margin-left: 10%;
            margin-right: 10%;
            font-size: 15px;
            }

            /*GIT 표 제목*/
            .GITth {
            background-color: #ddd;
            color: #555;
            padding: 11px;
            border-bottom: 1px solid #ddd;
            border-right: 1px solid #d6d4d4;
            }
            
            /*GIT 표 내용*/
            .GITtd1 {
            padding: 11px;
            text-align: left;
            padding-left: 20px;
            line-height: 1.5; /* 행간을 조절할 수 있음, 필요에 따라 조절 가능 */
            font-size: 15px;
            border-bottom: 1px solid #ddd;
            border-right: 1px solid #ddd;
            }
            
            .GITtd2 {
            padding: 11px;
            text-align: center;
            padding-left: 20px;
            line-height: 1.5; /* 행간을 조절할 수 있음, 필요에 따라 조절 가능 */
            font-size: 15px;
            border-bottom: 1px solid #ddd;
            border-right: 1px solid #ddd;
            }
            
            /*GIT 버전 정보 표 내용*/
            .GITtd_version {
            font-size: 15px;
            margin-bottom: 10px;
            }
            
            
            /* 동그라미 */
            .version-symbol {
            font-size: 1em;
            color: #333;
            }
            
            /* 네모 */
            .square-bullet {
            display: inline-block;
            width: 10px; /* 네모의 너비 조절 */
            height: 10px; /* 네모의 높이 조절 */
            background-color: #333; /* 네모의 배경색 지정 */
            margin-right: 5px; /* 네모와 텍스트 사이의 간격 조절 */
            }
            
            /* 첫 번째 표 스타일 */
            table#GITversion-table th {
            background-color: #ddd;
            color: #555;
            width: 50%;
            text-align: center;
            }

            table#GITversion-table {
            background-color: #ffffff;
            width: 80%;
            margin: 20px auto;
            border-collapse: collapse;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }

            /* 두 번째 표 스타일 */
            table#GITupdate-table th {
            background-color: #ddd;
            color: #555;
            text-align: center;
            }

            table#GITupdate-table {
            background-color: #ffffff;
            width: 80%;
            margin: 20px auto;
            border-collapse: collapse;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
        </style>

        """	

        html_output = updateCss + """
        <p class="GITimg"><img src=""" + GITimg + """ alt="Logo" style="width: 197px; height: 29px"></p>  
        <br>
        <p class="GITContents"><span class="square-bullet"></span><strong> 버전 정보</strong></p>
        <table id="GITversion-table">
            <tr>
            <th class="GITth">업데이트 버전</th>
            <th class="GITth">펌웨어</th>
            </tr>
                <!-- 수작업 필요 -->
            <tr>
            <td class="GITtd1">
            <p class="GITtd_version"><span class="version-symbol">&#8226;</span> 프로그램 : NSH-01-0138 </p>
            <p class="GITtd_version"><span class="version-symbol">&#8226;</span> 리소스 : NSH-01-0157 </p>
            <p class="GITtd_version"><span class="version-symbol">&#8226;</span> 시스템 : NSH-01-0125 </p>
            <p class="GITtd_version"><span class="version-symbol">&#8226;</span> 서포트 앱 : NSH-01-0006 </p>
            </td>
            <td class="GITtd1">
            <p class="GITtd_version"><span class="version-symbol">&#8226;</span> VCI II : 2.86 </p>
            <p class="GITtd_version"><span class="version-symbol">&#8226;</span> VCI III : 00.42 </p>
            <p class="GITtd_version"><span class="version-symbol">&#8226;</span> GDS VCI : 1.41 </p>
            <p class="GITtd_version"><span class="version-symbol">&#8226;</span> TPMS : 3.4 </p>
            </td>
            </tr>
            <!-- 추가 업데이트 항목을 필요에 따라 계속해서 추가하세요. -->
        </table>
        <br>
        <p class="GITContents"><span class="square-bullet"></span><strong> 업데이트 정보</strong></p>
        
        <table id="GITupdate-table">
            <tr>
            <th class="GITth">구분</th>
            <th class="GITth">상세 내역</th>
            </tr>
            <tr>
            <td class="GITtd2">프로그램</td>
            <td class="GITtd1">펌웨어 업데이트 : VCI III 00.42</td>
            </tr>
            <tr>
            <td class="GITtd2">진단</td>
            <td class="GITtd1">
                """ + result + """
            </td>
            </tr>
            <tr>
            <td class="GITtd2">ECU 업데이트</td>
            <td class="GITtd1">
            """+ ecu +"""
            </td>
            </tr>
        </table>
        <br>
        <p class="GITimg"><img src="https://image.gitauto.com/gitauto/kor/common/top_logo.png" alt="logo"></p>
        <br>
        <br>
        </div>


        """


        file_path = self.entry_filePath.get()

        if project == '현대' and customer == '센터':
            file_name = '하이테크센터 현대.html'
        elif project == '현대' and customer == '협력사':
            file_name = '블루핸즈 현대.html'
        elif project == '기아' and customer == '센터':
            file_name = '기아 서비스 센터.html'
        elif project == '기아' and customer == '협력사':
            file_name = '기아 협력사.html'

        self.printsave(html_output)

        self.info()

        return

    # 진단
    def result_out(self, result_url1, result_url2, ecu_url) :

        # 웹크롤링
        # Check if chrome driver is installed or not
        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
        # driver_path = f'./{chrome_ver}/chromedriver.exe'
        driver_path = 'Z:\chromedriver\120\chromedriver.exe'

        # if os.path.exists(driver_path):
        # 	print(f"chrome driver is insatlled: {driver_path}")

        # else:
        # 	print(f"install the chrome driver(ver: {chrome_ver})")
        # 	chromedriver_autoinstaller.install(True)


        if getattr(sys, 'frozen', False) and hasattr(sys, "_MEIPASS"):
            driver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
            driver = webdriver.Chrome()
        # print('running in a Pyinstaller bundle')
        else:
            driver = webdriver.Chrome()
            # print('running in a normal Python process')

        # 계정 입력
        # id = input("아이디를 입력하세요 : ")
        id = self.entry_id.get()
        # pw = input("비밀번호를 입력하세요 : ")
        pw = self.entry_pw.get()

        # 크롤링 시작
        driver.get('https://gims.gitauto.com:8080/jira/browse/GDSN-10324')

        eId = driver.find_element(By.XPATH, "//input[@name='os_username']").send_keys(id)
        ePw = driver.find_element(By.XPATH, "//input[@name='os_password']").send_keys(pw)
        loginBtn = driver.find_element(By.NAME, 'login').click()

        time.sleep(3)

        #-------------------------------------------------------------------------------

        # # 현대/기아 선택
        # project = input("현대/기아 중 선택해주세요[현대 or 기아 로 입력] : ")
        if self.selected_item1.get() == '1':
            project = '현대'
        elif self.selected_item1.get() == '2':
            project = '기아'

        # # 서비스센터/협력사 선택
        # customer = input("센터/협력사 중 선택해주세요[센터 or 협력사 로 입력] :")
        if self.selected_item2.get() == '1':
            customer = '센터'
        elif self.selected_item2.get() == '2':
            customer = '협력사'

        # driver = webdriver.Chrome()

        if (project == '현대' and customer == '협력사') or (project == '기아' and customer == '협력사'):
            # selenium
            driver.get(result_url1)
            
            # Beautiful Soup - Jira 티켓 내부 값 불러오기
            html = driver.page_source
            soup = bs(html, "html.parser")
            html = soup.select('div.user-content-block')

            list1 = []
            for text in html:
                list1.append(text.get_text())
            
            time.sleep(3)
            
            driver.get(result_url2)

            # Beautiful Soup - Jira 티켓 내부 값 불러오기
            html = driver.page_source
            soup = bs(html, "html.parser")
            html = soup.select('div.user-content-block')

            list2 = []
            for text in html:
                list2.append(text.get_text())
            
            list = list1+list2

            # 티켓 내부 값 에서 줄바꿈표시를 <br>로 변경
            list_res = list[0].replace('\n', '<br>') + list[1].replace('\n', '<br>')
            list_res = list_res.replace('\xa0', '')

        
        elif (project == '현대' and customer == '센터') or (project == '기아' and customer == '센터'):
            # selenium
            driver.get(result_url1)
            
            # Beautiful Soup - Jira 티켓 내부 값 불러오기
            html = driver.page_source
            soup = bs(html, "html.parser")
            html = soup.select('div.user-content-block')

            list = []
            for text in html:
                list.append(text.get_text())

            # 티켓 내부 값 에서 줄바꿈표시를 <br>로 변경
            list_res = list[0].replace('\n', '<br>')
            list_res = list_res.replace('\xa0', '')

        time.sleep(3)

        # selenium
        driver.get(ecu_url)

        time.sleep(3)

        # Beautiful Soup - Jira 티켓 내부 값 불러오기
        html = driver.page_source
        soup = bs(html, "html.parser")
        html = soup.select('div.user-content-block')

        list = []
        for text in html:
                # print(text.get_text())
            list.append(text.get_text())

        # 티켓 내부 값 에서 줄바꿈표시를 <br>로 변경
        list_ecu = list[0].replace('\n', '<br>')
        list_ecu = list_ecu.replace('\xa0', '')

        time.sleep(3)

        driver.close()

        return list_res, list_ecu

    # html 파일로 저장
    def printsave(self, *a):

        file_path = self.entry_filePath.get() + "\\"

        # 현대/기아 선택
        # project = input("현대/기아 중 선택해주세요[현대 or 기아 로 입력] : ")
        if self.selected_item1.get() == '1':
            project = '현대'
        elif self.selected_item1.get() == '2':
            project = '기아'

        # 서비스센터/협력사 선택
        # customer = input("센터/협력사 중 선택해주세요[센터 or 협력사 로 입력] :")
        if self.selected_item2.get() == '1':
            customer = '센터'
        elif self.selected_item2.get() == '2':
            customer = '협력사'

        if project == '현대' and customer == '센터':
            file_name = '하이테크센터 현대.html'
        elif project == '현대' and customer == '협력사':
            file_name = '블루핸즈 현대.html'
        elif project == '기아' and customer == '센터':
            file_name = '기아 서비스 센터.html'
        elif project == '기아' and customer == '협력사':
            file_name = '기아 협력사.html'

        # 내수 고객사별 정리
        file = open(file_path+file_name, 'a', encoding='UTF-8')
        # print(*a)
        print(*a,file=file)
        file.close()

        return

    # 메시지 박스
    def info(self):
        messagebox.showinfo("알림", "html 파일 생성 완료!")

class world:
    def __init__(self, window7):
        window7.title("업데이트 문서 자동 작성 프로그램")
        window7_width = 400
        window7_height = 750  # 높이 조정
        screen_width = window7.winfo_screenwidth()
        screen_height = window7.winfo_screenheight()
        center_x = int(screen_width / 2 - window7_width / 2)
        center_y = int(screen_height / 2 - window7_height / 2)
        window7.geometry(f"{window7_width}x{window7_height}+{center_x}+{center_y}")

        self.build_ui(window7)
    
    def build_ui(self, window7):
        label_title=Label(window7, text="*** [해외] 업데이트 문서 자동 작성 프로그램 입니다 ***", fg="purple", relief="groove")
        label_title.pack(fill='x', padx=5, pady=5)

        label_frame1 = ttk.LabelFrame(window7, text="설정")
        label_frame1.pack(padx=10, pady=10, fill="x", expand=True)

        # 계정 정보 입력
        label_id=ttk.Label(label_frame1, text="아이디 : ")
        label_id.pack(anchor='w')

        entry_id = ttk.Entry(label_frame1, width=50, justify="center")
        entry_id.pack(padx=5, pady=5)

        label_pw=ttk.Label(label_frame1, text="비밀번호 : ")
        label_pw.pack(anchor='w')

        entry_pw = ttk.Entry(label_frame1, width=50, justify="center")
        entry_pw.pack(padx=5, pady=5)

        # 북미/유럽/중국 선택
        label_gbn=ttk.Label(label_frame1, text="미국/캐나다/유럽/중국 중 선택")
        label_gbn.pack(anchor='w')

        # 라디오 버튼
        selected_item2 = tk.StringVar()
        items = (('미국', '1'),
                ('캐나다', '2'),
                ('유럽', '3'),
                ('중국', '4'),
                ('미국령', '5'))

        # 라디오 버튼을 팩에 배치
        for item in items:
            r = ttk.Radiobutton(
                label_frame1,
                text=item[0],
                value=item[1],
                variable=selected_item2
            )
            # 팩에 배치
            r.pack(padx=5, pady=5)

        # 현대/기아/제네시스 선택
        label_project=ttk.Label(label_frame1, text="현대/기아/제네시스 중 선택")
        label_project.pack(anchor='w')

        # 라디오 버튼
        selected_item1 = tk.StringVar()
        items = (('현대', '1'),
                ('기아', '2'),
                ('제네시스', '3'))

        # 라디오 버튼을 팩에 배치
        for item in items:
            r = ttk.Radiobutton(
                label_frame1,
                text=item[0],
                value=item[1],
                variable=selected_item1
            )
            # 팩에 배치
            r.pack(padx=5, pady=5)

        label_frame2=ttk.Label(label_frame1, text="[GIMS 이슈 번호 입력]")
        label_frame2.pack(anchor='w')

        # GIMS 이슈 번호 입력
        label_gims1=ttk.Label(label_frame1, text="1) 승용 : ")
        label_gims1.pack(anchor='w')

        entry_gims1 = ttk.Entry(label_frame1, width=50, justify="center")
        entry_gims1.pack(padx=5, pady=5)

        label_gims2=ttk.Label(label_frame1, text="2) 상용 : ")
        label_gims2.pack(anchor='w')

        entry_gims2 = ttk.Entry(label_frame1, width=50, justify="center")
        entry_gims2.pack(padx=5, pady=5)

        label_gims3=ttk.Label(label_frame1, text="3) ECU 업그레이드 : ")
        label_gims3.pack(anchor='w')

        entry_gims3 = ttk.Entry(label_frame1, width=50, justify="center")
        entry_gims3.pack(padx=5, pady=5)

        # 저장 파일 경로
        label_filePath=ttk.Label(label_frame1, text="저장 파일 경로 : ")
        label_filePath.pack(anchor='w')

        entry_filePath = ttk.Entry(label_frame1, width=50, justify="center")
        entry_filePath.pack(padx=5, pady=5)

        Btn = ttk.Button(label_frame1, text="시작...", command=self.main_func).pack(pady=5)

    def main_func(self):

        # 현대/기아/제네시스 선택
        if self.selected_item1.get() == '1':
            project = '현대'
        elif self.selected_item1.get() == '2':
            project = '기아'
        elif self.selected_item1.get() == '3':
            project = '제네시스'

        # 북미/유럽/중국 선택
        if self.result_outselected_item2.get() == '1':
            country = '미국'
        elif self.selected_item2.get() == '2':
            country = '캐나다'
        elif self.selected_item2.get == '3':
            country = '유럽'
        elif self.selected_item2.get() == '4':
            country = '중국'
        elif self.selected_item2.get == '5':
            country = '미국령'

        # # ticket 기반
        ticket = 'https://gims.gitauto.com:8080/jira/browse/'
        # issue1 = input('진단에 넣을 승용 GIMS 이슈 번호를 입력하세요 : ')
        issue1 = self.entry_gims1.get()
        result_url1 = ticket + issue1

        issue2 = self.entry_gims2.get()
        result_url2 = ticket + issue2

        # issue_ecu = input('ECU 업그레이드에 넣을 GIMS 이슈 번호를 입력하세요 : ')
        issue_ecu = self.entry_gims3.get()
        ecu_url = ticket + issue_ecu

        # result_out 함수 실행
        return_list = self.result_out(result_url1, result_url2, ecu_url)
        result = return_list[0]
        ecu = return_list[1]


        # 이미지 로고
        if (project == '현대') :
            GITimg = "https://image.gitauto.com/gitauto/kor/popup/logo_gdssmart_test_bang.png"
            GITstring = "GDS SMART를"
        elif(project == '기아') :
            GITimg = "https://image.gitauto.com/gitauto/kor/popup/logo_kds_2_test_bang.png"
            GITstring = "KDS 2.0을"
        elif(project == '제네시스') :
            GITimg = "https://image.gitauto.com/gitauto/kor/popup/logo_genesissmart_test_bang.png"
            GITstring = "Genesis Smart를"

        # html 결과문
        
        updateCss = """  
        <br>
        <br>
        <div> <!-- 업데이트 문서 시작 -->
        <style>
            
            /* 상단 img 속성*/
            .GITimg {
            color: #555;
            display: flex;
            align-items: center; /* 가운데 정렬 */
            text-align: left;
            margin-left: 10%;
            margin-right: 10%;
            }
            
            /* 목차 */
            .GITContents {
            margin: 10px;
            margin-left: 10%;
            font-size: 18px;
            }
            
            /* 상단 안내문 */
            .GITstring {
            margin: 10px;
            margin-left: 10%;
            margin-right: 10%;
            font-size: 15px;
            }

            /*GIT 표 제목*/
            .GITth {
            background-color: #ddd;
            color: #555;
            padding: 11px;
            border-bottom: 1px solid #ddd;
            border-right: 1px solid #d6d4d4;
            }
            
            /*GIT 표 내용*/
            .GITtd1 {
            padding: 11px;
            text-align: left;
            padding-left: 20px;
            line-height: 1.5; /* 행간을 조절할 수 있음, 필요에 따라 조절 가능 */
            font-size: 15px;
            border-bottom: 1px solid #ddd;
            border-right: 1px solid #ddd;
            }
            
            .GITtd2 {
            padding: 11px;
            text-align: center;
            padding-left: 20px;
            line-height: 1.5; /* 행간을 조절할 수 있음, 필요에 따라 조절 가능 */
            font-size: 15px;
            border-bottom: 1px solid #ddd;
            border-right: 1px solid #ddd;
            }
            
            /*GIT 버전 정보 표 내용*/
            .GITtd_version {
            font-size: 15px;
            margin-bottom: 10px;
            }
            
            
            /* 동그라미 */
            .version-symbol {
            font-size: 1em;
            color: #333;
            }
            
            /* 네모 */
            .square-bullet {
            display: inline-block;
            width: 10px; /* 네모의 너비 조절 */
            height: 10px; /* 네모의 높이 조절 */
            background-color: #333; /* 네모의 배경색 지정 */
            margin-right: 5px; /* 네모와 텍스트 사이의 간격 조절 */
            }
            
            /* 첫 번째 표 스타일 */
            table#GITversion-table th {
            background-color: #ddd;
            color: #555;
            width: 50%;
            text-align: center;
            }

            table#GITversion-table {
            background-color: #ffffff;
            width: 80%;
            margin: 20px auto;
            border-collapse: collapse;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }

            /* 두 번째 표 스타일 */
            table#GITupdate-table th {
            background-color: #ddd;
            color: #555;
            text-align: center;
            }

            table#GITupdate-table {
            background-color: #ffffff;
            width: 80%;
            margin: 20px auto;
            border-collapse: collapse;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
        </style>

        """	

        html_output = updateCss + """
        <p class="GITimg"><img src=""" + GITimg + """ alt="Logo" style="width: 197px; height: 29px"></p>  
        <br>
        <p class="GITContents"><span class="square-bullet"></span><strong> 버전 정보</strong></p>
        <table id="GITversion-table">
            <tr>
            <th class="GITth">업데이트 버전</th>
            <th class="GITth">펌웨어</th>
            </tr>
                <!-- 수작업 필요 -->
            <tr>
            <td class="GITtd1">
            <p class="GITtd_version"><span class="version-symbol">&#8226;</span> 프로그램 : NSH-01-0138 </p>
            <p class="GITtd_version"><span class="version-symbol">&#8226;</span> 리소스 : NSH-01-0157 </p>
            <p class="GITtd_version"><span class="version-symbol">&#8226;</span> 시스템 : NSH-01-0125 </p>
            <p class="GITtd_version"><span class="version-symbol">&#8226;</span> 서포트 앱 : NSH-01-0006 </p>
            </td>
            <td class="GITtd1">
            <p class="GITtd_version"><span class="version-symbol">&#8226;</span> VCI II : 2.86 </p>
            <p class="GITtd_version"><span class="version-symbol">&#8226;</span> VCI III : 00.42 </p>
            <p class="GITtd_version"><span class="version-symbol">&#8226;</span> GDS VCI : 1.41 </p>
            <p class="GITtd_version"><span class="version-symbol">&#8226;</span> TPMS : 3.4 </p>
            </td>
            </tr>
            <!-- 추가 업데이트 항목을 필요에 따라 계속해서 추가하세요. -->
        </table>
        <br>
        <p class="GITContents"><span class="square-bullet"></span><strong> 업데이트 정보</strong></p>
        
        <table id="GITupdate-table">
            <tr>
            <th class="GITth">구분</th>
            <th class="GITth">상세 내역</th>
            </tr>
            <tr>
            <td class="GITtd2">프로그램</td>
            <td class="GITtd1">펌웨어 업데이트 : VCI III 00.42</td>
            </tr>
            <tr>
            <td class="GITtd2">진단</td>
            <td class="GITtd1">
                """ + result + """
            </td>
            </tr>
            <tr>
            <td class="GITtd2">ECU 업데이트</td>
            <td class="GITtd1">
            """+ ecu +"""
            </td>
            </tr>
        </table>
        <br>
        <p class="GITimg"><img src="https://image.gitauto.com/gitauto/kor/common/top_logo.png" alt="logo"></p>
        <br>
        <br>
        </div>


        """

        file_path = self.entry_filePath.get()

        self.printsave(html_output)

        self.info()

        return


    def result_out(self, result_url1, result_url2, ecu_url) :

        # 웹크롤링
        # Check if chrome driver is installed or not
        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
        # driver_path = f'./{chrome_ver}/chromedriver.exe'
        driver_path = 'Z:\chromedriver\120\chromedriver.exe'


        if getattr(sys, 'frozen', False) and hasattr(sys, "_MEIPASS"):
            driver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
            driver = webdriver.Chrome()
        # print('running in a Pyinstaller bundle')
        else:
            driver = webdriver.Chrome()
            # print('running in a normal Python process')

        # 계정 입력
        # id = input("아이디를 입력하세요 : ")
        id = self.entry_id.get()
        # pw = input("비밀번호를 입력하세요 : ")
        pw = self.entry_pw.get()

        # 크롤링 시작
        driver.get('https://gims.gitauto.com:8080/jira/browse/GDSN-10324')

        eId = driver.find_element(By.XPATH, "//input[@name='os_username']").send_keys(id)
        ePw = driver.find_element(By.XPATH, "//input[@name='os_password']").send_keys(pw)
        loginBtn = driver.find_element(By.NAME, 'login').click()

        time.sleep(3)

        #-------------------------------------------------------------------------------

        # # 현대/기아 선택
        # project = input("현대/기아 중 선택해주세요[현대 or 기아 로 입력] : ")
        if self.selected_item1.get() == '1':
            project = '현대'
        elif self.selected_item1.get() == '2':
            project = '기아'
        elif self.selected_item1.get() == '3':
            project = '제네시스'

        # driver = webdriver.Chrome()

        if "GDSN" in result_url2:
            # selenium
            driver.get(result_url1)
            
            # Beautiful Soup - Jira 티켓 내부 값 불러오기
            html = driver.page_source
            soup = bs(html, "html.parser")
            html = soup.select('div.user-content-block')

            list1 = []
            for text in html:
                list1.append(text.get_text())
            
            time.sleep(3)
            
            driver.get(result_url2)

            # Beautiful Soup - Jira 티켓 내부 값 불러오기
            html = driver.page_source
            soup = bs(html, "html.parser")
            html = soup.select('div.user-content-block')

            list2 = []
            for text in html:
                list2.append(text.get_text())
            
            list = list1+list2

            # 티켓 내부 값 에서 줄바꿈표시를 <br>로 변경
            list_res = list[0].replace('\n', '<br>') + list[1].replace('\n', '<br>')
            list_res = list_res.replace('\xa0', '')

        
        elif "GDSN" not in result_url2:
            # selenium
            driver.get(result_url1)
            
            # Beautiful Soup - Jira 티켓 내부 값 불러오기
            html = driver.page_source
            soup = bs(html, "html.parser")
            html = soup.select('div.user-content-block')

            list = []
            for text in html:
                list.append(text.get_text())

            # 티켓 내부 값 에서 줄바꿈표시를 <br>로 변경
            list_res = list[0].replace('\n', '<br>')
            list_res = list_res.replace('\xa0', '')

        time.sleep(3)

        # selenium
        driver.get(ecu_url)

        time.sleep(3)
        
        # ECU 업그레이드
        # 연결된 issue 없을 경우 null 값으로 처리
        if "GDSN" in ecu_url:
            # Beautiful Soup - Jira 티켓 내부 값 불러오기
            html = driver.page_source
            soup = bs(html, "html.parser")
            html = soup.select('div.user-content-block')

            list = []
            for text in html:
                    # print(text.get_text())
                list.append(text.get_text())

            # 티켓 내부 값 에서 줄바꿈표시를 <br>로 변경
            list_ecu = list[0].replace('\n', '<br>')
            list_ecu = list_ecu.replace('\xa0', '')
        
        elif "GDSN" not in ecu_url:
            list_ecu = ""

        time.sleep(3)

        driver.close()

        return list_res, list_ecu


    # html 파일로 저장
    def printsave(self, *a):

        file_path = self.entry_filePath.get() + "\\"

        # 현대/기아 선택
        # project = input("현대/기아 중 선택해주세요[현대 or 기아 로 입력] : ")
        if self.selected_item1.get() == '1':
            project = '현대'
        elif self.selected_item1.get() == '2':
            project = '기아'
        elif self.selected_item1.get() == '3':
            project = '제네시스'

        # 북미/유럽/중국 선택
        if self.selected_item2.get() == '1':
            country = '미국'
        elif self.selected_item2.get() == '2':
            country = '캐나다'
        elif self.selected_item2.get == '3':
            country = '유럽'
        elif self.selected_item2.get() == '4':
            country = '중국'
        elif self.selected_item2.get == '5':
            country = '미국령'

        # # ticket 기반
        ticket = 'https://gims.gitauto.com:8080/jira/browse/'
        issue2 = self.entry_gims2.get()
        result_url2 = ticket + issue2

        # 북미
        if country == '미국' and project == '제네시스' :	
            file_name = 'GMA-PA.html'
        elif country == '미국' and project == '현대' :
            file_name = 'HMA-PA.html'
        elif country == '미국' and project == '기아':
            file_name = 'KMA-PA.html'
        elif country == '캐나다' and project == '현대' :
            file_name = 'HAC-PA.html'
        elif country == '캐나다' and project == '기아':
            file_name = 'KCI-PA.html'

        # 유럽
        if country == '유럽' and project == '제네시스' :	
            file_name = 'GME-PA.html'
        elif country == '유럽' and project == '현대' :
            if "GDSN" not in result_url2:	# 승용
                file_name = 'HME-PA.html'
            elif "GDSN" in result_url2: # 상용
                file_name = 'HME-CV.html'
        elif country == '유럽' and project == '기아':
            file_name = 'KME-PA.html'

        # 미국령
        if country == '미국령' and project == '현대':
            file_name = 'HMU-PA.html'
        elif country == '미국령' and project == '기아':
            file_name = 'KMU-PA.html'

        # 중국
        if country == '중국' and project == '현대':
            if "GDSN" not in result_url2:	# 승용
                file_name = 'HBHMC-PA.html'
            elif "GDSN" in result_url2: # 상용
                file_name = 'HS-CV.html'
        elif country == '중국' and project == '기아':
            file_name = 'KDYKMC-PA.html'
        elif country == '중국' and project == '제네시스':
            file_name = 'GMC-PA.html'

        # 내수 고객사별 정리
        file = open(file_path+file_name, 'a', encoding='UTF-8')
        # print(*a)
        print(*a,file=file)
        file.close()

        return

    # 메시지 박스
    def info():
        messagebox.showinfo("알림", "html 파일 생성 완료!")



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

def createNewWindow8():
    window8 = tk.Toplevel(mainWindow)
    app = rscCheck(window8)
    window8.mainloop()

def createNewWindow9():
    window9 = tk.Toplevel(mainWindow)
    app = handOperateApp(window9)
    window9.mainloop()

#-- 업데이트 문서 --
def createNewWindow6():
    window6 = tk.Toplevel(mainWindow)
    app = korea(window6)
    window6.mainloop()

def createNewWindow7():
    window7 = tk.Toplevel(mainWindow)
    app = world(window7)
    window7.mainloop()


mainWindow = Tk()
mainWindow.title("AutomationTool")

# 화면 비율
window_width = 300
window_height = 480  # 높이 조정
screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
mainWindow.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

label_frame = ttk.LabelFrame(mainWindow, text="프로그램")
label_frame.pack(padx=10, pady=10, fill="x", expand=True)

label_frame2 = ttk.LabelFrame(mainWindow, text="업데이트 내역서")
label_frame2.pack(padx=10, pady=10, fill="x", expand=True)

# 버튼
# -- label_frame
button1 = ttk.Button(label_frame, text="3세대 파일명 변경 프로그램", command=createNewWindow1)
button1.pack(padx=7, pady=7)
button2 = ttk.Button(label_frame, text="4세대 파일명 변경 프로그램", command=createNewWindow2)
button2.pack(padx=7, pady=7)
button3 = ttk.Button(label_frame, text="파일 버전 확인 프로그램", command=createNewWindow3)
button3.pack(padx=7, pady=7)
button4 = ttk.Button(label_frame, text="자동 분할 압축 프로그램", command=createNewWindow4)
button4.pack(padx=7, pady=7)
button5 = ttk.Button(label_frame, text="빈폴더 확인 프로그램", command=createNewWindow5)
button5.pack(padx=7, pady=7)
button8 = ttk.Button(label_frame, text="수동 취합 검증 프로그램", command=createNewWindow8)
button8.pack(padx=7, pady=7)
button9 = ttk.Button(label_frame, text="수동 취합용 자동 프로그램", command=createNewWindow9)
button9.pack(padx=7, pady=7)

# -- label_frame2
button6 = ttk.Button(label_frame2, text="국내", command=createNewWindow6)
button6.pack(padx=7, pady=7)
button7 = ttk.Button(label_frame2, text="해외", command=createNewWindow7)
button7.pack(padx=7, pady=7)

mainWindow.mainloop()