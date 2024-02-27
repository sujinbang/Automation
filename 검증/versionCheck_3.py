import os
def GDSM():

    file_path = input("♥♥♥ 파일경로를 입력하세요 : ")

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
    System = "\system"
    Sys_txt = "\System_Version.txt"


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
                    print("Application = " + item)
                    # label=Label(frame, text="Application = " + item).pack()

        # 파일 열기
        with open(file_path+App+App_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
            print("Version_txt = " + file_content)
            # label=Label(frame, text="Version_txt = " + file_content).pack()

        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)  
        if item_list[0] != file_content:
            print("!!!!!!!! FAIL !!!!!!!!")
            # label=Label(frame, text="FAIL", fg="red").pack()
        else :
            print("PASS")
            # label=Label(frame, text="PASS", fg="blue").pack()

        print("======================================")

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
        print("Critical = " + zip_files[0])
        zip_split = str(zip_files[0]).split("-")
        split_str_new = str(zip_files[0]).strip(zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1])
        split_str_new_list.append(split_str_new)
        # label=Label(frame, text="Critical = " + zip_files[0]).pack()
        
        # 파일 열기
        with open(file_path+Critical+Critical_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        print("Version_txt = " + file_content)
        # label=Label(frame, text="Version_txt = " + file_content).pack()

        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
        pass_list=[]

        for i in range(0,len(split_str_new_list)):
            if split_str_new_list[i] == file_content:
                pass_list.append("PASS")
        
        if "PASS" in pass_list :
            # print(pass_list)
            print(split_str_new)
            print("PASS")
        else :
            print(split_str_new)
            print("!!!!!!!!! FAIL !!!!!!!!!")

        print("======================================")

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
                print("Diagnosis = " + zip_files[i])
                # label=Label(frame, text="Diagnosis = " + zip_files[0]).pack()
                zip_split = zip_files[i].split("-")
                split_str_new = str(zip_files[i]).strip(zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1])
                print(zip_files[i])
                print(zip_split[-3])
                print(zip_split[-2])
                print(zip_split[-1])
                print(split_str_new)
                split_str_new_list.append(split_str_new)

        elif len(zip_files) == 1:
            print("Diagnosis = " + zip_files[0])
            zip_split = zip_files[0].split("-")
            split_str_new = str(zip_files[0]).strip(zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1])
            split_str_new_list.append(split_str_new)
        
        
        # 파일 열기
        with open(file_path+Diagnosis+Diagnosis_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        print("Version_txt = " + file_content)
        # label=Label(frame, text="Version_txt = " + file_content).pack()


        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
        pass_list=[]

        for i in range(0,len(split_str_new_list)):
            if split_str_new_list[i] == file_content:
                pass_list.append("PASS")
        
        if "PASS" in pass_list :
            # print(pass_list)
            print(split_str_new)
            print("PASS")
        else :
            print(split_str_new)
            print("!!!!!!!!! FAIL !!!!!!!!!")

        print("======================================")

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
                print("Diagnosis_CV = " + zip_files[i])
                # label=Label(frame, text="Diagnosis_CV = " + zip_files[i]).pack()
                zip_split = zip_files[i].split("-")
                split_str_new = str(zip_files[i]).strip(zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1])
                split_str_new_list.append(split_str_new)

        elif len(zip_files) == 1:
            print("Diagnosis_CV = " + zip_files[0])
            # label=Label(frame, text="Diagnosis_CV = " + zip_files[0]).pack()
            zip_split = zip_files[0].split("-")
            split_str_new = str(zip_files[0]).strip(zip_split[-4]+"-"+zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1])
            split_str_new_list.append(split_str_new)
        
        # 파일 열기
        with open(file_path+Diagnosis_CV+Diagnosis_CV_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        print("Version_txt = " + file_content)
        # label=Label(frame, text="Version_txt = " + file_content).pack()

        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
        pass_list=[]

        for i in range(0,len(split_str_new_list)):
            if split_str_new_list[i] == file_content:
                pass_list.append("PASS")
        
        if "PASS" in pass_list :
            # print(pass_list)
            print(split_str_new)
            print("PASS")
        else :
            print(split_str_new)
            print("!!!!!!!!! FAIL !!!!!!!!!")

        print("======================================")

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
        print("ECU = " + zip_files[0])
        zip_split = str(zip_files[0]).split("-")
        split_str_new = str(zip_files[0]).strip(zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1])
        split_str_new_list.append(split_str_new)
        # label=Label(frame, text="ECU = " + zip_files[0]).pack()
        
        # 파일 열기
        with open(file_path+ECU+ECU_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        print("Version_txt = " + file_content)
        # label=Label(frame, text="Version_txt = " + file_content).pack()

        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
        pass_list=[]

        for i in range(0,len(split_str_new_list)):
            if split_str_new_list[i] == file_content:
                pass_list.append("PASS")
        
        if "PASS" in pass_list :
            # print(pass_list)
            print("PASS")
        else :
            print(split_str_new)
            print("!!!!!!!!! FAIL !!!!!!!!!")

        print("======================================")

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
        print("ECU_CV = " + zip_files[0])
        zip_split = zip_files[0].split("-")
        split_str_new = str(zip_files[0]).strip(str(zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1]))
        split_str_new_list.append(split_str_new)
        # label=Label(frame, text="ECU_CV = " + zip_files[0]).pack()

        
        # 파일 열기
        with open(file_path+ECU_CV+ECU_CV_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        print("Version_txt = " + file_content)
        # label=Label(frame, text="Version_txt = " + file_content).pack()

        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
        pass_list=[]

        for i in range(0,len(split_str_new_list)):
            if split_str_new_list[i] == file_content:
                pass_list.append("PASS")
        
        if "PASS" in pass_list :
            # print(pass_list)
            print("PASS")
        else :
            print(split_str_new)
            print("!!!!!!!!! FAIL !!!!!!!!!")
        
        print("======================================")

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
        print("System = " + zip_files[0])
        zip_split = zip_files[0].split("-")
        split_str_new = str(zip_files[0]).strip(str(zip_split[-3]+"-"+zip_split[-2]+"-"+zip_split[-1]))
        split_str_new_list.append(split_str_new)
        # label=Label(frame, text="System = " + zip_files[0]).pack()

        # 파일 열기
        with open(file_path+System+Sys_txt, "r", encoding="utf-8") as file:
            file_content = file.read()
        print("Version_txt = " + file_content)
        # label=Label(frame, text="Version_txt = " + file_content).pack()

        # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
        pass_list=[]

        for i in range(0,len(split_str_new_list)):
            if split_str_new_list[i] == file_content:
                pass_list.append("PASS")
        
        if "PASS" in pass_list :
            # print(pass_list)
            print("PASS")
        else :
            print(split_str_new)
            print("!!!!!!!!! FAIL !!!!!!!!!") 

        print("======================================")

    else:
        pass
    
    return

GDSM()