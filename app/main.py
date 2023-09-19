import streamlit as st
from data import questions
import plotly.graph_objects as go

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

# Donation Note at the top
st.markdown("If you found this app helpful, consider making a donation to support development. Thank you! 🙏")
st.markdown("Bitcoin (BTC) Address: 🔗 `bc1qkru3pwy9jhn2gsmet245ssd9xx5mlzcvpgczpy`")
st.markdown("Polygon Address: 🔗 `0x5eBDB6031BeCa2A9a538A00477dC8049244e86fe`")

# Initialize or reset session state variables
if 'correct_answers' not in st.session_state:
    st.session_state.correct_answers = 0
if 'incorrect_answers' not in st.session_state:
    st.session_state.incorrect_answers = 0

# Display score statically on the top
st.markdown(f"**Score**: {st.session_state.correct_answers} Correct, {st.session_state.incorrect_answers} Incorrect")

if st.button("Reset Score"):
    st.session_state.correct_answers = 0
    st.session_state.incorrect_answers = 0

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

if st.button("End Test"):
    labels = ['Correct Answers', 'Incorrect Answers']
    values = [st.session_state.correct_answers, st.session_state.incorrect_answers]
    colors = ['green', 'red']

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent', marker_colors=colors, pull=[0.1, 0])])
    fig.update_layout(title_text="Test Results")

    st.write(fig)

# Donation Note at the bottom
st.markdown("If you found this app helpful, consider making a donation to support development. Thank you! 🙏")
st.markdown("Bitcoin (BTC) Address: 🔗 `bc1qkru3pwy9jhn2gsmet245ssd9xx5mlzcvpgczpy`")
st.markdown("Polygon Address: 🔗 `0x5eBDB6031BeCa2A9a538A00477dC8049244e86fe`")
