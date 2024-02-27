import os

while ( True ) : 

    def GDSN():

        project = input("♥♥♥ 프로젝트를 입력하세요(3세대 : 3 || 4세대 : 4 || Gscan : G) : ")
        file_path = input("♥♥♥ 파일경로를 입력하세요 : ")


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

            item_list = []

            # 폴더명 추출
            for item in os.listdir(file_path+App):
                sub_folder = os.path.join(file_path+App, item) # 폴더경로 + 폴더명
                if os.path.isdir(sub_folder):
                    if '.txt' not in item:
                        item_list.append(item)
                        # print("Application_version = " + sub_folder2)
                        print("Application = " + item)


            # 파일 열기
            with open(file_path+App+App_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
                print("Version_txt = " + file_content)

            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)  
            if item_list[0] != file_content:
                print("!!!!!!!! FAIL !!!!!!!!")
            else :
                print("PASS")

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

            split_str_new_list = []
            # ZIP 파일 목록 출력
            if len(zip_files) >= 2:
                for i in range(0,len(zip_files)):
                    print("Resource = " + zip_files[i])
                    zip_split = zip_files[i].split("-")
                    split_str_new = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]
                    split_str_new_list.append(split_str_new)

            elif len(zip_files) == 1:
                print("Resource = " + zip_files[0])
                zip_split = zip_files[0].split("-")
                split_str_new = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]
                split_str_new_list.append(split_str_new)
            
            # 파일 열기
            with open(file_path+Rsc+Rsc_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("Version_txt = " + file_content)


            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)
            pass_list=[]

            for i in range(0,len(split_str_new_list)):
                if split_str_new_list[i] == file_content:
                    pass_list.append("PASS")
            
            if "PASS" in pass_list :
                print(pass_list)
                print("PASS")
            else :
                print("!!!!!!!!! FAIL !!!!!!!!!")

            print("======================================")

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
                        print("SupportApp = " + item)

            # 파일 열기
            with open(file_path+SupportApp+SupportApp_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("Version_txt = " + file_content)

            # 폴더명과 버전 txt가 같은지 (PASS/FAIL)          
            if item_list[0] != file_content:
                print("!!!!!!!! FAIL !!!!!!!!")
                print(item_list[0], file_content)
            else :
                print("PASS")            
            
            print("======================================")

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
            print("System = " + zip_files[0])
            zip_split = zip_files[0].split("-")
            split_str_new = zip_split[0]+"-"+zip_split[1]+"-"+zip_split[2]
            split_str_new_list.append(split_str_new)

            # 파일 열기
            with open(file_path+System+Sys_txt, "r", encoding="utf-8") as file:
                file_content = file.read()
            print("Version_txt = " + file_content)

            pass_list=[]

            for i in range(0,len(split_str_new_list)):
                if split_str_new_list[i] == file_content:
                    pass_list.append("PASS")
            
            if "PASS" in pass_list :
                print(pass_list)
                print("PASS")
            else :
                print("!!!!!!!!! FAIL !!!!!!!!!")            

            print("======================================")

        else:
            pass
        
        return
    
    GDSN()
