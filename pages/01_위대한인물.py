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
        "nationality": "영국",
        "fields": ["수학", "물리학", "천문학", "연금술", "자연철학", "기독교 신학", "경제학"],
        "major_achievements": ["만유인력의 법칙 발견", "미적분학 창시", "고전 역학의 기초 확립"],
        "qr_info_source": "유튜브 EBS", # Placeholder for QR code related info
        "qr_image": "./images/newton.png"  # QR 이미지 경로 추가
    },
    {
        "name_korean": "마리 퀴리",
        "name_english": "Marie Curie",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Marie_Curie_c._1920s.jpg/440px-Marie_Curie_c._1920s.jpg",
        "image_caption": "마리 퀴리, 1920년대경",
        "image_source_text": "위키백과",
        "nationality": "폴란드, 프랑스",
        "fields": ["물리학", "화학"],
        "major_achievements": ["방사능 연구", "폴로늄 및 라듐 발견", "노벨상 2회 수상 (물리학, 화학)"],
        "qr_info_source": "유튜브",
        "qr_image": "./images/curie.png"  # QR 이미지 경로 추가
    },
    {
        "name_korean": "알베르트 아인슈타인",
        "name_english": "Albert Einstein",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Einstein_1921_by_F_Schmutzer_-_restoration.jpg/440px-Einstein_1921_by_F_Schmutzer_-_restoration.jpg",
        "image_caption": "아인슈타인, 1921년",
        "image_source_text": "위키백과",
        "nationality": "독일, 미국",
        "fields": ["이론물리학"],
        "major_achievements": ["상대성이론 (특수, 일반)", "광전효과 규명 (노벨 물리학상)", "질량-에너지 등가원리 (E=mc²)"],
        "qr_info_source": "유튜브",
        "qr_image": "./images/einstein.png"  # QR 이미지 경로 추가
    },
    {
        "name_korean": "스티브 잡스",
        "name_english": "Steve Jobs",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Steve_Jobs_Headshot_2010-CROP2.jpg/440px-Steve_Jobs_Headshot_2010-CROP2.jpg",
        "image_caption": "스티브 잡스, 2010년",
        "image_source_text": "위키백과",
        "nationality": "미국",
        "fields": ["기업가", "혁신가"],
        "major_achievements": ["애플 공동 창립", "iPhone, iPad 등 혁신적 제품 개발", "디지털 콘텐츠 산업 혁신", "stay hungry stay foolish"],
        "qr_info_source": "유튜브",
        "qr_image": "./images/jobs.png"  # QR 이미지 경로 추가
    },
    {
        "name_korean": "니콜라 테슬라",
        "name_english": "Nikola Tesla",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/N.Tesla.JPG/440px-N.Tesla.JPG",
        "image_caption": "니콜라 테슬라",
        "image_source_text": "위키백과",
        "nationality": "세르비아, 미국",
        "fields": ["전기공학", "기계공학", "물리학"],
        "major_achievements": ["교류 전력 시스템 개발", "무선 통신의 기초 확립", "테슬라 코일 발명"],
        "qr_info_source": "유튜브",
        "qr_image": "./images/tesla.png"  # QR 이미지 경로 추가
    },
    {
        "name_korean": "토머스 에디슨",
        "name_english": "Thomas Edison",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Thomas_Edison2.jpg/440px-Thomas_Edison2.jpg",
        "image_caption": "토머스 에디슨",
        "image_source_text": "위키백과",
        "nationality": "미국",
        "fields": ["발명가", "사업가"],
        "major_achievements": ["전구의 실용화", "축음기 발명", "영화 산업의 기반 구축"],
        "qr_info_source": "유튜브",
        "qr_image": "./images/edison.png"  # QR 이미지 경로 추가
    },
    # Add more people here
]

# --- App Header ---
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
                if 'image_source_url' in person:
                    st.markdown(f"출처 : [{person['image_source_text']}]({person['image_source_url']})")
                else:
                    st.markdown(f"출처 : {person['image_source_text']}")
            with col2:
                st.markdown(f"**국적:** {person['nationality']}")
                st.markdown(f"**분야:** {', '.join(person['fields'])}")
                st.markdown(f"**주요 업적:**")
                for achievement in person['major_achievements']:
                    st.markdown(f"- {achievement}")

                st.markdown("##") 
                # st.markdown(
                #    """
                    # <div style="
                    #    background-color: #4A86E8;
                    #    color: white;
                    #    padding: 10px;
                    #   text-align: center;
                    #    font-weight: bold;
                    #    border-radius: 5px;
                    #    width: 120px; 
                    #">
                    #    EBS 교육 방송
                    # </div>
                    # """,
                    # unsafe_allow_html=True
                # )
                # st.caption(f"출처 : {person['qr_info_source']}")
                if person.get("qr_image"):
                   st.image(person["qr_image"], caption="유튜브", width=150)
            st.markdown("---") 
else:
    st.info("위대한 위인의 이름을 검색창에 입력하여 정보를 찾아보세요.")
    st.markdown("### 예시 위인:")
    
    example_persons_list = people_data[:4] 
    
    if example_persons_list: 
        example_cols = st.columns(len(example_persons_list))
        for i, person in enumerate(example_persons_list):
            with example_cols[i]:
                # 한글 이름: 왼쪽 정렬, 굵게, 이미지와의 간격 조절
                st.markdown(
                    f"""<p style="font-weight: bold; text-align: center; margin-bottom: 8px; font-size: 1em; min-height: 2.5em;">{person['name_korean']}</p>""",
                    unsafe_allow_html=True
                )
                
                # 이미지와 캡션: 가운데 정렬된 div 내에 배치
                st.markdown(
                    f"""
                    <div style="text-align: center;">
                        <img src="{person['image_url']}" alt="{person['name_korean']}" 
                             style="height: 250px; 
                                    width: auto; 
                                    max-width: 100%; 
                                    object-fit: cover; 
                                    border-radius: 5px; 
                                    margin-bottom: 8px;">
                        <br> 
                        <small>{person['image_caption']}</small>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    else:
        st.caption("예시 위인 데이터가 없습니다.")