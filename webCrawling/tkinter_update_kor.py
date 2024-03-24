# -*- coding: utf-8 -*-
# GIMS Description 크롤링으로 자동화 구현
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
# tkinter
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk

import chromedriver_autoinstaller

# Get driver and open url
# driver = webdriver.Chrome()

def main_func():

	# # 현대/기아 선택
	# project = input("현대/기아 중 선택해주세요[현대 or 기아 로 입력] : ")
	if selected_item1.get() == '1':
		project = '현대'
	elif selected_item1.get() == '2':
		project = '기아'

	# # 서비스센터/협력사 선택
	# customer = input("센터/협력사 중 선택해주세요[센터 or 협력사 로 입력] :")
	if selected_item2.get() == '1':
		customer = '센터'
	elif selected_item2.get() == '2':
		customer = '협력사'

	# # ticket 기반
	ticket = 'https://gims.gitauto.com:8080/jira/browse/'
	# issue1 = input('진단에 넣을 승용 GIMS 이슈 번호를 입력하세요 : ')
	issue1 = entry_gims1.get()
	result_url1 = ticket + issue1
	# issue2 = input('진단에 넣을 상용 GIMS 이슈 번호를 입력하세요 : ')
	issue2 = entry_gims2.get()
	result_url2 = ticket + issue2
	# issue_ecu = input('ECU 업그레이드에 넣을 GIMS 이슈 번호를 입력하세요 : ')
	issue_ecu = entry_gims3.get()
	ecu_url = ticket + issue_ecu

	# 현대와 기아 결과값 나누기
	return_list = result_out(result_url1, result_url2, ecu_url)

	result = return_list[0]
	num_res = result.find('KMC')
	if (project == '현대' and customer == '센터') :
		result = result[:num_res-1]
	elif (project == '기아' and customer == '센터') :
		result = result[num_res-1:]
	else :
		result = result

	ecu = return_list[1]
	num_ecu = ecu.find('KMC')
	if (project == '현대' and customer == '센터'):
		ecu = ecu[:num_ecu-1]
	elif (project == '기아' and customer == '센터'):
		ecu = ecu[num_ecu-1:]
	else :
		ecu = ecu

	#연구소 내부 공유 삭제
	if (result.find('연구소 내부') != -1) :
		num_res2 = result.find('연구소 내부')
		result = result[:num_res2-1] + result[num_res-1:]
	else : 
		result = result

	if (ecu.find('연구소 내부') != -1) :
		num_ecu2 = ecu.find('연구소 내부')
		ecu = ecu[:num_ecu2-1] + ecu[num_ecu-1:]
	else :
		ecu = ecu

	# 이미지 로고
	if (project == '현대') :
		GITimg = "https://image.gitauto.com/gitauto/kor/popup/logo_gdssmart_test_bang.png"
		GITstring = "GDS SMART를"
	elif(project == '기아') :
		GITimg = "https://image.gitauto.com/gitauto/kor/popup/logo_kds_2_test_bang.png"
		GITstring = "KDS 2.0을"

	# html 결과문
	
	updateCss = """  
	<br>
	<br>
	<div> <!-- 업데이트 문서 시작 -->
	<style>
		
		/* 상단 img 속성*/
		.GITimg {
		color: #555;
		display: flex;
		align-items: center; /* 가운데 정렬 */
		text-align: left;
		margin-left: 10%;
		margin-right: 10%;
		}
		
		/* 목차 */
		.GITContents {
		margin: 10px;
		margin-left: 10%;
		font-size: 18px;
		}
		
		/* 상단 안내문 */
		.GITstring {
		margin: 10px;
		margin-left: 10%;
		margin-right: 10%;
		font-size: 15px;
		}

		/*GIT 표 제목*/
		.GITth {
		background-color: #ddd;
		color: #555;
		padding: 11px;
		text-align: left;
		border-bottom: 1px solid #ddd;
		border-right: 1px solid #ddd;
		}
		
		/*GIT 표 내용*/
		.GITtd {
		padding: 11px;
		text-align: left;
		padding-left: 20px;
		line-height: 1.5; /* 행간을 조절할 수 있음, 필요에 따라 조절 가능 */
		font-size: 15px;
		border-bottom: 1px solid #ddd;
		border-right: 1px solid #ddd;
		}
		
		/*GIT 버전 정보 표 내용*/
		.GITtd_version {
		font-size: 15px;
		margin-bottom: 10px;
		}
		
		
		/* 동그라미 */
		.version-symbol {
		font-size: 1em;
		color: #333;
		}
		
		/* 네모 */
		.square-bullet {
		display: inline-block;
		width: 10px; /* 네모의 너비 조절 */
		height: 10px; /* 네모의 높이 조절 */
		background-color: #333; /* 네모의 배경색 지정 */
		margin-right: 5px; /* 네모와 텍스트 사이의 간격 조절 */
		}
		
		/* 첫 번째 표 스타일 */
		table#GITversion-table th {
		background-color: #ddd;
		color: #555;
		width: 50%;
		text-align: center;
		}

		table#GITversion-table {
		background-color: #ffffff;
		width: 80%;
		margin: 20px auto;
		border-collapse: collapse;
		background-color: #fff;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
		}

		/* 두 번째 표 스타일 */
		table#GITupdate-table th {
		background-color: #ddd;
		color: #555;
		text-align: center;
		}

		table#GITupdate-table {
		background-color: #ffffff;
		width: 80%;
		margin: 20px auto;
		border-collapse: collapse;
		background-color: #fff;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
		}
	</style>

	"""	

	html_output = updateCss + """
	<p class="GITimg"><img src=""" + GITimg + """ alt="Logo" style="width: 197px; height: 29px"></p>  
	<br>
	<p class="GITstring"><strong>
	"""+ GITstring +""" 더 편하게 이용하실 수 있도록 업데이트가 다음과 같이 진행되어 안내해 드립니다.
	</strong></p>
	<br>
	<p class="GITContents"><span class="square-bullet"></span><strong> 버전 정보</strong></p>
	<table id="GITversion-table">
		<tr>
		<th class="GITth">업데이트 버전</th>
		<th class="GITth">펌웨어</th>
		</tr>
			<!-- 수작업 필요 -->
		<tr>
		<td class="GITtd">
		<p class="GITtd_version"><span class="version-symbol">&#8226;</span> 프로그램 : NSH-01-0138 </p>
		<p class="GITtd_version"><span class="version-symbol">&#8226;</span> 리소스 : NSH-01-0157 </p>
		<p class="GITtd_version"><span class="version-symbol">&#8226;</span> 시스템 : NSH-01-0125 </p>
		<p class="GITtd_version"><span class="version-symbol">&#8226;</span> 서포트 앱 : NSH-01-0006 </p>
		</td>
		<td class="GITtd">
		<p class="GITtd_version"><span class="version-symbol">&#8226;</span> VCI II : 2.86 </p>
		<p class="GITtd_version"><span class="version-symbol">&#8226;</span> VCI III : 00.42 </p>
		<p class="GITtd_version"><span class="version-symbol">&#8226;</span> GDS VCI : 1.41 </p>
		<p class="GITtd_version"><span class="version-symbol">&#8226;</span> TPMS : 3.4 </p>
		</td>
		</tr>
		<!-- 추가 업데이트 항목을 필요에 따라 계속해서 추가하세요. -->
	</table>
	<br>
	<p class="GITContents"><span class="square-bullet"></span><strong> 업데이트 정보</strong></p>
	
	<table id="GITupdate-table">
		<tr>
		<th class="GITth">구분</th>
		<th class="GITth">상세 내역</th>
		</tr>
		<tr>
		<td class="GITtd">프로그램</td>
		<td class="GITtd">펌웨어 업데이트 : VCI III 00.42</td>
		</tr>
		<tr>
		<td class="GITtd">진단</td>
		<td class="GITtd">
			""" + result + """
		</td>
		</tr>
		<tr>
		<td class="GITtd">ECU 업데이트</td>
		<td class="GITtd">
		"""+ ecu +"""
		</td>
		</tr>
	</table>
	<br>
	<p class="GITimg"><img src="https://image.gitauto.com/gitauto/kor/common/top_logo.png" alt="logo"></p>
	<br>
	<br>
	</div>


	"""


	file_path = entry_filePath.get()

	if project == '현대' and customer == '센터':
		file_name = '하이테크센터 현대.html'
	elif project == '현대' and customer == '협력사':
		file_name = '블루핸즈 현대.html'
	elif project == '기아' and customer == '센터':
		file_name = '기아 서비스 센터.html'
	elif project == '기아' and customer == '협력사':
		file_name = '기아 협력사.html'

	printsave(html_output)

	info()

	return

