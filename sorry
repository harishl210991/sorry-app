import streamlit as st
import random
from time import sleep

st.set_page_config(page_title="Sorry ❤️", page_icon="💔", layout="centered")

st.markdown("<h1 style='text-align:center; color:#ff4b4b;'>😔 I'm Really Sorry...</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Please forgive me, my love 💖</p>", unsafe_allow_html=True)

messages = [
    "Even if you press NO, my heart says YES to your forgiveness 💞",
    "System error: You cannot say no to this much cuteness 😢",
    "Forgiveness.exe has started running… please wait ⏳",
    "Warning ⚠️: Refusing forgiveness may cause excessive husband sadness.",
    "I already deleted my ego folder… can we start fresh? 🥺",
    "I made a mistake, but loving you wasn’t one of them 💌",
    "Click OK — and let’s order your favorite dessert 🍰",
]

placeholder = st.empty()

if "count" not in st.session_state:
    st.session_state.count = 0

with placeholder.container():
    st.write("Will you forgive me? 🙏")
    col1, col2 = st.columns(2)
    with col1:
        ok = st.button("❤️ OK")
    with col2:
        no = st.button("💔 No")

if ok or no:
    st.session_state.count += 1
    msg = random.choice(messages)
    with placeholder.container():
        st.markdown(f"<h3 style='text-align:center; color:#ff69b4;'>{msg}</h3>", unsafe_allow_html=True)
        sleep(1.5)
        st.experimental_rerun()

st.markdown("<br><br><center>Made with ❤️ for my favorite person.</center>", unsafe_allow_html=True)
