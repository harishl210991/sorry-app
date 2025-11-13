import streamlit as st
import random
import time
from datetime import datetime
from zoneinfo import ZoneInfo   # For India timezone
import os

st.set_page_config(page_title="Sorry ❤️", page_icon="💔", layout="centered")

LOG_FILE = "click_log.txt"  # shared log across all devices

# -------------------------
# Helper functions for shared file-based log
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
# Messages
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
# Header
# -------------------------
st.markdown("<h1 style='text-align:center; color:#ff4b4b;'>🥺 I'm Really Sorry...</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Please forgive me my love ❤️</p>", unsafe_allow_html=True)

# -------------------------
# Ask for initials
# -------------------------
st.markdown("### 💛 Before we continue…")
initials = st.text_input("Enter your initials (like D/DK/DH/HD):")

if not initials:
    st.warning("Please enter your initials above before clicking anything ❤️")
else:
    initials = initials.strip().upper()

placeholder = st.empty()

# -------------------------
# Main buttons
# -------------------------
with placeholder.container():
    c1, c2 = st.columns(2)
    ok = c1.button("❤️ OK")
    no = c2.button("💔 No")

# -------------------------
# Button logic (writes initials + IST timestamp)
# -------------------------
if initials and (ok or no):
    # India timezone time
    now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S")

    if ok:
        append_log(f"• {initials} — {now} — YES ❤️")
        st.balloons()
    else:
        append_log(f"• {initials} — {now} — NO 💔")

    msg = random.choice(messages)

    with placeholder.container():
        st.markdown(
            f"<h3 style='text-align:center; color:#ff69b4;'>{msg}</h3>",
            unsafe_allow_html=True
        )
        time.sleep(1.2)
    st.rerun()

# -----------------------------------------------------------
# ❤️ Secret word section
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

        # Show image safely
        if os.path.exists("photo.jpg"):
            st.image("photo.jpg", use_container_width=True)
        else:
            st.warning("(Upload 'photo.jpg' to your repo to display the picture 😇)")
    else:
        st.error("Hmm… that's not the word 😅 Try again my love 💛")

# -----------------------------------------------------------
# 📜 Shared click log (visible everywhere)
# -----------------------------------------------------------
st.markdown("---")
st.subheader("📜 Click Log")

log_lines = read_log()

if not log_lines:
    st.info("No clicks recorded yet.")
else:
    for entry in reversed(log_lines):
        st.write(entry)

st.caption("Made with ❤️, initials, IST time, and honest apologies.")
