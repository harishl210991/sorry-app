import streamlit as st
import random
import time
from datetime import datetime

# --- Page setup ---
st.set_page_config(page_title="Sorry ❤️", page_icon="💔", layout="centered")

st.markdown("<h1 style='text-align:center; color:#ff4b4b;'>🥺 I'm Really Sorry...</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Please forgive me, my love 💖</p>", unsafe_allow_html=True)

# --- Custom messages ---
messages = [
    "Even if you press NO, my heart says YES to your forgiveness 💞",
    "System error: A woman of this much beauty can exist you know (am telling the truth and not butter you up :P)",
    "Forgiveness.exe has started running… please wait ⏳",
    "Warning ⚠️: Refusing forgiveness may cause excessive husband sadness.",
    "I already deleted my ego folder… can we start fresh? 🥺",
    "I made a mistake, can I prove it with a biscoff cake 🍰",
    "Click OK - you might even get a kissi 😘",
    "Every ‘No’ you press adds +1 to my cuteness level, wanna test it? 😅",
    "I’ve filed a ‘Sorry Request’ to your heart... still pending approval 💌",
    "Forgiveness update available: install love v2.0 💞"
]

# --- Initialize state ---
if "count" not in st.session_state:
    st.session_state.count = 0

if "log" not in st.session_state:
    st.session_state.log = []

placeholder = st.empty()

# --- Main UI ---
with placeholder.container():
    st.write("Will you forgive me? 🙏")
    c1, c2 = st.columns(2)
    with c1:
        ok = st.button("❤️ OK")
    with c2:
        no = st.button("💔 No")

# --- Handle clicks ---
if ok or no:
    st.session_state.count += 1
    msg = random.choice(messages)

    if ok:
        st.session_state.log.append(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — She clicked YES ❤️"
        )
        st.balloons()
        st.toast("Yay! Processing infinite forgiveness loop… 😅", icon="🎉")
    else:
        st.session_state.log.append(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — She clicked NO 💔"
        )
        st.toast("Hmm… attempting another ultra-cute request…", icon="🥺")

    with placeholder.container():
        st.markdown(f"<h3 style='text-align:center; color:#ff69b4;'>{msg}</h3>", unsafe_allow_html=True)
        time.sleep(1.5)
    st.rerun()


# ----------------------
# 🔐 HIDDEN ADMIN PANEL
# ----------------------

st.markdown("---")

# A small discreet button  
admin_reveal = st.button("🔧 Admin")

if admin_reveal:
    st.markdown("### 🔐 Enter Admin Password")
    pwd = st.text_input("Password:", type="password")

    if pwd == "harishlove":  # <-- change password if you want
        st.success("Admin verified ✔")
        st.markdown("### 📜 Click Log (Private)")

        if len(st.session_state.log) == 0:
            st.info("No clicks yet 🤷‍♂️")
        else:
            for entry in reversed(st.session_state.log):
                st.write("•", entry)

    elif pwd:
        st.error("❌ Wrong password")

else:
    # Hide everything unless admin clicks the button
    st.caption("")

st.markdown("<br><center>Made with ❤️, cuteness & admin superpowers.</center>", unsafe_allow_html=True)
