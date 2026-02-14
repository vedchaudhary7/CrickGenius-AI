import streamlit as st
import json
import random

st.set_page_config(page_title="CrickGenius AI", layout="wide")

st.title("🏏 CrickGenius AI")
st.subheader("Smart Cricket Chatbot for IPL & International Cricket")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Chat Mode", "IPL Teams", "International Cricket", "Match Predictor", "Cricket Quiz"]
)

with open("cricket_data.json", "r") as file:
    data = json.load(file)

if menu == "Chat Mode":
    user_input = st.text_input("Ask anything about cricket:")

    if user_input:
        user_input = user_input.lower()
        found = False

        for player in data["players"]:
            if player in user_input:
                st.success(data["players"][player])
                found = True

        for team in data["ipl_teams"]:
            if team in user_input:
                st.success(data["ipl_teams"][team])
                found = True

        if not found:
            st.warning("Information not found in database.")

elif menu == "IPL Teams":
    team = st.selectbox("Select IPL Team", list(data["ipl_teams"].keys()))
    st.info(data["ipl_teams"][team])

elif menu == "International Cricket":
    st.write(data["world_cup"])

elif menu == "Match Predictor":
    team1 = st.text_input("Enter Team 1")
    team2 = st.text_input("Enter Team 2")

    if st.button("Predict"):
        score1 = random.randint(40, 90)
        score2 = random.randint(40, 90)

        if score1 > score2:
            st.success(f"{team1} has higher winning probability!")
        else:
            st.success(f"{team2} has higher winning probability!")

elif menu == "Cricket Quiz":
    question = random.choice(data["quiz"])
    st.write(question["question"])

    answer = st.text_input("Your Answer")

    if st.button("Submit"):
        if answer.lower() == question["answer"]:
            st.success("Correct!")
        else:
            st.error(f"Correct answer: {question['answer']}")
