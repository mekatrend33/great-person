import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# This must come before any other Streamlit commands
st.set_page_config(layout="wide") # Use wide layout for better plot display

# --- Matplotlib Font Setup (Same as original) ---
# 한글 폰트 설정 (Windows: Malgun Gothic, macOS: AppleGothic, Linux: NanumGothic 등)
# 사용하시는 OS에 맞게 폰트 이름을 설정해주세요.
# 해당 폰트가 설치되어 있어야 합니다.
try:
    plt.rcParams['font.family'] = 'Malgun Gothic' # Windows
except:
    try:
        plt.rcParams['font.family'] = 'AppleGothic' # macOS
    except:
        try:
            plt.rcParams['font.family'] = 'NanumGothic' # Linux (나눔고딕 설치 필요)
            # If using NanumGothic on a server, ensure it's installed:
            # apt-get update && apt-get install -y fonts-nanum*
        except:
            st.warning("한글 폰트를 찾을 수 없습니다. 기본 폰트로 그래프가 그려집니다.")
plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

# --- Data Generation (Same as original) ---
@st.cache_data # Cache data generation for performance
def get_data():
    data = {
        '년도': [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030],
        '출생자수': [16896, 16305, 18192, 18427, 19075, 19723, 20371, 21019, 21667],
        '사망자수': [33403, 32236, 32468, 31767, 31300, 30832, 30365, 29897, 29430],
        '비교': ['실제값', '실제값', '실제값', '추정값', '추정값', '추정값', '추정값', '추정값', '추정값']
    }
    return pd.DataFrame(data)

df = get_data()

# --- Streamlit App ---
st.title("2030 가구수 예측: 년도별 출생자수 및 사망자수 변화") # Updated title to be more descriptive

st.subheader("데이터 테이블")
st.dataframe(df, use_container_width=True)

st.subheader("시각화")

# --- Matplotlib Plotting Logic (Encapsulated in a function for clarity) ---
def create_population_plot(dataframe):
    fig, ax = plt.subplots(figsize=(12, 7))

    n_years = len(dataframe['년도'])
    index = np.arange(n_years)
    bar_width = 0.35

    # 기본 색상
    birth_color_actual = 'skyblue'
    death_color_actual = 'salmon'

    alpha_actual = 1.0
    alpha_estimated = 0.5 # 추정값은 50% 투명도

    # 막대 그래프 그리기
    for i, row in dataframe.iterrows():
        is_estimated = (row['비교'] == '추정값')
        current_alpha = alpha_estimated if is_estimated else alpha_actual
        
        # 출생자수 막대
        ax.bar(index[i] - bar_width/2, row['출생자수'], bar_width,
               color=birth_color_actual,
               alpha=current_alpha,
               edgecolor='grey' if is_estimated else 'black')

        # 사망자수 막대
        ax.bar(index[i] + bar_width/2, row['사망자수'], bar_width,
               color=death_color_actual,
               alpha=current_alpha,
               edgecolor='grey' if is_estimated else 'black')

    # 레이블, 제목, 축 설정
    ax.set_xlabel('년도', fontsize=12)
    ax.set_ylabel('인원수', fontsize=12)
    ax.set_title('년도별 출생자수 및 사망자수', fontsize=15, pad=20)
    ax.set_xticks(index)
    ax.set_xticklabels(dataframe['년도'])

    # 범례 생성
    legend_elements = [
        Patch(facecolor=birth_color_actual, alpha=alpha_actual, edgecolor='black', label='출생자수 (실제값)'),
        Patch(facecolor=birth_color_actual, alpha=alpha_estimated, edgecolor='grey', label='출생자수 (추정값)'),
        Patch(facecolor=death_color_actual, alpha=alpha_actual, edgecolor='black', label='사망자수 (실제값)'),
        Patch(facecolor=death_color_actual, alpha=alpha_estimated, edgecolor='grey', label='사망자수 (추정값)')
    ]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

    # 각 막대 위에 값 표시
    for i, row in dataframe.iterrows():
        is_estimated = (row['비교'] == '추정값')
        current_alpha = alpha_estimated if is_estimated else alpha_actual
        
        ax.text(index[i] - bar_width/2, row['출생자수'] + 500, f"{row['출생자수']:,}", 
                ha='center', va='bottom', fontsize=8, alpha=current_alpha)
        ax.text(index[i] + bar_width/2, row['사망자수'] + 500, f"{row['사망자수']:,}",
                ha='center', va='bottom', fontsize=8, alpha=current_alpha)

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout(rect=[0, 0, 0.85, 1]) 
    
    return fig

# Create and display the plot
fig = create_population_plot(df)
st.pyplot(fig)

st.caption("데이터 출처: 가상 데이터")
st.markdown("""
### 설명
- **실제값**: 2022년, 2023년, 2024년 데이터
- **추정값**: 2025년 이후 데이터 (그래프에서 옅은 색과 회색 테두리로 표시)
- 출생자수는 파란색 계열, 사망자수는 붉은색 계열로 표시됩니다.
""")

# To run this:
# 1. Save as streamlit_app.py (or any other .py name)
# 2. Open your terminal
# 3. Navigate to the directory where you saved the file
# 4. Run: streamlit run streamlit_app.py
