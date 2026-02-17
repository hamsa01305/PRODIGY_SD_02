import streamlit as st
import random

st.set_page_config(page_title="Guessing Game", page_icon="🎮")

st.title("🎮 Number Guessing Game")
st.write("I have selected a random number between 1 and 100.")
st.write("Try to guess it!")

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.warning("Too low! Try again.")
    elif guess > st.session_state.number:
        st.warning("Too high! Try again.")
    else:
        st.success("🎉 Congratulations! You guessed the correct number!
