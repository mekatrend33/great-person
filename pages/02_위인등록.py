import streamlit as st
import pandas as pd
from datetime import datetime

# 세션 상태에 게시글 데이터프레임이 없다면 초기화
if 'posts' not in st.session_state:
    st.session_state.posts = pd.DataFrame(columns=['id', 'title', 'author', 'field', 'achievement', 'date'])

# 새로운 게시글 ID 생성
def get_new_id():
    if len(st.session_state.posts) == 0:
        return 1
    return int(st.session_state.posts['id'].max()) + 1

# 엑셀에서 위대한 인물 데이터 추가
def load_from_excel():
    try:
        df = pd.read_excel("person.xlsx")
        required_cols = ['이름', '국적', '분야', '주요업적']

        if not all(col in df.columns for col in required_cols):
            st.error("엑셀 파일에 다음 컬럼이 포함되어 있어야 합니다: 이름, 국적, 분야, 주요업적")
            return

        new_posts = []
        for _, row in df.iterrows():
            new_posts.append({
                'id': get_new_id(),
                'title': row['이름'],
                'author': row['국적'],
                'field': row['분야'],
                'achievement': row['주요업적'],
                'date': datetime.now().strftime('%Y-%m-%d %H:%M')
            })

        st.session_state.posts = pd.concat(
            [pd.DataFrame(new_posts), st.session_state.posts],
            ignore_index=True
        )

        st.success(f"{len(new_posts)}명의 인물이 엑셀에서 추가되었습니다!")

    except FileNotFoundError:
        st.error("person.xlsx 파일을 찾을 수 없습니다. 이 파일이 이 앱과 같은 폴더에 있는지 확인하세요.")
    except Exception as e:
        st.error(f"엑셀 불러오기 중 오류 발생: {e}")

# 위대한 인물 등록 폼
def write_post():
    st.header("📝 위대한 인물 등록")
    with st.form("post_form", clear_on_submit=True):
        title = st.text_input("이름")
        author = st.text_input("국적")
        field = st.text_input("분야")
        achievement = st.text_area("주요 업적")
        submitted = st.form_submit_button("작성하기")

        if submitted:
            if title and author and field and achievement:
                new_post = {
                    'id': get_new_id(),
                    'title': title,
                    'author': author,
                    'field': field,
                    'achievement': achievement,
                    'date': datetime.now().strftime('%Y-%m-%d %H:%M')
                }
                st.session_state.posts = pd.concat(
                    [pd.DataFrame([new_post]), st.session_state.posts],
                    ignore_index=True
                )
                st.success("게시글이 등록되었습니다!")
            else:
                st.warning("모든 항목을 입력해주세요.")

# 게시글 목록 보기
def show_board():
    st.header("📋 위대한 인물 목록")
    if len(st.session_state.posts) == 0:
        st.info("게시글이 없습니다.")
    else:
        for _, row in st.session_state.posts.iterrows():
            if st.button(f"{row['title']} - {row['author']} ({row['date']})", key=row['id']):
                st.session_state.view_post_id = row['id']

# 게시글 상세 보기
def view_post():
    post_id = st.session_state.get('view_post_id')
    if post_id:
        post = st.session_state.posts[st.session_state.posts['id'] == post_id].iloc[0]
        st.header(f"📄 {post['title']}")
        st.write(f"**국적:** {post['author']}  |  **작성일:** {post['date']}")
        st.write(f"**분야:** {post['field']}")
        st.markdown("---")
        st.subheader("🏆 주요 업적")
        st.write(post['achievement'])
        if st.button("🔙 돌아가기"):
            del st.session_state.view_post_id

# 메인 앱 실행 흐름
def main():
    st.title("🌟 위대한 인물 게시판")

    menu = st.sidebar.radio("메뉴 선택", ['게시판 보기', '게시글 작성'])

    if st.sidebar.button("📂 엑셀에서 인물 추가"):
        load_from_excel()

    if 'view_post_id' in st.session_state:
        view_post()
    elif menu == '게시판 보기':
        show_board()
    elif menu == '게시글 작성':
        write_post()

if __name__ == "__main__":
    main()
