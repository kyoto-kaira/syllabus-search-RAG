import streamlit as st
from streamlit_pills import pills
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Iterator

from search import search_syllabus

load_dotenv()

st.set_page_config(page_title="京都大学シラバス検索", page_icon="📚")
st.title("京都大学シラバス検索")

# 検索クエリ
search_query = st.text_input(
    label="どんな講義をお探しですか？",
    max_chars=512,
    placeholder="例: 機械学習の基礎を学べる講義",
)


# 曜時限
options_weekdays = [
    f"{weekday}{i}" for weekday in ["月", "火", "水", "木", "金"] for i in range(1, 6)
] + ["集中"]
selected_weekdays = st.multiselect(
    label="曜時限",
    options=options_weekdays,
)
selected_weekdays = options_weekdays if not selected_weekdays else selected_weekdays

# 評価基準
options_eval_criteria = [
    "平常点",
    "課題",
    "発表",
    "討論",
    "小レポート",
    "小テスト",
    "期末レポート",
    "期末試験",
]
eval_criteria = st.multiselect(
    label="評価基準",
    options=options_eval_criteria,
)
eval_criteria = options_eval_criteria if not eval_criteria else eval_criteria

# 学部
options_department = [
    "文学部",
    "教育学部",
    "法学部",
    "経済学部",
    "理学部",
    "医学部",
    "工学部",
    "農学部",
    "薬学部",
    "総合人間学部",
    "情報学研究科",
    "生命科学研究科",
    "先端研究科",
    "国際高等研究所",
    "その他",
]
department = st.multiselect(
    label="学部",
    options=options_department,
)
department = options_department if not department else department

# モード
diversity = pills(
    label="モード",
    options=["多様性重視", "厳密性重視"],
)


def get_response(user_query: str) -> Iterator[str]:
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "与えられる文書をわかりやすく整形してください。"),
            ("human", user_query),
        ]
    )
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    chain = prompt | llm | StrOutputParser()

    return chain.stream({"": ""})


# 検索
if st.button("検索"):
    user_query = f"""
    - 検索クエリ: {search_query}
    - モード: {diversity}
    - 曜時限: {selected_weekdays}
    - 評価基準: {eval_criteria}
    - 学部: {department}
    """
    results = search_syllabus(user_query)
    for i, result in enumerate(results, start=1):
        result_str = ""
        for key, value in result.items():
            result_str += f"- {key}: {value}\n"
        with st.expander(f"検索結果{i}", expanded=True):
            with st.spinner("シラバス要約生成中..."):
                response = st.write_stream(get_response(str(result_str)))
