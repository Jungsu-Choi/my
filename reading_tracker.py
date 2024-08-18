import streamlit as st

# 책 목록을 세션 상태에 저장
if 'books' not in st.session_state:
    st.session_state.books = []

# 앱 제목
st.title("독서 진행 상황 기록 앱")

# 책 추가 기능
st.subheader("책 추가")
new_book = st.text_input("책 이름을 입력하세요:")
if st.button("책 추가"):
    if new_book:
        # 새로운 책을 추가, 초기 상태는 '읽지 않음'으로 설정
        st.session_state.books.append({"title": new_book, "status": "읽지 않음"})
        st.success(f"'{new_book}' 이(가) 추가되었습니다.")
    else:
        st.warning("책 이름을 입력해주세요.")

# 책 상태 업데이트 기능
st.subheader("책 상태 업데이트")
if st.session_state.books:
    book_to_update = st.selectbox("상태를 업데이트할 책을 선택하세요:", [book['title'] for book in st.session_state.books])
    status = st.radio("읽음 여부를 선택하세요:", ("읽음", "읽지 않음"))

    if st.button("상태 업데이트"):
        for book in st.session_state.books:
            if book['title'] == book_to_update:
                book['status'] = status
                st.success(f"'{book_to_update}' 의 상태가 '{status}' 으로 업데이트되었습니다.")
                break
else:
    st.write("현재 추가된 책이 없습니다.")

# 책 삭제 기능
st.subheader("책 삭제")
if st.session_state.books:
    book_to_delete = st.selectbox("삭제할 책을 선택하세요:", [book['title'] for book in st.session_state.books])
    if st.button("책 삭제"):
        st.session_state.books = [book for book in st.session_state.books if book['title'] != book_to_delete]
        st.success(f"'{book_to_delete}' 이(가) 삭제되었습니다.")
else:
    st.write("삭제할 책이 없습니다.")

# 책 목록 표시
st.subheader("현재 책 목록")
if st.session_state.books:
    for book in st.session_state.books:
        st.write(f"{book['title']} - 상태: {book['status']}")
else:
    st.write("현재 추가된 책이 없습니다.")