# 진단
def result_out(result_url1, result_url2, ecu_url) :

	# 웹크롤링
	# Check if chrome driver is installed or not
	chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
	# driver_path = f'./{chrome_ver}/chromedriver.exe'
	driver_path = 'Z:\999_sjbang\웹크롤링\120\chromedriver.exe'

	# if os.path.exists(driver_path):
	# 	print(f"chrome driver is insatlled: {driver_path}")

	# else:
	# 	print(f"install the chrome driver(ver: {chrome_ver})")
	# 	chromedriver_autoinstaller.install(True)


	if getattr(sys, 'frozen', False) and hasattr(sys, "_MEIPASS"):
		driver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
		driver = webdriver.Chrome()
	# print('running in a Pyinstaller bundle')
	else:
		driver = webdriver.Chrome()
		# print('running in a normal Python process')

	# 계정 입력
	# id = input("아이디를 입력하세요 : ")
	id = entry_id.get()
	# pw = input("비밀번호를 입력하세요 : ")
	pw = entry_pw.get()

	# 크롤링 시작
	driver.get('https://gims.gitauto.com:8080/jira/browse/GDSN-10324')

	eId = driver.find_element(By.XPATH, "//input[@name='os_username']").send_keys(id)
	ePw = driver.find_element(By.XPATH, "//input[@name='os_password']").send_keys(pw)
	loginBtn = driver.find_element(By.NAME, 'login').click()

	time.sleep(3)

	#-------------------------------------------------------------------------------

	# # 현대/기아 선택
	# project = input("현대/기아 중 선택해주세요[현대 or 기아 로 입력] : ")
	if selected_item1.get() == '1':
		project = '현대'
	elif selected_item1.get() == '2':
		project = '기아'

	# # 서비스센터/협력사 선택
	# customer = input("센터/협력사 중 선택해주세요[센터 or 협력사 로 입력] :")
	if selected_item2.get() == '1':
		customer = '센터'
	elif selected_item2.get() == '2':
		customer = '협력사'

	# driver = webdriver.Chrome()

	if (project == '현대' and customer == '협력사') or (project == '기아' and customer == '협력사'):
		# selenium
		driver.get(result_url1)
		
		# Beautiful Soup - Jira 티켓 내부 값 불러오기
		html = driver.page_source
		soup = bs(html, "html.parser")
		html = soup.select('div.user-content-block')

		list1 = []
		for text in html:
			list1.append(text.get_text())
		
		time.sleep(3)
		
		driver.get(result_url2)

		# Beautiful Soup - Jira 티켓 내부 값 불러오기
		html = driver.page_source
		soup = bs(html, "html.parser")
		html = soup.select('div.user-content-block')

		list2 = []
		for text in html:
			list2.append(text.get_text())
		
		list = list1+list2

		# 티켓 내부 값 에서 줄바꿈표시를 <br>로 변경
		list_res = list[0].replace('\n', '<br>') + list[1].replace('\n', '<br>')
		list_res = list_res.replace('\xa0', '')

	
	elif (project == '현대' and customer == '센터') or (project == '기아' and customer == '센터'):
		# selenium
		driver.get(result_url1)
		
		# Beautiful Soup - Jira 티켓 내부 값 불러오기
		html = driver.page_source
		soup = bs(html, "html.parser")
		html = soup.select('div.user-content-block')

		list = []
		for text in html:
			list.append(text.get_text())

		# 티켓 내부 값 에서 줄바꿈표시를 <br>로 변경
		list_res = list[0].replace('\n', '<br>')
		list_res = list_res.replace('\xa0', '')

	time.sleep(3)

	# selenium
	driver.get(ecu_url)

	time.sleep(3)

	# Beautiful Soup - Jira 티켓 내부 값 불러오기
	html = driver.page_source
	soup = bs(html, "html.parser")
	html = soup.select('div.user-content-block')

	list = []
	for text in html:
			# print(text.get_text())
		list.append(text.get_text())

	# 티켓 내부 값 에서 줄바꿈표시를 <br>로 변경
	list_ecu = list[0].replace('\n', '<br>')
	list_ecu = list_ecu.replace('\xa0', '')

	time.sleep(3)

	driver.close()

	return list_res, list_ecu


