# app/main.py

import streamlit as st
from app.data import questions

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

def run_app():
    # Add the custom CSS function
    # Adjust the font size
    custom_css("18px")  # Adjust "18px" to your desired font size


    st.title("DP203 Exam")

    for idx, q in enumerate(questions, 1):
        st.markdown(f"**Question {idx}**: {q['question']}", unsafe_allow_html=True)
        if 'image' in q:
            st.image(q['image'])
        answer = st.radio(f"Choices {idx}:", q['choices'])

        if st.button(f"Check Answer for Question {idx}"):
            if answer == q['answer']:
                st.success(f"Correct! The answer is {q['answer']}.")
                st.info(f"Explanation: {q['explanation']}")
            else:
                st.error(f"Wrong answer. The correct answer is {q['answer']} and the explanation is: \n\n {q['explanation']}.")

