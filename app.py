import streamlit as st
import random
import time
from datetime import datetime
import os

st.set_page_config(page_title="Sorry ❤️", page_icon="💔", layout="centered")

LOG_FILE = "click_log.txt"  # shared log file

# -------------------------
# helper functions for shared log
# -------------------------
def append_log(entry: str):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

def read_log():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines

# -------------------------
# messages
# -------------------------
messages = [
    "Even if you press NO, my heart says YES to your forgiveness 💞",
    "System error: A woman of this much beauty can exist you know 😍 (not buttering you up :P)",
    "Forgiveness.exe has started running… please wait ⏳",
    "Warning ⚠️: Refusing forgiveness may cause excessive husband sadness.",
    "I already deleted my ego folder… can we start fresh? 🥺",
    "I made a mistake, can I prove it with a biscoff cake 🍰",
    "Click OK - you might even get a kissi 😘",
]

# -------------------------
# header
# -------------------------
st.markdown("<h1 style='text-align:center; color:#ff4b4b;'>🥺 I'm Really Sorry...</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Please forgive me my love ❤️</p>", unsafe_allow_html=True)

placeholder = st.empty()

# -------------------------
# main buttons
# -------------------------
with placeholder.container():
    c1, c2 = st.columns(2)
    ok = c1.button("❤️ OK")
    no = c2.button("💔 No")

# -------------------------
# button logic (writes to shared file)
# -------------------------
if ok or no:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if ok:
        append_log(f"{now} — YES clicked ❤️")
        st.balloons()
    else:
        append_log(f"{now} — NO clicked 💔")

    msg = random.choice(messages)

    with placeholder.container():
        st.markdown(
            f"<h3 style='text-align:center; color:#ff69b4;'>{msg}</h3>",
            unsafe_allow_html=True
        )
        time.sleep(1.2)
    st.rerun()

# -----------------------------------------------------------
# ❤️ secret word section
# -----------------------------------------------------------
st.markdown("---")
st.subheader("💗 A tiny question just for you...")

secret_input = st.text_input("Enter the word/name only you and I know 😘:")

SECRET_WORD = "Iniya"  # <<---- change this to your real secret word

if secret_input:
    if secret_input.strip().lower() == SECRET_WORD.lower():
        st.success("💖 That's the one! 💖")
        st.markdown(
            "<h3 style='text-align:center; color:#ff1493;'>I love you the most in the entire world ❤️</h3>",
            unsafe_allow_html=True
        )
        # safe image handling
        if os.path.exists("photo.jpg"):
            st.image("photo.jpg", use_container_width=True)
        else:
            st.warning("(Psst… upload photo.jpg to the repo so I can show our picture 😇)")
    else:
        st.error("Hmm… that's not the word 😅 Try again my love 💛")

# -----------------------------------------------------------
# 📜 shared click log (visible on all devices)
# -----------------------------------------------------------
st.markdown("---")
st.subheader("📜 Click Log")

log_lines = read_log()
if not log_lines:
    st.info("No clicks recorded yet.")
else:
    for entry in reversed(log_lines):
        st.write("•", entry)

st.caption("Made with ❤️, infinite retries, and shared logs.")
