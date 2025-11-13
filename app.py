import streamlit as st
import random
import time
from datetime import datetime

st.set_page_config(page_title="Sorry ❤️", page_icon="💔", layout="centered")

# -------------------------
# INIT SESSION STATES
# -------------------------
if "log" not in st.session_state:
    st.session_state.log = []

if "admin_mode" not in st.session_state:
    st.session_state.admin_mode = False  # True after correct password


# -------------------------
# MAIN UI
# -------------------------
st.title("🥺 I'm Really Sorry...")
st.write("Please forgive me my love ❤️")

messages = [
    "Even if you press NO, my heart says YES to your forgiveness 💞",
    "System error: A woman of this much beauty can exist you know 😍 (not buttering you up :P)",
    "Forgiveness.exe has started running… please wait ⏳",
    "Warning ⚠️: Refusing forgiveness may cause excessive husband sadness.",
    "I already deleted my ego folder… can we start fresh? 🥺",
    "I made a mistake, can I prove it with a biscoff cake 🍰",
    "Click OK - you might even get a kissi 😘",
]

placeholder = st.empty()

with placeholder.container():
    c1, c2 = st.columns(2)
    ok = c1.button("❤️ OK")
    no = c2.button("💔 No")


# -------------------------
# BUTTON HANDLING
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


# -------------------------
# ADMIN PANEL (SAFE + SIMPLE)
# -------------------------
st.markdown("---")
st.subheader("🔧 Admin Access")

# If admin already authenticated, show log directly
if st.session_state.admin_mode:

    st.success("Admin Mode Active ✔")
    st.markdown("### 📜 Click Log (Private)")

    if len(st.session_state.log) == 0:
        st.info("No clicks yet.")
    else:
        for entry in reversed(st.session_state.log):
            st.write("•", entry)

else:
    # Ask for password
    pwd = st.text_input("Enter Admin Password:", type="password")

    if pwd == "harishlove":  # <<--------- change password here
        st.session_state.admin_mode = True
        st.rerun()  # refresh to show log
    elif pwd != "":
        st.error("Wrong password ❌")

st.caption("Made with ❤️ & admin superpowers.")
