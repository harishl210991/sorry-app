import streamlit as st
import random
import time
from datetime import datetime

st.set_page_config(page_title="Sorry ❤️", page_icon="💔", layout="centered")

st.markdown("<h1 style='text-align:center; color:#ff4b4b;'>🥺 I'm Really Sorry...</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Please forgive me, my love 💖</p>", unsafe_allow_html=True)

# --- Messages ---
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
# INIT SESSION STATES
# -------------------------
if "log" not in st.session_state:
    st.session_state.log = []

if "admin_mode" not in st.session_state:
    st.session_state.admin_mode = False  # stays TRUE after login

# --- UI ---
placeholder = st.empty()

with placeholder.container():
    st.write("Will you forgive me? 🙏")
    c1, c2 = st.columns(2)
    with c1:
        ok = st.button("❤️ OK")
    with c2:
        no = st.button("💔 No")


# -------------------------
# BUTTON LOGIC
# -------------------------
if ok or no:
    msg = random.choice(messages)

    if ok:
        st.session_state.log.append(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — She clicked YES ❤️"
        )
        st.balloons()
        st.toast("Yay! Infinite forgiveness loop activated 😅", icon="🎉")
    else:
        st.session_state.log.append(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — She clicked NO 💔"
        )
        st.toast("Hmm… trying again with extra cuteness…", icon="🥺")

    with placeholder.container():
        st.markdown(
            f"<h3 style='text-align:center; color:#ff69b4;'>{msg}</h3>",
            unsafe_allow_html=True
        )
        time.sleep(1)
    st.rerun()


# -------------------------
# ADMIN PANEL (RELIABLE VERSION)
# -------------------------
st.markdown("---")
st.subheader("🔧 Admin Access")

# If admin already verified → show log directly
if st.session_state.admin_mode:

    st.success("Admin Mode Active ✔")
    st.markdown("### 📜 Click Log")

    if len(st.session_state.log) == 0:
        st.info("No clicks recorded yet.")
    else:
        for entry in reversed(st.session_state.log):
            st.write("•", entry)

else:
    # Ask for password only if admin NOT in session
    pwd = st.text_input("Enter Admin Password:", type="password")

    if pwd == "harishlove":
        st.session_state.admin_mode = True
        st.rerun()
    elif pwd != "":
        st.error("Wrong password ❌")

st.caption("Made with ❤️ & admin superpowers.")
