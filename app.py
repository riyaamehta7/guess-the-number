import streamlit as st
import random

st.set_page_config(page_title="AI Guess the Number", page_icon="🎯")

st.title("🎯 AI Guess the Number Game")
st.write("Think of a number between 1 and 100, and I'll try to guess it!")

# Initialize session variables
if "low" not in st.session_state:
    st.session_state.low = 1
if "high" not in st.session_state:
    st.session_state.high = 100
if "guess" not in st.session_state:
    st.session_state.guess = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

st.write(f"My guess is **{st.session_state.guess}** 🎲")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Too High 📉"):
        st.session_state.high = st.session_state.guess - 1
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
        st.session_state.attempts += 1
        st.rerun()
with col2:
    if st.button("Too Low 📈"):
        st.session_state.low = st.session_state.guess + 1
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
        st.session_state.attempts += 1
        st.rerun()
with col3:
    if st.button("Correct ✅"):
        st.success(f"Yay! I guessed your number in {st.session_state.attempts + 1} tries 🎉")
        if st.button("Play Again 🔄"):
            for key in ["low", "high", "guess", "attempts"]:
                del st.session_state[key]
            st.rerun()
