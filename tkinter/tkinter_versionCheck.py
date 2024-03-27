import os
from tkinter import *
import tkinter as tk
from tkinter import ttk

def GDSN():

    # file_path = input("♥♥♥ 파일경로를 입력하세요 : ")
    file_path = entry.get()

    # 변수 선언
    App = "\\Application"
    App_txt = "\\Application_Version.txt"
    Rsc = "\\Resource"
    Rsc_txt = "\\Resource_Version.txt"
    SupportApp = "\\SupportApp"
    SupportApp_txt = "\\SupportApp_Version.txt"
    System = "\\system"
    Sys_txt = "\\System_Version.txt"


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
                    label=Label(frame, text="Application = " + item).pack()


        # 파일 열기
        with open(file_path+App+App_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(frame, text="Version_txt = " + file_content).pack()

        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)  
        if item_list[0] != file_content:
            # print("!!!!!!!! FAIL !!!!!!!!")
            label=Label(frame, text="FAIL", fg="red").pack()
        else :
            # print("PASS")
            label=Label(frame, text="PASS", fg="blue").pack()

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
        


        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
        pass_list=[]

        for i in range(0,len(split_str_new_list)):
            if split_str_new_list[i] == file_content:
                pass_list.append("PASS")
        
        if len(pass_list) == len(split_str_new_list) :
            # print(pass_list)
            # print("PASS")
            label=Label(frame, text="PASS", fg="blue").pack()
        else :
            # print("!!!!!!!!! FAIL !!!!!!!!!")
            label=Label(frame, text="FAIL", fg="red").pack()


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

    else:
        pass


    # System--------------------------------------
    
    if "system" in os.listdir(file_path) or "System" in os.listdir(file_path):

        zip_files = []

        # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
        for root, dirs, files in os.walk(file_path+System):
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
        with open(file_path+System+Sys_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("Version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()

        pass_list=[]

        for i in range(0,len(split_str_new_list)):
            if split_str_new_list[i] == file_content:
                pass_list.append("PASS")
        
        if len(pass_list) == len(split_str_new_list) :
            # print(pass_list)
            # print("PASS")
            label=Label(frame, text="PASS", fg="blue").pack()
        else :
            # print("!!!!!!!!! FAIL !!!!!!!!!")
            label=Label(frame, text="FAIL", fg="red").pack()            

    else:
        pass
    
    return

def GDSM():

    file_path = entry.get()

    # 변수 선언
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
    System = "\\system"
    Sys_txt = "\\System_Version.txt"


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
                    label=Label(frame, text="Application = " + item).pack()

        # 파일 열기
        with open(file_path+App+App_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
            # print("Version_txt = " + file_content)
            label=Label(frame, text="Version_txt = " + file_content).pack()

        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)  
        if item_list[0] != file_content:
            # print("!!!!!!!! FAIL !!!!!!!!")
            label=Label(frame, text="FAIL", fg="red").pack()
        else :
            # print("PASS")
            label=Label(frame, text="PASS", fg="blue").pack()

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
        label=Label(frame, text="Critical = " + zip_files[0]).pack()
        
        # 파일 열기
        with open(file_path+Critical+Critical_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("Version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()

        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
        pass_list=[]

        for i in range(0,len(split_str_new_list)):
            if split_str_new_list[i] == file_content:
                pass_list.append("PASS")
        
        if "PASS" in pass_list :
            # print(pass_list)
            # print("PASS")
            label=Label(frame, text="PASS", fg="blue").pack()
        else :
            # print("!!!!!!!!! FAIL !!!!!!!!!")
            label=Label(frame, text="FAIL", fg="red").pack()

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


        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
        pass_list=[]

        for i in range(0,len(split_str_new_list)):
            if split_str_new_list[i] == file_content:
                pass_list.append("PASS")
        
        if "PASS" in pass_list :
            # print(pass_list)
            # print("PASS")
            label=Label(frame, text="PASS", fg="blue").pack()
        else :
            # print("!!!!!!!!! FAIL !!!!!!!!!")
            label=Label(frame, text="FAIL", fg="red").pack()


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

        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
        pass_list=[]

        for i in range(0,len(split_str_new_list)):
            if split_str_new_list[i] == file_content:
                pass_list.append("PASS")
        
        if "PASS" in pass_list :
            # print(pass_list)
            # print("PASS")
            label=Label(frame, text="PASS", fg="blue").pack()
        else :
            # print("!!!!!!!!! FAIL !!!!!!!!!")
            label=Label(frame, text="FAIL", fg="red").pack()


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
        label=Label(frame, text="ECU = " + zip_files[0]).pack()
        zip_split = str(zip_files[0]).split("-")
        split_str_new = str(zip_files[0]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
        split_str_new_list.append(split_str_new)
        
        
        # 파일 열기
        with open(file_path+ECU+ECU_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("Version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()

        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
        pass_list=[]

        for i in range(0,len(split_str_new_list)):
            if split_str_new_list[i] == file_content:
                pass_list.append("PASS")
        
        if "PASS" in pass_list :
            # print(pass_list)
            # print("PASS")
            label=Label(frame, text="PASS", fg="blue").pack()
        else :
            # print("!!!!!!!!! FAIL !!!!!!!!!")
            label=Label(frame, text="FAIL", fg="red").pack()

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
        label=Label(frame, text="ECU_CV = " + zip_files[0]).pack()
        zip_split = zip_files[0].split("-")
        split_str_new = str(zip_files[0]).replace("-"+zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
        split_str_new_list.append(split_str_new)
        

        # 파일 열기
        with open(file_path+ECU_CV+ECU_CV_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("Version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()

        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
        pass_list=[]

        for i in range(0,len(split_str_new_list)):
            if split_str_new_list[i] == file_content:
                pass_list.append("PASS")
        
        if "PASS" in pass_list :
            # print(pass_list)
            # print("PASS")
            label=Label(frame, text="PASS", fg="blue").pack()
        else :
            # print("!!!!!!!!! FAIL !!!!!!!!!")
            label=Label(frame, text="FAIL", fg="red").pack()

    else:
        pass

    # System--------------------------------------
    
    if "System" in os.listdir(file_path) or "system" in os.listdir(file_path):

        zip_files = []

        # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
        for root, dirs, files in os.walk(file_path+System):
            for file in files:
                if file.endswith('.zip'):
                    # 확장자가 .zip인 파일은 리스트에 추가
                    zip_files.append(os.path.join(file))

        split_str_new_list = []
        # ZIP 파일 목록 출력
        # print("System = " + zip_files[0])
        label=Label(frame, text="System = " + zip_files[0]).pack()
        zip_split = zip_files[0].split("-")
        split_str_new = str(zip_files[0]).replace("-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1],'')
        split_str_new_list.append(split_str_new)

        # 파일 열기
        with open(file_path+System+Sys_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("Version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()

        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
        pass_list=[]

        for i in range(0,len(split_str_new_list)):
            if split_str_new_list[i] == file_content:
                pass_list.append("PASS")
        
        if "PASS" in pass_list :
            # print(pass_list)
            # print("PASS")
            label=Label(frame, text="PASS", fg="blue").pack()
        else :
            # print("!!!!!!!!! FAIL !!!!!!!!!")
            label=Label(frame, text="FAIL", fg="red").pack()

    else:
        pass
    
    return

def Gscan():

    file_path = entry.get()

    # 변수 선언
    App = "\\application"
    App_txt = "\\application_version.txt"
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


    # application-----------------------------------

    if "application" in os.listdir(file_path):

        # 폴더명 추출
        for item in os.listdir(file_path+App):
            sub_folder = os.path.join(file_path+App, item) # 폴더경로 + 폴더명
            if os.path.isdir(sub_folder):
                # print("application = " + item)
                label=Label(frame, text="Application = " + item).pack()

        # 파일 열기
        with open(file_path+App+App_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
            # print("application_version_txt = " + file_content)
            label=Label(frame, text="Version_txt = " + file_content).pack()

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
        label=Label(frame, text="critical = " + zip_files[0]).pack()
        
        # 파일 열기
        with open(file_path+critical+critical_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("Version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()

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
        label=Label(frame, text="diagnosis = " + zip_files[0]).pack()
        
        # 파일 열기
        with open(file_path+diagnosis+diagnosis_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("diagnosis_version_txt = " + file_content)
        label=Label(frame, text="diagnosis_version_txt = " + file_content).pack()

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
        label=Label(frame, text="diagnosis_cv = " + zip_files[0]).pack()
        
        # 파일 열기
        with open(file_path+diagnosis_cv+diagnosis_cv_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        print("Version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()

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
        label=Label(frame, text="diagnosis_im = " + zip_files[0]).pack()
        
        # 파일 열기
        with open(file_path+diagnosis_im+diagnosis_im_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("Version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()

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
        label=Label(frame, text="os = " + zip_files[0]).pack()
        
        # 파일 열기
        with open(file_path+gscan_os+gscan_os_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("os_version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()
        
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
        label=Label(frame, text="system = " + zip_files[0]).pack()

        # 파일 열기
        with open(file_path+system+sys_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        # print("system_version_txt = " + file_content)
        label=Label(frame, text="Version_txt = " + file_content).pack()

    else:
        pass

    return

def clear_frame():
   for widgets in frame.winfo_children():
      widgets.destroy()

# 메인 함수
def main_function():
    if selected_project.get() == '1':
        GDSM()
    elif selected_project.get() == '2':
        GDSN()
    elif selected_project.get() == '3':
        Gscan()

# 화면 가운데 위치
window = Tk()
window.title("파일 버전 확인 프로그램")
# window.geometry("400x700")
window_width = 400
window_height = 600  # 높이 조정
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


# tkinter

label_title=tk.Label(window, text="*** 파일 버전 확인 Tool 입니다 ***", fg="blue", relief="groove")
label_title.pack(fill='x', padx=5, pady=5)

# 텍스트
label1=tk.Label(window, text="프로젝트를 선택하세요")
label1.pack(padx=5, pady=5)

# 항목값
selected_project = tk.StringVar()
projects = (('3세대', '1'),
         ('4세대', '2'),
         ('Gscan', '3'))

# radio buttons
for project in projects:
    r = ttk.Radiobutton(
        window,
        text=project[0],
        value=project[1],
        variable=selected_project
    )
    r.pack(padx=5, pady=5)


# 텍스트
label2=tk.Label(window, text="파일 경로를 입력하세요")
label2.pack(fill='x', padx=5, pady=5)

# 입력창
entry=ttk.Entry(window, width=50, justify="center")
entry.pack(fill='x', padx=5, pady=5)

# 버튼

btn_versionCheck = ttk.Button(window, text = "버전 확인...", command = main_function)
btn_versionCheck.pack(padx=5, pady=5)


label3=tk.Label(window, text="내용을 삭제하려면 버튼을 클릭하세요")
label3.pack(fill='x', padx=5, pady=5)

btn_cls = ttk.Button(window, text = "초기화...", command=clear_frame)
btn_cls.pack(padx=5, pady=5)

# 프레임
frame = LabelFrame(window, text="확인")
frame.pack(padx=10, pady=10, fill="x", expand=True)


window.mainloop()