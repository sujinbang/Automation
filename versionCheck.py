import os



while ( True ) : 

    project = input("♥♥♥ 프로젝트를 입력하세요(3세대/4세대/Gscan) : ")
    file_path = input("♥♥♥ 파일경로를 입력하세요 : ")

    def GDSN(file_path):

        # 변수 선언
        App = "\Application"
        App_txt = "\Application_Version.txt"
        Rsc = "\Resource"
        Rsc_txt = "\Resource_Version.txt"
        SupportApp = "\SupportApp"
        SupportApp_txt = "\SupportApp_Version.txt"
        System = "\system"
        Sys_txt = "\System_Version.txt"

        print("======================================")

        # Application-----------------------------------

        if "Application" in os.listdir(file_path):

            # 폴더명 추출
            for item in os.listdir(file_path+App):
                sub_folder = os.path.join(file_path+App, item) # 폴더경로 + 폴더명
                sub_folder2 = os.path.join(item) # 폴더명만
                if os.path.isdir(sub_folder):
                    # print("Application_version = " + sub_folder2)
                    print("Application = " + sub_folder2)

            # 파일 열기
            with open(file_path+App+App_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
                print("Application_version_txt = " + file_content)

            print("======================================")

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

            # ZIP 파일 목록 출력
            if len(zip_files) >= 2:
                for i in range(0,len(zip_files)):
                    print("Resource = " + zip_files[i])

            elif len(zip_files) == 1:
                print("Resource = " + zip_files[0])
            
            # 파일 열기
            with open(file_path+Rsc+Rsc_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("Resource_version_txt = " + file_content)

            print("======================================")

        else:
            pass



        # SupportApp----------------------------------
        
        if "SupportApp" in os.listdir(file_path):
            # 폴더명 추출
            for item in os.listdir(file_path+SupportApp):
                sub_folder = os.path.join(file_path+SupportApp, item) # 폴더경로 + 폴더명
                sub_folder2 = os.path.join(item) # 폴더명만
                if os.path.isdir(sub_folder):
                    # print("Application_version = " + sub_folder2)
                    print("SupportApp = " + sub_folder2)
            
            # 파일 열기
            with open(file_path+SupportApp+SupportApp_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("SupportApp_version_txt = " + file_content)
            
            print("======================================")

        else:
            pass


        # System--------------------------------------
        
        if "system" in os.listdir(file_path):

            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+System):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            # ZIP 파일 목록 출력
            print("System = " + zip_files[0])

            # 파일 열기
            with open(file_path+System+Sys_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("System_version_txt = " + file_content)

            print("======================================")

        else:
            pass
        
        return
    
    def GDSM(file_path):
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

        print("======================================")

        # Application-----------------------------------

        if "Application" in os.listdir(file_path):

            # 폴더명 추출
            for item in os.listdir(file_path+App):
                sub_folder = os.path.join(file_path+App, item) # 폴더경로 + 폴더명
                sub_folder2 = os.path.join(item) # 폴더명만
                if os.path.isdir(sub_folder):
                    print("Application = " + sub_folder2)

            # 파일 열기
            with open(file_path+App+App_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
                print("Application_version_txt = " + file_content)

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

            # ZIP 파일 목록 출력
            print("Critical = " + zip_files[0])
            
            # 파일 열기
            with open(file_path+Critical+Critical_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("Critical_version_txt = " + file_content)
            
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

            # ZIP 파일 목록 출력
            print("Diagnosis = " + zip_files[0])
            
            # 파일 열기
            with open(file_path+Diagnosis+Diagnosis_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("Diagnosis_version_txt = " + file_content)
            
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

            # ZIP 파일 목록 출력
            print("Diagnosis_CV = " + zip_files[0])
            
            # 파일 열기
            with open(file_path+Diagnosis_CV+Diagnosis_CV_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("Diagnosis_CV_version_txt = " + file_content)
            
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

            # ZIP 파일 목록 출력
            print("ECU = " + zip_files[0])
            
            # 파일 열기
            with open(file_path+ECU+ECU_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("ECU_version_txt = " + file_content)
            
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

            # ZIP 파일 목록 출력
            print("ECU_CV = " + zip_files[0])
            
            # 파일 열기
            with open(file_path+ECU_CV+ECU_CV_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("ECU_CV_version_txt = " + file_content)
            
            print("======================================")

        else:
            pass

        # System--------------------------------------
        
        if "System" in os.listdir(file_path):

            zip_files = []

            # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
            for root, dirs, files in os.walk(file_path+System):
                for file in files:
                    if file.endswith('.zip'):
                        # 확장자가 .zip인 파일은 리스트에 추가
                        zip_files.append(os.path.join(file))

            # ZIP 파일 목록 출력
            print("System = " + zip_files[0])

            # 파일 열기
            with open(file_path+System+Sys_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("System_version_txt = " + file_content)

            print("======================================")

        else:
            pass
        
        return        

    def Gscan(file_path):
        # 변수 선언
        App = r"\application"
        App_txt = r"\application_version.txt"
        critical = "\critical"
        critical_txt = "\critical_version.txt"
        diagnosis = "\diagnosis"
        diagnosis_txt = "\diagnosis_version.txt"
        diagnosis_cv = "\diagnosis_cv"
        diagnosis_cv_txt = "\diagnosis_cv_version.txt"
        diagnosis_im = "\diagnosis_im"
        diagnosis_im_txt = "\diagnosis_im_version.txt"
        gscan_os = "\os"
        gscan_os_txt = "\os_version.txt"
        system = "\system"
        sys_txt = "\system_version.txt"

        print("======================================")

        # application-----------------------------------

        if "application" in os.listdir(file_path):

            # 폴더명 추출
            for item in os.listdir(file_path+App):
                sub_folder = os.path.join(file_path+App, item) # 폴더경로 + 폴더명
                sub_folder2 = os.path.join(item) # 폴더명만
                if os.path.isdir(sub_folder):
                    print("application = " + sub_folder2)

            # 파일 열기
            with open(file_path+App+App_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
                print("application_version_txt = " + file_content)

            print("======================================")

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
            print("critical = " + zip_files[0])
            
            # 파일 열기
            with open(file_path+critical+critical_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("critical_version_txt = " + file_content)
            
            print("======================================")

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
            print("diagnosis = " + zip_files[0])
            
            # 파일 열기
            with open(file_path+diagnosis+diagnosis_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("diagnosis_version_txt = " + file_content)
            
            print("======================================")

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
            print("diagnosis_cv = " + zip_files[0])
            
            # 파일 열기
            with open(file_path+diagnosis_cv+diagnosis_cv_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("diagnosis_cv_version_txt = " + file_content)
            
            print("======================================")

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
            print("diagnosis_im = " + zip_files[0])
            
            # 파일 열기
            with open(file_path+diagnosis_im+diagnosis_im_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("diagnosis_im_version_txt = " + file_content)
            
            print("======================================")

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
            print("os = " + zip_files[0])
            
            # 파일 열기
            with open(file_path+gscan_os+gscan_os_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("os_version_txt = " + file_content)
            
            print("======================================")

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
            print("system = " + zip_files[0])

            # 파일 열기
            with open(file_path+system+sys_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("system_version_txt = " + file_content)

            print("======================================")

        else:
            pass
    
        return

    # 메인 함수 실행

    def main_function():
        if project == "3세대" :
            GDSM(file_path)
        elif project == "4세대" :
            GDSN(file_path)
        elif project == "Gscan" :
            Gscan(file_path)
        
        return

    main_function()