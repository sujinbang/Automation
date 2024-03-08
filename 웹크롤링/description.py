# -*- coding: utf-8 -*-
# GIMS Description 크롤링으로 자동화 구현
import sys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as ex
import pyautogui
from bs4 import BeautifulSoup as bs
import getChromeDriver
import getCSS



# 크롤링 시작
driver = getChromeDriver.driver
driver.get('https://gims.gitauto.com:8080/jira/browse/GDSN-10324')

# 계정 정보 입력
# id = input("아이디: ")
id = '230044'
# pw = input("비밀번호: ")
pw = 'QWER!@34'
eId = driver.find_element(By.XPATH, "//input[@name='os_username']").send_keys(id)
ePw = driver.find_element(By.XPATH, "//input[@name='os_password']").send_keys(pw)
loginBtn = driver.find_element(By.NAME, 'login').click()


# nowSugang = driver.find_element(By.XPATH, "//div[@class='status']//div[@class='fl']").click()

time.sleep(3)


# 현대/기아 선택
project = input("현대/기아 중 선택해주세요[현대 or 기아 로 입력] : ")
if project == '현대' or project == '기아':
	pass
else :
	project = input('다시 입력하세요[현대 or 기아 로 입력] : ')

# 서비스센터/협력사 선택
customer = input("센터/협력사 중 선택해주세요[센터 or 협력사 로 입력] :")
if customer == '센터' or customer == '협력사':
	pass
else :
	customer = input('다시 입력하세요[센터 or 협력사 로 입력] : ')


# 변수 선언
# subject = 'input("제목 : ")'
# program1 = 'input("프로그램 : ")'
# resource = 'input("리소스 : ")'
# system = 'input("시스템 : ")'
# supportApp = 'input("서포트 앱 : ")'
# vci2 = 'input("VCI II : ")'
# vci3 = 'input("VCI III : ")'
# gdsvci = 'input("GDSVCI : ")'
# tpms = 'input("TPMS : ")'
# program2 = 'input("프로그램 : ")'

# ticket 기반
ticket = 'https://gims.gitauto.com:8080/jira/browse/'
result_url1 = ticket + str(input('진단에 넣을 승용 GIMS 이슈 번호를 입력하세요 : '))
result_url2 = ticket + str(input('진단에 넣을 상용 GIMS 이슈 번호를 입력하세요 : '))
ecu_url = ticket + str(input('ECU 업그레이드에 넣을 GIMS 이슈 번호를 입력하세요 : '))


# 진단
def result_out(result_url1, result_url2) :

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

	return list_res



# ECU
def ecu_out(ecu_url) :

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

	return list_ecu


# 현대와 기아 결과값 나누기
result = result_out(result_url1, result_url2)
num_res = result.find('KMC')
if (project == '현대' and customer == '센터') :
	result = result[:num_res-1]
elif (project == '기아' and customer == '센터') :
	result = result[num_res-1:]
else :
	result = result

ecu = ecu_out(ecu_url)
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
html_output = getCSS.updateCss + """
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

driver.close()

# print(result)

# 내수 고객사별 정리
file_path = 'Z:\\999_sjbang\\웹크롤링\\'
if project == '현대' and customer == '센터':
	file_name = '하이테크센터 현대.html'
elif project == '현대' and customer == '협력사':
	file_name = '블루핸즈 현대.html'
elif project == '기아' and customer == '센터':
	file_name = '기아 서비스 센터.html'
elif project == '기아' and customer == '협력사':
	file_name = '기아 협력사.html'

# html 파일로 저장
def printsave(*a):
    file = open(file_path+file_name, 'a', encoding='UTF-8')
    # print(*a)
    print(*a,file=file)
    file.close()

printsave(html_output)

print("완료")
