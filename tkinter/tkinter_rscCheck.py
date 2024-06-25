# -- 리소스 파일 체크 프로그램 입니다
# -- 중단!
import os
import shutil
import zipfile
from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk

# 변수 선언
fileroot = "\\systemdb\\system"
Rsc = "\\Resource"
Sys = "\\system"

# Rsc
# 폴더명 추출
zip_files = []
fileFail = []
empty_folders = []

def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()

def update_rsc_folder():
    global Rsc
    if selected_item.get() == '1':
        Rsc = Rsc
    elif selected_item.get() == '2':
        Rsc = Sys

def rsc_fileList():
    zip_files.clear()  # 리스트 초기화
    file_path = entry_filePath.get()
    # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
    for root, dirs, files in os.walk(file_path + Rsc):
        for file in files:
            if file.endswith('.zip'):
                # 확장자가 .zip인 파일은 리스트에 추가
                zip_files.append(os.path.join(file))
    return

def fileCheck():
    fileFail.clear()
    file_path = entry_filePath.get()
    # Resource
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

        # 파일 확인
        fix_file = ['ECU_mapping.sqlite', 'SoftwareInformation.sqlite', 'SpecialFunction.sqlite', 'GDSN_AUXmultilanguage.sqlite', 'GDSNmultilanguage.sqlite', 'GDSMultilanguage_CV.Sqlite']
        fileList = []
        for (root, dirs, files) in os.walk(file_name+fileroot):
            if not dirs:
                if not files:
                    empty_folders.append(root)
            fileList.append(files)

        # Resource
        if selected_item.get() == '1':
            for i in range(0, len(fileList[0])):
                # label = Label(frame, text=file[0][i], fg="blue").pack()
                if fileList[0][i] in fix_file :
                    fileFail.append(fileList[0][i])
            if len(fileFail) != 0:
                for j in range(0, len(fileFail)):
                    label = Label(frame, text= fileFail[j] + " 파일 확인!!!!!!" + '\n', fg="red").pack()
            elif len(fileFail) == 0:
                label = Label(frame, text='PASS', fg="blue").pack()

        # System
        elif selected_item.get() == '2':
            for i in range(0, len(fileList[0])):
                # label = Label(frame, text=fileList[0][i], fg="blue").pack()
                if fileList[0][i] not in fix_file :
                    fileFail.append(fileList[0][i])
            if len(fileFail) != 0:
                for j in range(0, len(fileFail)):
                    label = Label(frame, text=fileFail[j] + " 파일 확인!!!!!!" + '\n', fg="red").pack()
            elif len(fileFail) == 0:
                label = Label(frame, text='PASS', fg="blue").pack()

        
    file_path = entry_filePath.get()
    response = messagebox.askyesno("확인", "압축 해제한 파일을 삭제하시겠습니까?")
    if response == 1:  # 사용자가 '확인'을 클릭한 경우
        for i in range(0, len(zip_files)):
            zip_file_rep = zip_files[i].replace('.zip', '')
            shutil.rmtree(file_path + Rsc + "\\" + zip_file_rep)
        messagebox.showinfo("알림", "압축 해제한 파일이 성공적으로 삭제되었습니다.")
    else:
        messagebox.showinfo("알림", "파일 삭제가 취소되었습니다.")



def main_function():
    update_rsc_folder()
    rsc_fileList()  # 리소스 파일 리스트
    fileCheck()  # 파일 확인


# 화면 가운데 위치
window = Tk()
window.title("4세대 리소스 정합성 확인 프로그램")
# window.geometry("400x700")
window_width = 400
window_height = 400  # 높이 조정
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# 파일 경로 입력
label_title=tk.Label(window, text="*** 4세대 리소스 정합성 확인 프로그램 ***", fg="blue", relief="groove")
label_title.pack(fill='x', padx=5, pady=5)

label_frame1 = ttk.LabelFrame(window, text="설정")
label_frame1.pack(padx=10, pady=10, fill="x", expand=True)

label1 = Label(label_frame1, text="프로젝트를 선택하세요")
label1.pack(anchor='w')

# 항목값
selected_item = tk.StringVar(value='1')
items = (('Resource', '1'),
         ('System', '2'))

# 프로젝트 선택 라디오 버튼
for item in items:
    r = ttk.Radiobutton(
        label_frame1,
        text=item[0],
        value=item[1],
        variable=selected_item,
        command=update_rsc_folder
    )
    r.pack(padx=5, pady=5)

label2 = Label(label_frame1, text="파일 경로:")
label2.pack(anchor='w')

entry_filePath = ttk.Entry(label_frame1, width=50, justify="center")
entry_filePath.pack(padx=5, pady=5)

btn_Check = ttk.Button(label_frame1, text="파일 확인", command=main_function)
btn_Check.pack(padx=5, pady=5)

# btn_delete = ttk.Button(label_frame1, text="압축 해제한 파일 삭제", command=delete_extracted_files)
# btn_delete.pack(fill='x', padx=5, pady=5)

# 프레임
frame = ttk.LabelFrame(label_frame1, text="Output")
frame.pack(fill="x")

label3 = Label(frame, text="")
label3.pack()

btn_cls = ttk.Button(label_frame1, text="초기화", command=clear_frame)
btn_cls.pack(padx=5, pady=5)

window.mainloop()