# html 파일로 저장
def printsave(*a):

	file_path = entry_filePath.get() + "\\"

	# 현대/기아 선택
	# project = input("현대/기아 중 선택해주세요[현대 or 기아 로 입력] : ")
	if selected_item1.get() == '1':
		project = '현대'
	elif selected_item1.get() == '2':
		project = '기아'

	# 서비스센터/협력사 선택
	# customer = input("센터/협력사 중 선택해주세요[센터 or 협력사 로 입력] :")
	if selected_item2.get() == '1':
		customer = '센터'
	elif selected_item2.get() == '2':
		customer = '협력사'

	if project == '현대' and customer == '센터':
		file_name = '하이테크센터 현대.html'
	elif project == '현대' and customer == '협력사':
		file_name = '블루핸즈 현대.html'
	elif project == '기아' and customer == '센터':
		file_name = '기아 서비스 센터.html'
	elif project == '기아' and customer == '협력사':
		file_name = '기아 협력사.html'

	# 내수 고객사별 정리
	file = open(file_path+file_name, 'a', encoding='UTF-8')
	# print(*a)
	print(*a,file=file)
	file.close()

	return

# 메시지 박스
def info():
    messagebox.showinfo("알림", "html 파일 생성 완료!")

# tkinter
# 화면 가운데 위치
window = Tk()
window.title("업데이트 문서 자동 작성 프로그램")
# window.geometry("400x700")
window_width = 400
window_height = 700  # 높이 조정
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

