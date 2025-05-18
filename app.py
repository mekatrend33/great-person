import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="스트림릿 배포하기",  # 오타 수정: 배포하기기 -> 배포하기
    page_icon="👤",
    layout="wide",
)

st.header("스트림릿 배포")  # 오타 수정: 배포포 -> 배포
st.subheader("스트림릿 기능 맛보기") # 오타 수정: 맛보기기 -> 맛보기, subheder -> subheader

st.markdown("### 페이지 이동")
# st.page_link를 사용하여 다른 페이지로 이동하는 링크 생성
# "pages/01_막대그래프.py"는 pages 폴더 내의 실제 파일 경로입니다.
st.page_link("01_막대그래프.py", label="막대그래프 페이지 보기", icon="📊")

st.markdown("---") # 구분선

st.subheader("메트릭 예시") # 섹션 제목 추가
cols = st.columns((1, 1, 2)) # 오타 수정: colums -> columns
# ""2 -> "2" 또는 2 로 수정
cols[0].metric("날짜 10/11", "15ºC", "2")
cols[0].metric("날짜 10/12", "17ºC", "2") # 데이터 약간 변경
cols[0].metric("날짜 10/13", "14ºC", "-1")# 데이터 약간 변경
cols[1].metric("날짜 10/14", "18ºC", "4") # 데이터 약간 변경
cols[1].metric("날짜 10/15", "19ºC", "1") # 데이터 약간 변경
cols[1].metric("날짜 10/16", "16ºC", "-3")# 데이터 약간 변경

# cols[2]는 비워두거나 다른 내용을 추가할 수 있습니다.
cols[2].write("여기는 세 번째 컬럼입니다.")
cols[2].image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)


st.info("""
위 '막대그래프 페이지 보기' 링크를 클릭하거나,
왼쪽 사이드바에서 '01 막대그래프'를 선택하여 해당 페이지로 이동할 수 있습니다.
""")


