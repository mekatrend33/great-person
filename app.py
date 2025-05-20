import streamlit as st

# --- Configuration ---
st.set_page_config(
    page_title="위대한 위인 검색",
    page_icon="🌟",  # Optional: you can use an emoji or a URL to an icon
    layout="wide"    # Use wide layout to better match the image
)

# --- Data for Great People ---
# In a real application, this data might come from a database or a CSV file.
people_data = [
    {
        "name_korean": "아이작 뉴턴",
        "name_english": "Isaac Newton",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/GodfreyKneller-IsaacNewton-1689.jpg/440px-GodfreyKneller-IsaacNewton-1689.jpg",
        "image_caption": "1689년에 그려진 뉴턴의 초상화",
        "image_source_text": "위키백과",
        "image_source_url": "https://www.wikipedia.org/", # General Wikipedia link
        "nationality": "영국",
        "fields": ["수학", "물리학", "천문학", "연금술", "자연철학", "기독교 신학", "경제학"],
        "major_achievements": ["만유인력의 법칙 발견", "미적분학 창시", "고전 역학의 기초 확립"],
        "qr_info_source": "유튜브" # Placeholder for QR code related info
    },
    {
        "name_korean": "마리 퀴리",
        "name_english": "Marie Curie",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Marie_Curie_c._1920s.jpg/440px-Marie_Curie_c._1920s.jpg",
        "image_caption": "마리 퀴리, 1920년대경",
        "image_source_text": "위키백과",
        "image_source_url": "https://www.wikipedia.org/",
        "nationality": "폴란드, 프랑스",
        "fields": ["물리학", "화학"],
        "major_achievements": ["방사능 연구", "폴로늄 및 라듐 발견", "노벨상 2회 수상 (물리학, 화학)"],
        "qr_info_source": "유튜브"
    },
    {
        "name_korean": "알베르트 아인슈타인",
        "name_english": "Albert Einstein",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Einstein_1921_by_F_Schmutzer_-_restoration.jpg/440px-Einstein_1921_by_F_Schmutzer_-_restoration.jpg",
        "image_caption": "아인슈타인, 1921년",
        "image_source_text": "위키백과",
        "image_source_url": "https://www.wikipedia.org/",
        "nationality": "독일, 미국",
        "fields": ["이론물리학"],
        "major_achievements": ["상대성이론 (특수, 일반)", "광전효과 규명 (노벨 물리학상)", "질량-에너지 등가원리 (E=mc²)"],
        "qr_info_source": "유튜브"
    },
    # Add more people here
]

# --- App Header ---
# Attempt to mimic the logo (using text as a placeholder)
# If you have the actual logo image, you can use st.image("path/to/your/logo.png")
# For example, if the logo is `logo.png` in the same directory as `app.py`:
# st.image("logo.png", width=150)
# Since I don't have the exact logo, I'll use text.
st.markdown("<h1 style='text-align: center; color: #0072C6;'>GREAT-PERSON</h1>", unsafe_allow_html=True)
st.markdown("---") # Horizontal line

# --- Search Bar ---
search_term = st.text_input("", placeholder="🔍 위인 이름을 검색하세요...")
st.markdown("---") # Horizontal line

# --- Display Logic ---
if search_term:
    results = [
        person for person in people_data
        if search_term.lower() in person["name_korean"].lower() or
           search_term.lower() in person["name_english"].lower()
    ]

    if not results:
        st.warning(f"'{search_term}'에 대한 검색 결과가 없습니다.")
    else:
        for person in results:
            st.markdown("##") # Add some vertical space

            # Main content area (two columns: image on left, info on right)
            col1, col2 = st.columns([2, 3]) # Adjust column widths as needed

            with col1:
                st.subheader(f"{person['name_korean']}")
                st.caption(f"{person['name_english']}")
                st.image(person["image_url"], caption=person["image_caption"])
                st.markdown(f"출처 : [{person['image_source_text']}]({person['image_source_url']})")

            with col2:
                st.markdown(f"**국적:** {person['nationality']}")
                st.markdown(f"**분야:** {', '.join(person['fields'])}")
                st.markdown(f"**주요 업적:**")
                for achievement in person['major_achievements']:
                    st.markdown(f"- {achievement}")

                # QR Code Section (Placeholder)
                # Generating actual QR codes would require a library like 'qrcode'
                # and then displaying it with st.image.
                # For now, we'll just replicate the look.
                st.markdown("##") # Add some space before QR
                st.markdown(
                    """
                    <div style="
                        background-color: #4A86E8; /* Blue similar to the image */
                        color: white;
                        padding: 10px;
                        text-align: center;
                        font-weight: bold;
                        border-radius: 5px;
                        width: 120px; /* Adjust width as needed */
                    ">
                        QR 코드
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.caption(f"출처 : {person['qr_info_source']}")
            st.markdown("---") # Separator between results
else:
    st.info("위대한 위인의 이름을 검색창에 입력하여 정보를 찾아보세요.")
    st.markdown("### 예시 위인:")
    # Display a few examples initially or when search is empty
    example_cols = st.columns(len(people_data[:3])) # Show up to 3 examples
    for i, person in enumerate(people_data[:3]):
        with example_cols[i]:
            st.markdown(f"**{person['name_korean']}**")
            st.image(person['image_url'], width=150)
            if st.button(f"{person['name_korean']} 정보 보기", key=f"example_{i}"):
                # This is a bit tricky without re-running with a search term.
                # A simpler approach for "click to search" would involve session state.
                # For now, this button is illustrative.
                st.info(f"'{person['name_korean']}'을(를) 검색창에 입력해보세요.")