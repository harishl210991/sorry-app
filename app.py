import streamlit as st
import random
import time
from datetime import datetime

st.set_page_config(page_title="Sorry ❤️", page_icon="💔", layout="centered")

# Init log
if "log" not in st.session_state:
    st.session_state.log = []

# Apology messages
messages = [
    "Even if you press NO, my heart says YES to your forgiveness 💞",
    "System error: A woman of this much beauty can exist you know 😍 (not buttering you up :P)",
    "Forgiveness.exe has started running… please wait ⏳",
    "Warning ⚠️: Refusing forgiveness may cause excessive husband sadness.",
    "I already deleted my ego folder… can we start fresh? 🥺",
    "I made a mistake, can I prove it with a biscoff cake 🍰",
    "Click OK - you might even get a kissi 😘",
]

st.title("🥺 I'm Really Sorry...")
st.write("Please forgive me ❤️")

placeholder = st.empty()

# Main buttons
with placeholder.container():
    col1, col2 = st.columns(2)
    ok = col1.button("❤️ OK")
    no = col2.button("💔 No")

# Button logic
if ok or no:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if ok:
        st.session_state.log.append(f"{now} — YES clicked ❤️")
        st.balloons()
    else:
        st.session_state.log.append(f"{now} — NO clicked 💔")

    msg = random.choice(messages)
    with placeholder.container():
        st.markdown(f"<h3 style='text-align:center; color:#ff69b4;'>{msg}</h3>", unsafe_allow_html=True)
        time.sleep(1.2)

    st.rerun()

# FORCE SHOW THE LOG ALWAYS
st.markdown("---")
st.subheader("📜 DEBUG LOG (Should ALWAYS be visible)")

if len(st.session_state.log) == 0:
    st.write("No clicks recorded yet.")
else:
    for entry in reversed(st.session_state.log):
        st.write("•", entry)
