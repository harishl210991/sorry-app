import streamlit as st
import random
import time
from datetime import datetime

st.set_page_config(page_title="Sorry ❤️", page_icon="💔", layout="centered")

# -------------------------
# INIT SESSION STATE
# -------------------------
if "log" not in st.session_state:
    st.session_state.log = []

# -------------------------
# MESSAGES
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
# HEADER
# -------------------------
st.markdown("<h1 style='text-align:center; color:#ff4b4b;'>🥺 I'm Really Sorry...</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Please forgive me my love ❤️</p>", unsafe_allow_html=True)

placeholder = st.empty()

# -------------------------
# MAIN BUTTONS
# -------------------------
with placeholder.container():
    c1, c2 = st.columns(2)
    ok = c1.button("❤️ OK")
    no = c2.button("💔 No")

# -------------------------
# BUTTON LOGIC
# -------------------------
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

# -----------------------------------------------------------
# ❤️ SECRET WORD CHECK
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

        # Show image
        st.image("photo.jpg", use_container_width=True)  
        # ↑ Upload photo.jpg in your repo

    else:
        st.error("Hmm… that's not the word 😅 Try again my love 💛")

# -----------------------------------------------------------
# 📜 ALWAYS SHOW LOG (No admin protection)
# -----------------------------------------------------------
st.markdown("---")
st.subheader("📜 Click Log (for me to see)")

if len(st.session_state.log) == 0:
    st.info("No clicks recorded yet.")
else:
    for entry in reversed(st.session_state.log):
        st.write("•", entry)

st.caption("Made with ❤️ & infinite apologies.")
