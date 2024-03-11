import os
import shutil
import zipfile

while True :
    # 변수 선언
    Rsc = "\Resource"
    file_path = input("파일 경로 : ")

    # 폴더명 추출
    zip_files = []
    def rsc_fileList():
        # file_path = entry_filePath.get()
        # 상위 디렉토리부터 모든 하위 디렉토리 및 파일을 탐색
        for root, dirs, files in os.walk(file_path+Rsc):
            for file in files:
                if file.endswith('.zip'):
                    # 확장자가 .zip인 파일은 리스트에 추가
                    zip_files.append(os.path.join(file))
        return

    # 파일 체크
    empty_folders = []
    def fileCheck():
        # file_path = entry_filePath.get()
        rsc_path = file_path+Rsc
        for i in range(0,len(zip_files)):
            zip_file_rep = zip_files[i].replace('.zip','')
            file_name = file_path+Rsc+"\\"+zip_file_rep

            # 압축 파일 해제
            dirsList = []
            for dirs in os.listdir(rsc_path):
                dirsList.append(dirs)
            if zip_file_rep not in dirsList:
                os.makedirs(file_name)
                zipfile.ZipFile(file_path+Rsc+"\\"+zip_files[i]).extractall(file_path+Rsc+"\\"+zip_file_rep)
            elif zip_file_rep in dirsList:
                shutil.rmtree(file_name)  # 폴더 전체 삭제
                os.makedirs(file_name)
                zipfile.ZipFile(file_path+Rsc+"\\"+zip_files[i]).extractall(file_path+Rsc+"\\"+zip_file_rep)

            # 빈 파일 확인
            for (root, dirs, files) in os.walk(file_name):
                if not dirs:
                    # print("최하위 폴더 :", root)
                    if not files:
                        empty_folders.append(root)

        if len(empty_folders) == 0:
            # label=Label(frame, text="빈 파일이 없습니다", fg="blue").pack()
            print("빈 파일이 없습니다")
        else :
            for i in range(0, len(empty_folders)):
                # label=Label(frame, text=empty_folders[i] + " 파일을 확인하세요", fg="red").pack()
                print(empty_folders[i] + " 파일을 확인하세요")
            
        return


    # 메인 함수 실행
    def main_function():
        rsc_fileList() # 리소스 파일 리스트
        fileCheck() # 파일 확인
        return

    main_function() 
