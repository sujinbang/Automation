import os
import shutil
import zipfile
from tkinter import *
import tkinter
from tkinter import messagebox

# 변수 선언
Resource = "\Resource"
Diagnosis = "\Diagnosis"
Rsc = Resource  # 기본값으로 Resource 폴더 설정

# 폴더명 추출
zip_files = []
empty_folders = []

def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()

def update_rsc_folder():
    global Rsc
    if selected_item.get() == '1':
        Rsc = Diagnosis
    elif selected_item.get() == '2':
        Rsc = Resource

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
    empty_folders.clear()  # 리스트 초기화
    file_path = entry_filePath.get()
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

        # 빈 파일 확인
        for (root, dirs, files) in os.walk(file_name):
            if not dirs:
                if not files:
                    empty_folders.append(root)

    if len(empty_folders) == 0:
        label = Label(frame, text="빈 파일이 없습니다", fg="blue")
        label.pack()
    else:
        for i in range(0, len(empty_folders)):
            label = Label(frame, text=empty_folders[i] + " 파일을 확인하세요", fg="red", wraplength=400)
            label.pack()

def delete_extracted_files():
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
    rsc_fileList()  # 리소스 파일 리스트
    fileCheck()  # 파일 확인

window = Tk()
window.title("FileCheck")
window.geometry("500x800")

label1 = tkinter.Label(window, text="프로젝트를 선택하세요")
label1.pack(fill='x', padx=5, pady=5)

# 항목값
selected_item = tkinter.StringVar(value='2')  # 기본값으로 4세대 선택
items = (('3세대', '1'),
         ('4세대', '2'))

# 프로젝트 선택 라디오 버튼
for item in items:
    r = Radiobutton(
        window,
        text=item[0],
        value=item[1],
        variable=selected_item,
        command=update_rsc_folder
    )
    r.pack(padx=5, pady=5)

label2 = tkinter.Label(window, text="파일 경로를 입력하세요")
label2.pack(fill='x', padx=5, pady=5)

entry_filePath = tkinter.Entry(window, width=50, justify="center")
entry_filePath.pack(fill='x', padx=5, pady=5)

btn_Check = Button(window, text="압축 해제 및 빈 파일 확인", command=main_function)
btn_Check.pack(fill='x', padx=5, pady=5)

btn_delete = Button(window, text="압축 해제한 파일 삭제", command=delete_extracted_files)
btn_delete.pack(fill='x', padx=5, pady=5)

# 프레임
frame = LabelFrame(window, text="Output", relief="solid", bd=2, pady=10)
frame.pack(fill='both')

btn_cls = Button(window, text="Clear", command=clear_frame)
btn_cls.pack(padx=5, pady=5)

window.mainloop()