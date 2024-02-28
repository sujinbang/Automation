
import os
import shutil
import zipfile

# 폴더 생성
# path = r'Z:\999_sjbang\운영\test\HME\Resource\NEH-02-0001-2024012301-C-RSC'
file_path = input("파일 경로 : ")
# RSC_version = input("리소스 버전 : ")

def makedirs(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
makedirs(file_path)

# 압축 해제
# file = r'Z:\999_sjbang\운영\test\HME\Resource\NEH-02-0001-2024012301-C-RSC.zip'
zip_file = input("해제할 압축파일 : ")
zipfile.ZipFile(zip_file).extractall(file_path)

# 파일 사이즈 확인
def get_human_readable_size(size_in_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024:
            # return f"{size_in_bytes:.2f} {unit}"
            return size_in_bytes, unit
        size_in_bytes /= 1024

# 파일 수, 하위 디렉토리 수 확인
def get_directory_info(directory_path):
    total_size = 0
    total_files = 0
    total_subdirs = 0

    for dirpath, dirnames, filenames in os.walk(directory_path):
        total_subdirs += len(dirnames)
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
            total_files += 1

    return total_size, total_files, total_subdirs


directory_path = file_path
directory_size, file_count, subdir_count = get_directory_info(directory_path)
print(f"resource의 크기: {get_human_readable_size(directory_size)[0]:.2f} {get_human_readable_size(directory_size)[1]}")
print(f"파일 수: {file_count}")
print(f"하위 디렉토리 수: {subdir_count}")



source_directory = file_path
destination_base_directory = r'Z:\999_sjbang\운영\test\HME\Resource\seperate'
def separate_files_by_directory(source_directory, destination_base_directory, files_per_directory=1):
    # source_directory: 원본 파일이 있는 디렉토리
    # destination_base_directory: 분리된 디렉토리가 저장될 기본 디렉토리
    # files_per_directory: 각 하위 디렉토리당 파일 수

    # 대상 디렉토리가 존재하지 않으면 생성
    if not os.path.exists(destination_base_directory):
        os.makedirs(destination_base_directory)

    # 원본 디렉토리의 파일 목록 가져오기
    files = os.listdir(source_directory)

    # 파일을 files_per_directory 개수로 나누어 디렉토리에 복사
    for i in range(0, len(files), files_per_directory):
        # 파일명 규칙
        directory_name = f'NEH-02-0001-20240123{i // files_per_directory}-C-RSC'
        destination_directory = os.path.join(destination_base_directory, directory_name)

        # 대상 디렉토리가 존재하지 않으면 생성
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        # 파일을 대상 디렉토리로 이동
        for file_name in files[i:i + files_per_directory]:
            source_path = os.path.join(source_directory, file_name)
            destination_path = os.path.join(destination_directory, file_name)
            shutil.move(source_path, destination_path)

# 예제 사용
separate_files_by_directory(source_directory, destination_base_directory, files_per_directory=1)

# # separate 파일 다시 압축
# def zip_directory(directory_to_zip, zip_file_name):
#     with zipfile.ZipFile(zip_file_name, 'w') as zipf:
#         for root, dirs, files in os.walk(directory_to_zip):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 arcname = os.path.relpath(file_path, directory_to_zip)
#                 zipf.write(file_path, arcname=arcname)

# # 디렉토리 압축
# zip_directory('path/to/your/directory', 'output_zip.zip')
