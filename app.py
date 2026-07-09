import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="축구 승무패 맞추기 게임",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_html_app():
    # 2. 파일 경로 설정 (htmls/index.html)
    html_file_path = Path(__file__).resolve().parent / "htmls" / "index.html"
    
    # 3. HTML 파일 존재 여부 확인 및 읽기
    if html_file_path.exists():
        try:
            with open(html_file_path, "r", encoding="utf-8") as f:
                html_content = f.read()
            return html_content
        except Exception as e:
            st.error(f"⚠️ HTML 파일을 읽는 중 오류가 발생했습니다: {e}")
            return None
    else:
        st.error(
            "⚠️ 필수 웹앱 파일(`htmls/index.html`)을 찾을 수 없습니다.\n\n"
            "**해당 경로에 파일이 올바르게 위치해 있는지 확인해 주세요.**\n"
            f"- 예상 경로: `{html_file_path}`"
        )
        return None

def main():
    html_src = load_html_app()
    
    if html_src:
        # 4. Streamlit 컴포넌트를 통해 HTML 앱 렌더링
        # 고등학생 사용자들이 쾌적하게 이용할 수 있도록 넓은 높이와 스크롤을 제공합니다.
        components.html(html_src, height=850, scrolling=True)

if __name__ == "__main__":
    main()
