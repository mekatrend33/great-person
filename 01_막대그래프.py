import streamlit as st
import pandas as pd
# import numpy as np # 이 파일에서는 numpy를 사용하지 않으므로 주석 처리 또는 삭제 가능

# st.set_page_config는 메인 앱(app2.py)에서 한 번만 호출하는 것이 일반적입니다.
# 페이지별로 타이틀이나 아이콘을 다르게 하고 싶다면 각 페이지 파일에 넣을 수 있습니다.
# 여기서는 페이지별로 다른 타이틀과 아이콘을 설정해 보겠습니다.
st.set_page_config(
    page_title="막대그래프 보기", # 페이지에 맞는 타이틀
    page_icon="📊",            # 페이지에 맞는 아이콘
    layout="wide",             # layout은 보통 메인 앱 설정을 따릅니다.
)

st.header("막대그래프")
st.subheader("막대그래프 기능 맛보기") # 오타 수정: 막대그래프프 -> 막대그래프, 맛보기기 -> 맛보기

view = [100, 150, 30, 200, 80] # 데이터 약간 추가
st.write('# Youtube view') # 마크다운 #은 st.header와 유사
st.write('## raw data')    # 마크다운 ##은 st.subheader와 유사
st.write(view)             # view 변수 내용을 직접 출력

st.write('## bar chart')
st.bar_chart(view)

st.write("## Pandas Series로 변환하여 보기")
sview = pd.Series(view, index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri']) # 인덱스 추가
st.write(sview)

st.write("### Pandas Series를 사용한 막대그래프")
st.bar_chart(sview)

# 메인 페이지로 돌아가는 링크 (선택 사항)
st.page_link("app2.py", label="메인 페이지로 돌아가기", icon="🏠")

