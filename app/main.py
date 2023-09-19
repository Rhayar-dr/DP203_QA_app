import streamlit as st
from data import questions
import time

def custom_css(font_size):
    st.markdown(
        f"""
        <style>
            .css-1y0tads {{
                font-size: {font_size} !important;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

custom_css("18px")

st.title("DP203 Test")

# Donation Note at the top
st.markdown("If you found this app helpful, consider making a donation to support development. Thank you! 🙏")
st.markdown("Bitcoin (BTC) Address: 🔗 `bc1qkru3pwy9jhn2gsmet245ssd9xx5mlzcvpgczpy`")
st.markdown("Polygon Address: 🔗 `0x5eBDB6031BeCa2A9a538A00477dC8049244e86fe`")

# Initialize score and timer
correct_answers = 0
incorrect_answers = 0
start_time = None
end_time = None

# Timer Buttons & Display at the top
if st.button('Start'):
    start_time = time.time()
    
if st.button('Stop'):
    if start_time:
        end_time = time.time()

if st.button('Reset'):
    start_time = None
    end_time = None

if start_time:
    elapsed_time = time.time() - start_time
else:
    elapsed_time = 0

if end_time:
    elapsed_time = end_time - start_time

st.markdown(f"**Timer**: {int(elapsed_time // 60)} minutes and {int(elapsed_time % 60)} seconds")

for idx, q in enumerate(questions, 1):
    st.markdown(f"**Question {idx}**: {q['question']}", unsafe_allow_html=True)
    if 'image' in q:
        st.image(q['image'])
    answer = st.radio(f"Choices {idx}:", q['choices'])

    if st.button(f"Check Answer for Question {idx}"):
        if answer == q['answer']:
            correct_answers += 1
            st.success(f"Correct! The answer is {q['answer']}.")
            st.info(f"Explanation: {q['explanation']}")
        else:
            incorrect_answers += 1
            st.error(f"Wrong answer. The correct answer is {q['answer']} and the explanation is: \n\n {q['explanation']}.")

# Display score and timer at the bottom
st.markdown(f"**Correct Answers**: {correct_answers}")
st.markdown(f"**Incorrect Answers**: {incorrect_answers}")
st.markdown(f"**Timer**: {int(elapsed_time // 60)} minutes and {int(elapsed_time % 60)} seconds")

# Donation Note at the bottom
st.markdown("If you found this app helpful, consider making a donation to support development. Thank you! 🙏")
st.markdown("Bitcoin (BTC) Address: 🔗 `bc1qkru3pwy9jhn2gsmet245ssd9xx5mlzcvpgczpy`")
st.markdown("Polygon Address: 🔗 `0x5eBDB6031BeCa2A9a538A00477dC8049244e86fe`")
