import streamlit as st
import random;
st.set_page_config(page_title="楽ちん献立アプリ",layout="wide")
st.title("🍽️ 楽ちん献立アプリ")

# 表示する料理のリスト
menus = [
    "堤煮込みハンバーグ",
    "包み焼ハンバーグ",
    "包み煮込みハンバーグ",
    "タピオカパン",
    "Mac",
    "エスカルゴ",
    "水炊き",
    "シュールストレミング",
    "マーマイト",
    "サルミアッキ",
    "湯葉",
    "クリスマスケーキ",
    "一蘭",
    "堤焼きハンバーグ"
]
st.write("ボタンを押すと、今日の献立をランダムで1つ表示します！")

if st.button("🍳 献立を決める"):
    choice = random.choice(menus)

    st.success(f"今日の献立は…… **{choice}** です！")
    st.write("おいしく食べてね💝")
