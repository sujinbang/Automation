import os
from tkinter import *
import tkinter

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



# tkinter
# 프레임 내용 삭제
def clear_frame1():
   for widgets in frame1.winfo_children():
      widgets.destroy()

# def clear_frame2():
#    for widgets in frame2.winfo_children():
#       widgets.destroy()

window = Tk()

window.title("AutomationTool")
window.geometry("500x800")

# 메인 함수
def main_function():
    if openItem.selected_item.get() == '1':
        rename_app()
    elif openItem.selected_item.get() == '2':
        rename_rsc()
    elif openItem.selected_item.get() == '3':
        rename_supportApp()
    elif openItem.selected_item.get() == '4':
        rename_sys()    

# 파일 경로 입력
label1=tkinter.Label(window, text="파일 경로를 입력하세요")
label1.pack(fill='x', padx=5, pady=5)

entry_filePath=tkinter.Entry(window, width=50)
entry_filePath.pack(fill='x', padx=5, pady=5)

# 프로젝트 입력
selected_project = tkinter.StringVar()
projects = (('3세대', '1'),
         ('4세대', '2'))

# radio buttons
for project in projects:
    r = Radiobutton(
        window,
        text=project[0],
        value=project[1],
        variable=selected_project
    )
    r.pack(fill='x', padx=5, pady=5)


def openItem():

    # 항목값
    if selected_project.get() == '1':
        selected_item = tkinter.StringVar()
        items = (('Application', '1'),
                ('Critical', '2'),
                ('Diagnosis', '3'),
                ('Diagnosis_CV', '4'),
                ('ECU', '5'),
                ('ECU_CV', '6'),
                ('System', '7'))

    elif selected_project.get() == '2':
        selected_item = tkinter.StringVar()
        items = (('Application', '1'),
                ('Resource', '2'),
                ('SupportApp', '3'),
                ('System', '4'))        

    # radio buttons
    for item in items:
        r = Radiobutton(
            frame1,
            text=item[0],
            value=item[1],
            variable=selected_item
        )
        r.pack()
    
    return


button = Button(window,
                text = "Get Selected",
                command=openItem)
button.pack(fill='x', padx=5, pady=5)

# 텍스트
label2=tkinter.Label(window, text="항목을 선택하세요")
label2.pack()

# 프레임
frame1 = LabelFrame(window, text="Item", relief="solid", bd=2, pady=10)
frame1.pack(side="left", expand=True)

btn_cls1 = Button(window, text = "Clear", command=clear_frame1)
btn_cls1.pack(fill='x', padx=5, pady=5)

# # new file명 입력
# label3=tkinter.Label(window, text="바꿀 파일명을 입력하세요")
# label3.pack(fill='x', padx=5, pady=5)

# entry_newName=tkinter.Entry(window, width=50)
# entry_newName.pack(fill='x', padx=5, pady=5)

# # 버튼
# btn_versionCheck = Button(window, text = "Rename", command = main_function)
# btn_versionCheck.pack(fill='x', padx=5, pady=5)

# label4=tkinter.Label(window, text="내용을 삭제하려면 버튼을 클릭하세요")
# label4.pack(fill='x', padx=5, pady=5)

# btn_cls2 = Button(window, text = "Clear", command=clear_frame2)
# btn_cls2.pack(fill='x', padx=5, pady=5)

# # 프레임
# frame2 = LabelFrame(window, text="Output", relief="solid", bd=2, pady=10)
# frame2.pack(side="left", expand=True)

# 메시지 박스
# from tkinter import messagebox
# messagebox.showinfo()


window.mainloop()