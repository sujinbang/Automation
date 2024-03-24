import os
import shutil
import zipfile
from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk

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



# 화면 가운데 위치
window = Tk()
window.title("빈 파일 확인 프로그램")
# window.geometry("400x700")
window_width = 400
window_height = 600  # 높이 조정
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# 파일 경로 입력
label_frame1 = ttk.LabelFrame(window, text="설정")
label_frame1.pack(padx=10, pady=10, fill="x", expand=True)

# label_title=tk.Label(window, text="*** 빈 파일 확인 Tool 입니다 ***", fg="blue", relief="groove")
# label_title.pack(fill='x', padx=5, pady=5)

label1 = Label(label_frame1, text="프로젝트를 선택하세요")
label1.pack(anchor='w')

# 항목값
selected_item = tk.StringVar(value='2')  # 기본값으로 4세대 선택
items = (('3세대', '1'),
         ('4세대', '2'))

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

btn_Check = ttk.Button(label_frame1, text="Resource 빈 파일 확인", command=main_function)
btn_Check.pack(padx=5, pady=5)

# btn_delete = ttk.Button(label_frame1, text="압축 해제한 파일 삭제", command=delete_extracted_files)
# btn_delete.pack(fill='x', padx=5, pady=5)

# 프레임
frame = ttk.LabelFrame(label_frame1, text="Output")
frame.pack(fill="x")

label3 = Label(frame, text="")
label3.pack()

btn_cls = ttk.Button(label_frame1, text="Clear", command=clear_frame)
btn_cls.pack(padx=5, pady=5)

window.mainloop()