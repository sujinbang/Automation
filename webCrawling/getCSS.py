
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