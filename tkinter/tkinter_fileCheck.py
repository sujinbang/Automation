# -- 파일 체크 프로그램 입니다
import os
import shutil
import zipfile
from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk

# file_path = entry.get()
file_path = input("파일 경로를 입력하세요 : ")

# 변수 선언
App = "\\Application"
App_txt = "\\Application_Version.txt"
Rsc = "\\Resource"
Rsc_txt = "\\Resource_Version.txt"
SupportApp = "\\SupportApp"
SupportApp_txt = "\\SupportApp_Version.txt"
System = "\\system"
Sys_txt = "\\System_Version.txt"

if "Application" in os.listdir(file_path):

    item_list = []

    # 폴더명 추출
    for item in os.listdir(file_path+App):
        sub_folder = os.path.join(file_path+App, item) # 폴더경로 + 폴더명
        if os.path.isdir(sub_folder):
            print(item)
            if '.txt' not in item:
                item_list.append(item)
                print("Application = " + item)
                # label=Label(frame, text="Application = " + item).pack()

    # 파일 열기
        with open(file_path+App+App_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
            print("Version_txt = " + file_content)
            # label=Label(frame, text="Version_txt = " + file_content).pack()

else:
    pass

# if "Resource" in os.listdir(file_path):

#     file_name = file_path + Rsc
#     for (root, dirs, files) in os.walk(file_name):
#         # print(root)
#         if len(dirs) != 0:
#             print("FAIL")
#         # print("Rsc = ", dirs)
#         print("Rsc = ", files)
# else:
#     pass

# if "SupportApp" in os.listdir(file_path):

#     file_name = file_path + SupportApp
#     for (root, dirs, files) in os.walk(file_name):
#         # print(root)
#         print("SupportApp = ", dirs)
#         print("SupportApp = ", files)
# else:
#     pass

# if "System" in os.listdir(file_path) or "system" in os.listdir(file_path):

#     file_name = file_path + System
#     for (root, dirs, files) in os.walk(file_name):
#         # print(root)
#         if len(dirs) != 0:
#             print("FAIL")
#         # print("System = ", dirs)
#         print("System = ", files)
# else:
#     pass
