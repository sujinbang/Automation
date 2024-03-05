import os
from tkinter import *
import tkinter
from tkinter import messagebox
# from tkinter_versionCheck import main_function

# 변수 선언
App = "\Application"
App_txt = "\Application_Version.txt"
Critical = "\Critical"
Critical_txt = "\Critical_Version.txt"
Diagnosis = "\Diagnosis"
Diagnosis_txt = "\Diagnosis_Version.txt"
Diagnosis_CV = "\Diagnosis_CV"
Diagnosis_CV_txt = "\Diagnosis_CV_Version.txt"
ECU = "\ECU"
ECU_txt = "\ECU_Version.txt"
ECU_CV = "\ECU_CV"
ECU_CV_txt = "\ECU_CV_Version.txt"
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

# Critical
def rename_critical():
    # file_path
    file_path = entry_filePath.get()
    # new_name
    new_name = entry_newName.get()

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
def rename_diag():
    # file_path
    file_path = entry_filePath.get()
    # new_name
    new_name = entry_newName.get()
    
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
def rename_diag_CV():

    # file_path
    file_path = entry_filePath.get()
    # new_name
    new_name = entry_newName.get()

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
def rename_ECU():

    # file_path
    file_path = entry_filePath.get()
    # new_name
    new_name = entry_newName.get()

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
def rename_ECU_CV():

    # file_path
    file_path = entry_filePath.get()
    # new_name
    new_name = entry_newName.get()

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
    split_str_new = zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1]  # new_name

    old_name = file_path + Sys + "\\" + zip_files[0]
    new_name = file_path + Sys + "\\" + new_name + "-" + split_str_new

    os.rename(old_name, new_name)


### Check
# Application
def Check_app():

    file_path = entry_filePath.get()

    if "Application" in os.listdir(file_path):

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
    
    else:
        label=Label(frame, text="파일이 존재하지 않습니다.", fg='red').pack()

    return

def Check_Crit():

    file_path = entry_filePath.get()

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
        label=Label(frame, text="Critical = " + zip_files[0]).pack()
        
        # 파일 열기
        with open(file_path+Critical+Critical_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        print("Version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()
    
    else:
        label=Label(frame, text="파일이 존재하지 않습니다.", fg='red').pack()

    return

def Check_Diag():

    file_path = entry_filePath.get()

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
                label=Label(frame, text="Diagnosis = " + zip_files[i]).pack()
                zip_split = zip_files[i].split("-")
                split_str_new = str(zip_files[i]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                split_str_new_list.append(split_str_new)

        elif len(zip_files) == 1:
            # print("Diagnosis = " + zip_files[0])
            label=Label(frame, text="Diagnosis = " + zip_files[0]).pack()
            zip_split = zip_files[0].split("-")
            split_str_new = str(zip_files[0]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
            split_str_new_list.append(split_str_new)
        
        
        # 파일 열기
        with open(file_path+Diagnosis+Diagnosis_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("Version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()
    
    else:
        label=Label(frame, text="파일이 존재하지 않습니다.", fg='red').pack()

    return

def Check_Diag_CV():

    file_path = entry_filePath.get()

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
                label=Label(frame, text="Diagnosis_CV = " + zip_files[i]).pack()
                zip_split = zip_files[i].split("-")
                split_str_new = str(zip_files[i]).replace("-"+zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
                split_str_new_list.append(split_str_new)

        elif len(zip_files) == 1:
            # print("Diagnosis_CV = " + zip_files[0])
            label=Label(frame, text="Diagnosis_CV = " + zip_files[0]).pack()
            zip_split = zip_files[0].split("-")
            split_str_new = str(zip_files[0]).replace("-"+zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
            split_str_new_list.append(split_str_new)
        
        # 파일 열기
        with open(file_path+Diagnosis_CV+Diagnosis_CV_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("Version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()
    
    else :
        label=Label(frame, text="파일이 존재하지 않습니다.", fg='red').pack()

    return

def Check_ECU():

    file_path = entry_filePath.get()

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
        label=Label(frame, text="ECU = " + zip_files[0]).pack()
        
        # 파일 열기
        with open(file_path+ECU+ECU_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("Version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()
    
    else :
        label=Label(frame, text="파일이 존재하지 않습니다.", fg='red').pack()

    return

def Check_ECU_CV():

    file_path = entry_filePath.get()
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
        label=Label(frame, text="ECU_CV = " + zip_files[0]).pack()

        
        # 파일 열기
        with open(file_path+ECU_CV+ECU_CV_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("Version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()

    else:
        label=Label(frame, text="파일이 존재하지 않습니다.", fg='red').pack()

    return

def Check_sys():

    file_path = entry_filePath.get()

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
        label=Label(frame, text="System = " + zip_files[0]).pack()
        zip_split = zip_files[0].split("-")
        split_str_new = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]
        split_str_new_list.append(split_str_new)

        # 파일 열기
        with open(file_path+Sys+Sys_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("Version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()
    
    else :
        label=Label(frame, text="파일이 존재하지 않습니다.", fg='red').pack()

    return 


# tkinter

# 프레임 내용 삭제
def clear_frame():
   for widgets in frame.winfo_children():
      widgets.destroy()

window = Tk()

window.title("AutomationTool")
window.geometry("500x800")

# 메인 함수
def Rename():
    if selected_item.get() == '1':
        rename_app()
    elif selected_item.get() == '2':
        rename_critical()
    elif selected_item.get() == '3':
        rename_diag()
    elif selected_item.get() == '4':
        rename_diag_CV()
    elif selected_item.get() == '5':
        rename_ECU()
    elif selected_item.get() == '6':
        rename_ECU_CV()
    elif selected_item.get() == '7':
        rename_sys()

    info()   # 메세지 박스 open

# 메시지 박스
def info():
    messagebox.showinfo("알림", "파일명이 변경되었습니다")

def VersionCheck():
    if selected_item.get() == '1':
        Check_app()
    elif selected_item.get() == '2':
        Check_Crit()
    elif selected_item.get() == '3':
        Check_Diag()
    elif selected_item.get() == '4':
        Check_Diag_CV()
    elif selected_item.get() == '5':
        Check_ECU()
    elif selected_item.get() == '6':
        Check_ECU_CV()
    elif selected_item.get() == '7':
        Check_sys()   

# 파일 경로 입력
label_title=tkinter.Label(window, text="*** 3세대 파일명 변경 Tool 입니다 ***", fg="green", relief="groove")
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
        ('Critical', '2'),
        ('Diagnosis', '3'),
        ('Diagnosis_CV', '4'),
        ('ECU', '5'),
        ('ECU_CV', '6'),
        ('System', '7'))        

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