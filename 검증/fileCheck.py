import os
import shutil
import zipfile

# 변수 선언
Rsc = "\Resource"
file_path = input("파일 경로 : ")

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

# 압축 파일 해제
def makedirs():
    for i in range(0,len(zip_files)):
        zip_file_rep = zip_files[i].replace('.zip','')
        file_name = file_path+Rsc+"\\"+zip_file_rep
        if not os.path.exists(zip_file_rep):
            os.makedirs(file_name)
            zipfile.ZipFile(file_path+Rsc+"\\"+zip_files[i]).extractall(file_path+Rsc+"\\"+zip_file_rep)
makedirs()


# os.walk() : 하위 디렉토리와 파일 모두 확인
empty_folders = []
for i in range(0,len(zip_files)):
    zip_file_rep = zip_files[i].replace('.zip','')
    dir_path = file_path+Rsc+"\\"+zip_file_rep

    for (root, dirs, files) in os.walk(dir_path):
        for i in range(0,len(dirs)):
            dir_size = os.path
            print(str(i) + "=" + dirs[i])
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            print(file_size)



        # print(listDir)
        # for file in files:
        #     file_path = os.path.join(root, file)
        #     file_size = os.path.getsize(file_path)
        #     print(file_path)
        #     print(file)
        #     print(file_size)

# 빈 폴더 확인 :  os.listdir()
# 파일 삭제 : os.remove()
# 디렉토리 삭제 : os.rmdir


            
