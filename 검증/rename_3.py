#--
import os

file_path = input("♥♥♥ 파일경로를 입력하세요 : ")

while ( True ) : 

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


    project = input("♥♥♥ 항목을 입력하세요 (Application : 1 | Critical : 2 | Diagnosis : 3 | ECU : 4 | ECU_CV : 5 | System : 6) : ")
    new_name = input("♥♥♥ 바꿀 파일명을 입력하세요 : ")

    # 폴더명 변경

    # Application
    def rename_app(file_path, new_name):
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
    def rename_critical(file_path, new_name):
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
    def rename_diag(file_path, new_name):
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
    def rename_diag(file_path, new_name):
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
    def rename_ECU(file_path, new_name):
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
    def rename_ECU_CV(file_path, new_name):
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
    def rename_sys(file_path, new_name):
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


    # 메인함수 실행
    def main_func():
        if project == '1':
            rename_app(file_path, new_name)
        elif project == '2':
            rename_critical(file_path, new_name)
        elif project == '3':
            rename_diag(file_path, new_name)
        elif project == '4':
            rename_ECU(file_path, new_name)
        elif project == '5':
            rename_ECU_CV(file_path, new_name)
        elif project == '6':
            rename_sys(file_path, new_name)

    main_func()