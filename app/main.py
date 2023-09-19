import streamlit as st
from data import questions
import time

def custom_css(font_size, additional_styles=""):
    st.markdown(
        f"""
        <style>
            .css-1y0tads {{
                font-size: {font_size} !important;
            }}
            {additional_styles}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Custom CSS for sticky container
custom_css("18px", ".sticky-container { position: sticky; top: 0; z-index: 100; background-color: white; padding: 1rem; border-bottom: 1px solid #f0f0f0; }")

st.title("DP203 Exam")

# Donation Note at the top
st.markdown("If you found this app helpful, consider making a donation to support development. Thank you! 🙏")
st.markdown("Bitcoin (BTC) Address: 🔗 `bc1qkru3pwy9jhn2gsmet245ssd9xx5mlzcvpgczpy`")
st.markdown("Polygon Address: 🔗 `0x5eBDB6031BeCa2A9a538A00477dC8049244e86fe`")

# Initialize or reset session state variables
if 'correct_answers' not in st.session_state:
    st.session_state.correct_answers = 0
if 'incorrect_answers' not in st.session_state:
    st.session_state.incorrect_answers = 0
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'end_time' not in st.session_state:
    st.session_state.end_time = None
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False

with st.beta_container():
    with st.beta_expander("Timer and Score", expanded=True):
        # Timer Buttons & Display at the top
        if st.button('Start'):
            st.session_state.start_time = time.time()
            st.session_state.timer_running = True

        if st.button('Stop'):
            st.session_state.end_time = time.time()
            st.session_state.timer_running = False

        if st.button('Reset'):
            st.session_state.start_time = None
            st.session_state.end_time = None
            st.session_state.correct_answers = 0
            st.session_state.incorrect_answers = 0
            st.session_state.timer_running = False

        if st.session_state.start_time:
            elapsed_time = time.time() - st.session_state.start_time
        else:
            elapsed_time = 0

        if st.session_state.end_time:
            elapsed_time = st.session_state.end_time - st.session_state.start_time

        st.markdown(f"**Timer**: {int(elapsed_time // 60)} minutes and {int(elapsed_time % 60)} seconds")
        st.markdown(f"**Correct Answers**: {st.session_state.correct_answers}")
        st.markdown(f"**Incorrect Answers**: {st.session_state.incorrect_answers}")

        if st.session_state.timer_running:
            st.markdown('<meta http-equiv="refresh" content="1">', unsafe_allow_html=True)

for idx, q in enumerate(questions, 1):
    st.markdown(f"**Question {idx}**: {q['question']}", unsafe_allow_html=True)
    if 'image' in q:
        st.image(q['image'])
    answer = st.radio(f"Choices {idx}:", q['choices'])

    if st.button(f"Check Answer for Question {idx}"):
        if answer == q['answer']:
            st.session_state.correct_answers += 1
            st.success(f"Correct! The answer is {q['answer']}.")
            st.info(f"Explanation: {q['explanation']}")
        else:
            st.session_state.incorrect_answers += 1
            st.error(f"Wrong answer. The correct answer is {q['answer']} and the explanation is: \n\n {q['explanation']}.")

# Donation Note at the bottom
st.markdown("If you found this app helpful, consider making a donation to support development. Thank you! 🙏")
st.markdown("Bitcoin (BTC) Address: 🔗 `bc1qkru3pwy9jhn2gsmet245ssd9xx5mlzcvpgczpy`")
st.markdown("Polygon Address: 🔗 `0x5eBDB6031BeCa2A9a538A00477dC8049244e86fe`")
