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

if "admin_mode" not in st.session_state:
    st.session_state.admin_mode = False  # stays True after verification


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

st.markdown("<h1 style='text-align:center; color:#ff4b4b;'>🥺 I'm Really Sorry...</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Please forgive me, my love 💖</p>", unsafe_allow_html=True)

placeholder = st.empty()


# -------------------------
# MAIN UI
# -------------------------
with placeholder.container():
    st.write("Will you forgive me? 🙏")
    c1, c2 = st.columns(2)
    ok = c1.button("❤️ OK")
    no = c2.button("💔 No")


# -------------------------
# BUTTON LOGIC
# -------------------------
if ok or no:
    msg = random.choice(messages)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if ok:
        st.session_state.log.append(f"{now} — She clicked YES ❤️")
        st.balloons()
    else:
        st.session_state.log.append(f"{now} — She clicked NO 💔")

    with placeholder.container():
        st.markdown(f"<h3 style='text-align:center; color:#ff69b4;'>{msg}</h3>", unsafe_allow_html=True)
        time.sleep(1.2)
    st.rerun()


# -------------------------
# ADMIN SYSTEM (MOBILE SAFE)
# -------------------------

st.markdown("---")
st.subheader("🔧 Admin Access")

# Already authenticated → immediately show logs
if st.session_state.admin_mode:

    st.success("Admin Mode Active ✔")
    st.markdown("### 📜 Click Log")

    if len(st.session_state.log) == 0:
        st.info("No clicks yet.")
    else:
        # Always show logs, no collapsing
        for entry in reversed(st.session_state.log):
            st.write("•", entry)

else:
    # If NOT authenticated, show password box
    pwd = st.text_input("Enter admin password:", type="password")

    if pwd == "harishlove":       # <-- change to your desired password
        st.session_state.admin_mode = True
        st.rerun()
    elif pwd != "":
        st.error("Wrong password ❌")

st.caption("Made with ❤️ & admin superpowers.")
