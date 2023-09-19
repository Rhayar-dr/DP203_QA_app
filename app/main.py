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

st.title("DP203 Exam")

# Initialize score and timer
score = 0
start_time = time.time()

for idx, q in enumerate(questions, 1):
    st.markdown(f"**Question {idx}**: {q['question']}", unsafe_allow_html=True)
    if 'image' in q:
        st.image(q['image'])
    answer = st.radio(f"Choices {idx}:", q['choices'])

    if st.button(f"Check Answer for Question {idx}"):
        if answer == q['answer']:
            score += 1  # increment score
            st.success(f"Correct! The answer is {q['answer']}.")
            st.info(f"Explanation: {q['explanation']}")
        else:
            st.error(f"Wrong answer. The correct answer is {q['answer']} and the explanation is: \n\n {q['explanation']}.")

end_time = time.time()
total_time_spent = end_time - start_time

# Display score and time after the loop
st.markdown(f"**Your Score**: {score}/{len(questions)}")
st.markdown(f"**Time Spent**: {int(total_time_spent // 60)} minutes and {int(total_time_spent % 60)} seconds")

# Donation Note
st.markdown("If you found this app helpful, consider making a donation to support development. Thank you! 🙏")
st.markdown("Bitcoin (BTC) Address: ₿ `bc1qkru3pwy9jhn2gsmet245ssd9xx5mlzcvpgczpy`")
st.markdown("Polygon Address (polygon network): 🔗 `0x5eBDB6031BeCa2A9a538A00477dC8049244e86fe`")
