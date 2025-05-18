import streamlit as st

st.set_page_config(
    page_title="위대한 위인인",
    page_icon="./images/ding.png"
)

st.title("hello streamlit!")
st.markdown("**위대한 위인**을 하나씩 추가해 보세요!")

type_emoji_dict = {
    "수학자자": "⚪",
    "과학자자": "✊",
    "기술자자": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}

person = {
    "name": "뉴턴",
    "types": ["과학자", "수학자"],
    "image_url": "https://i.namu.wiki/i/0KC24R7hvHoRQFaki5E9aJJc4h4NGh0szPAL9G7XDNPc6RiIdf7qCGfJkjrv3usF-ci2LLqQgxiFr1n7WTcbfYFKpWDnSyeVI8uUDBWwZ7-0V8hkd0VTPcms-NKxQXR3FEjJfQD8aJ40UW48XI8Qig.webp"
}