label_frame1 = ttk.LabelFrame(window, text="설정")
label_frame1.pack(padx=10, pady=10, fill="x", expand=True)

# 계정 정보 입력
label_id=ttk.Label(label_frame1, text="아이디 : ")
label_id.pack(anchor='w')

entry_id = ttk.Entry(label_frame1, width=50, justify="center")
entry_id.pack(padx=5, pady=5)

label_pw=ttk.Label(label_frame1, text="비밀번호 : ")
label_pw.pack(anchor='w')

entry_pw = ttk.Entry(label_frame1, width=50, justify="center")
entry_pw.pack(padx=5, pady=5)

# 현대/기아 선택
label_project=ttk.Label(label_frame1, text="현대/기아 중 선택")
label_project.pack(anchor='w')

# 라디오 버튼
selected_item1 = tk.StringVar()
items = (('현대', '1'),
        ('기아', '2'))

# 라디오 버튼을 팩에 배치
for item in items:
    r = ttk.Radiobutton(
        label_frame1,
        text=item[0],
        value=item[1],
        variable=selected_item1
    )
    # 팩에 배치
    r.pack(padx=5, pady=5)

# 센터/협력사 선택
label_gbn=ttk.Label(label_frame1, text="센터/협력사 중 선택")
label_gbn.pack(anchor='w')

# 라디오 버튼
selected_item2 = tk.StringVar()
items = (('센터', '1'),
        ('협력사', '2'))

# 라디오 버튼을 팩에 배치
for item in items:
    r = ttk.Radiobutton(
        label_frame1,
        text=item[0],
        value=item[1],
        variable=selected_item2
    )
    # 팩에 배치
    r.pack(padx=5, pady=5)

label_frame2=ttk.Label(label_frame1, text="[GIMS 이슈 번호 입력]")
label_frame2.pack(anchor='w')

# GIMS 이슈 번호 입력
label_gims1=ttk.Label(label_frame1, text="1) 승용 : ")
label_gims1.pack(anchor='w')

entry_gims1 = ttk.Entry(label_frame1, width=50, justify="center")
entry_gims1.pack(padx=5, pady=5)

label_gims2=ttk.Label(label_frame1, text="2) 상용 : ")
label_gims2.pack(anchor='w')

entry_gims2 = ttk.Entry(label_frame1, width=50, justify="center")
entry_gims2.pack(padx=5, pady=5)

label_gims3=ttk.Label(label_frame1, text="3) ECU 업그레이드 : ")
label_gims3.pack(anchor='w')

entry_gims3 = ttk.Entry(label_frame1, width=50, justify="center")
entry_gims3.pack(padx=5, pady=5)

# 저장 파일 경로
label_filePath=ttk.Label(label_frame1, text="저장 파일 경로 : ")
label_filePath.pack(anchor='w')

entry_filePath = ttk.Entry(label_frame1, width=50, justify="center")
entry_filePath.pack(padx=5, pady=5)

Btn = ttk.Button(label_frame1, text="시작...", command=main_func).pack(pady=5)



window.mainloop()





