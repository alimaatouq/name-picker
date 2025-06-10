import streamlit as st
import random

st.title("🎤 Random Presenter Picker (No Repeats)")

# Fixed list of names
names = ["Ali M", "Ali S", "Samer", "Aazim", "Sidra"]

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

# Select the last presenter
last_presenter = st.selectbox("👤 Who presented last?", ["None"] + names)
last_presenter = None if last_presenter == "None" else last_presenter

# Button to pick the next presenter
if st.button("🎲 Pick Next Presenter"):
    possible_choices = [name for name in names if name != last_presenter]

    if not possible_choices:
        st.warning("Only one name available. Everyone has already presented.")
    else:
        chosen = random.choice(possible_choices)
        st.success(f"🎉 Selected: **{chosen}**")
        st.session_state.history.append((last_presenter, chosen))

# Show history
if st.session_state.history:
    st.subheader("🕓 History")
    for i, (last, current) in enumerate(st.session_state.history, 1):
        st.write(f"{i}. Last: {last or 'None'} → Now: {current}")
