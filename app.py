import streamlit as st
from joblib import load
import numpy as np
import json
from PIL import Image
import os

# Page setup
st.set_page_config(page_title="⚽ Match Predictor", layout="centered")
st.title("⚽ Football Match Outcome Predictor")
st.markdown("""
Welcome to your personal match oracle!  
Enter the match stats and see who’s likely to win — based on real data from the **2018–19 football season** 🗓️  
""")

# Load trained model
model = load("exportedModels/rf_classifier.model")

# Load team mappings
with open("exportedModels/metaData.json", "r") as f:
    meta = json.load(f)

home_team_map = meta["home_teams"]
away_team_map = meta["away_teams"]

# Reverse mappings: encoded ID → team name
home_team_names = {v: k for k, v in home_team_map.items()}
away_team_names = {v: k for k, v in away_team_map.items()}


# Function to load logo if available
def get_logo(team_name):
    logo_file = f"logos/{team_name.lower().replace(' ', '')}.png"
    if os.path.exists(logo_file):
        return Image.open(logo_file)
    return None


# Layout: two columns for home and away
col1, col2 = st.columns(2)

with col1:
    selected_home_name = st.selectbox("🏠 Home Team", list(home_team_names.values()))
    home_logo = get_logo(selected_home_name)
    if home_logo:
        st.image(home_logo, caption=f"{selected_home_name}", width=100)
    else:
        st.caption(f"No logo available for {selected_home_name}")

    HTHG = st.number_input("Half-Time Goals (Home)", min_value=0)
    HS = st.number_input("Shots (Home)", min_value=0)
    HST = st.number_input("Shots on Target (Home)", min_value=0)
    HR = st.number_input("Red Cards (Home)", min_value=0)

with col2:
    selected_away_name = st.selectbox("🚗 Away Team", list(away_team_names.values()))
    away_logo = get_logo(selected_away_name)
    if away_logo:
        st.image(away_logo, caption=f"{selected_away_name}", width=100)
    else:
        st.caption(f"No logo available for {selected_away_name}")

    HTAG = st.number_input("Half-Time Goals (Away)", min_value=0)
    AS = st.number_input("Shots (Away)", min_value=0)
    AST = st.number_input("Shots on Target (Away)", min_value=0)
    AR = st.number_input("Red Cards (Away)", min_value=0)

# Friendly outcome mapping
outcome_map = {
    'H': f"🏠 **{selected_home_name} wins!**",
    'A': f"🚗 **{selected_away_name} wins!**",
    'D': "🤝 **It's a draw!**"
}

# Prediction button
if st.button("🔮 Predict Outcome"):
    sample_input = [[home_team_map[selected_home_name], away_team_map[selected_away_name],
                     HTHG, HTAG, HS, AS, HST, AST, HR, AR]]
    prediction = model.predict(sample_input)[0]
    st.markdown(f"### Prediction: {outcome_map[prediction]}")
    st.caption("📊 Prediction based on historical match data from the 2018–19 season.")