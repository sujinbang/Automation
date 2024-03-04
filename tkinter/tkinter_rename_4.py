import os
from tkinter import *
import tkinter
from tkinter import messagebox
# from tkinter_versionCheck import main_function

# 변수 선언
App = "\Application"
App_txt = "\Application_Version.txt"
Rsc = "\Resource"
Rsc_txt = "\Resource_Version.txt"
SupportApp = "\SupportApp"
SupportApp_txt = "\SupportApp_Version.txt"
Sys = "\system"
Sys_txt = "\System_Version.txt"

# 폴더명 변경

### Rename
# Application
def rename_app():
    # file_path
    file_path = entry_filePath.get()
    # new_name
    new_name = entry_newName.get()

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
def rename_rsc():
    # file_path
    file_path = entry_filePath.get()
    # new_name
    new_name = entry_newName.get()

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
def rename_supportApp():
    # file_path
    file_path = entry_filePath.get()
    # new_name
    new_name = entry_newName.get()

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
def rename_sys():
    # file_path
    file_path = entry_filePath.get()
    # new_name
    new_name = entry_newName.get()

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
def Check_app():

    file_path = entry_filePath.get()

    item_list = []

    # 폴더명 추출
    for item in os.listdir(file_path+App):
        sub_folder = os.path.join(file_path+App, item) # 폴더경로 + 폴더명
        if os.path.isdir(sub_folder):
            if '.txt' not in item:
                item_list.append(item)
                # print("Application = " + item)
                label=Label(frame, text="Application = " + item).pack()


    # 파일 열기
    with open(file_path+App+App_txt, "r", encoding="utf-8") as file:
        file_content = file.read()
        # print("Version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()

    return

def Check_rsc():

    file_path = entry_filePath.get()

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
            label=Label(frame, text="Resource = " + zip_files[i]).pack()
            zip_split = zip_files[i].split("-")
            split_str_new = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]
            split_str_new_list.append(split_str_new)

    elif len(zip_files) == 1:
        # print("Resource = " + zip_files[0])
        label=Label(frame, text="Resource = " + zip_files[0]).pack()
        zip_split = zip_files[0].split("-")
        split_str_new = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]
        split_str_new_list.append(split_str_new)
    
    # 파일 열기
    with open(file_path+Rsc+Rsc_txt, "r", encoding="utf-8") as file:
        file_content = file.read()
    # print("Version_txt = " + file_content)
    label=Label(frame, text="Version_txt = " + file_content).pack()

    return

def Check_SupportApp():

    file_path = entry_filePath.get()
    item_list = []

    # 폴더명 추출
    for item in os.listdir(file_path+SupportApp):
        sub_folder = os.path.join(file_path+SupportApp, item) # 폴더경로 + 폴더명
        if os.path.isdir(sub_folder):
            if '.txt' not in item:
                item_list.append(item)
                # print("SupportApp = " + item)
                label=Label(frame, text="SupportApp = " + item).pack()

    # 파일 열기
    with open(file_path+SupportApp+SupportApp_txt, "r", encoding="utf-8") as file:
        file_content = file.read()
    # print("Version_txt = " + file_content)
    label=Label(frame, text="Version_txt = " + file_content).pack()

    # 폴더명과 버전 txt가 같은지 (PASS/FAIL)          
    if item_list[0] != file_content:
        # print("!!!!!!!! FAIL !!!!!!!!")
        label=Label(frame, text="FAIL", fg="red").pack()
        # print(item_list[0], file_content)
        label=Label(frame, text=(item_list[0], file_content), fg="red").pack()
    else :
        # print("PASS") 
        label=Label(frame, text="PASS", fg="blue").pack()
    
    return

def Check_sys():

    file_path = entry_filePath.get()
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
    label=Label(frame, text="System = " + zip_files[0]).pack()
    zip_split = zip_files[0].split("-")
    split_str_new = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]
    split_str_new_list.append(split_str_new)

    # 파일 열기
    with open(file_path+Sys+Sys_txt, "r", encoding="utf-8") as file:
        file_content = file.read()
    # print("Version_txt = " + file_content)
    label=Label(frame, text="Version_txt = " + file_content).pack()

    return 


# tkinter

# 프레임 내용 삭제
def clear_frame():
   for widgets in frame.winfo_children():
      widgets.destroy()

window = Tk()

# 메뉴
menubar=tkinter.Menu(window)
menu=tkinter.Menu(menubar, tearoff=0)
menu.add_command(label="VersionCheck")
menu.add_command(label="Rename_4세대")
menubar.add_cascade(label="메뉴", menu=menu)
window.config(menu=menubar)


window.title("AutomationTool")
window.geometry("500x800")

# 메인 함수
def Rename():
    if selected_item.get() == '1':
        rename_app()
    elif selected_item.get() == '2':
        rename_rsc()
    elif selected_item.get() == '3':
        rename_supportApp()
    elif selected_item.get() == '4':
        rename_sys()

    info()   # 메세지 박스 open

# 메시지 박스
def info():
    messagebox.showinfo("알림", "파일명이 변경되었습니다")

def VersionCheck():
    if selected_item.get() == '1':
        Check_app()
    elif selected_item.get() == '2':
        Check_rsc()
    elif selected_item.get() == '3':
        Check_SupportApp()
    elif selected_item.get() == '4':
        Check_sys()    

# 파일 경로 입력
label_title=tkinter.Label(window, text="*** 4세대 파일명 변경 Tool 입니다 ***", fg="blue", relief="groove")
label_title.pack(fill='x', padx=5, pady=5)

# 파일 경로 입력
label1=tkinter.Label(window, text="[Step 1] 파일 경로를 입력하세요")
label1.pack(fill='x', padx=5, pady=5)

entry_filePath=tkinter.Entry(window, width=50, justify="center")
entry_filePath.pack(fill='x', padx=5, pady=5)

# 텍스트
label2=tkinter.Label(window, text="[Step 2] 항목을 선택하세요")
label2.pack()

# 항목값
selected_item = tkinter.StringVar()
items = (('Application', '1'),
        ('Resource', '2'),
        ('SupportApp', '3'),
        ('System', '4'))        

# radio buttons
for item in items:
    r = Radiobutton(
        window,
        text=item[0],
        value=item[1],
        variable=selected_item
    )
    r.pack(padx=5, pady=5)

# new file명 입력
label3=tkinter.Label(window, text="[Step 3] 바꿀 파일명을 입력하세요")
label3.pack(fill='x', padx=5, pady=5)

entry_newName=tkinter.Entry(window, width=50, justify="center")
entry_newName.pack(fill='x', padx=5, pady=5)

# 버튼
btn_Rename = Button(window, text = "Rename", command = Rename)
btn_Rename.pack(fill='x', padx=5, pady=5)

# new file명 입력
label3=tkinter.Label(window, text="[Step 4] 버전을 확인하세요")
label3.pack(fill='x', padx=5, pady=5)

btn_versionCheck = Button(window, text = "VersionCheck", command = VersionCheck)
btn_versionCheck.pack(fill='x', padx=5, pady=5)

# 프레임
frame = LabelFrame(window, text="Output", relief="solid", bd=2, pady=10)
frame.pack(fill='both')

btn_cls = Button(window, text="Clear", command = clear_frame)
btn_cls.pack(padx=5, pady=5)





window.mainloop()