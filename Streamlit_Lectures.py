from pathlib import Path

import streamlit as st

st.set_page_config(      #페이지 설정
    page_title = '최원겸의 Streamlit', # 페이지 타이틀
    page_icon=str(Path(__file__).parent / "page_icon.png"), # 페이지 아이콘
    layout = 'wide', # 페이지 레이아웃: centered,wide
    initial_sidebar_state = 'expanded',# 사이드바 초기상태 : auto,collapsed,expanded
    # 페이지 오른쪽 상부의 메뉴에 추가할 메뉴 항목: Get help, Report a bug, About
    menu_items = {
        'Get help': 'https://docs.streamlit.io',
        'Report a bug': 'https://streamlit.io',
        'About': "### 최원겸 \n - [홍익대학교 산업데이터공학과](https://cn2.hongik.ac.kr')"
    }
)

#사이드바 설정
st.sidebar.title('다양한 사이드바 위젯들')
#사이드바 타이틀

st.sidebar.write('메뉴 항목')
#메뉴 항목 출력
st.sidebar.checkbox('외국인 포함')
#체크박스: 외국인 포함
st.sidebar.checkbox('고령인구 포함')
#체크박스: 고령인구 포함
st.sidebar.divider()
#구분선
st.sidebar.radio('데이터 타입',['전체','남성','여성'])
#라디오 버튼: 전체,남성,여성
st.sidebar.slider('나이',0,100,(20,50))
#나이 슬라이더: 0~100, 기본값(20,50)
st.sidebar.selectbox('지역',['서울','부산','대구','인천','광주','대전','울산','세종','경기','강원','충북','충남','전북','전남','경북','경남','제주'])

