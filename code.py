import streamlit as st
import random

st.title("🎲 Random Name Picker (No Repeats!)")

# Initialize session state
if "names" not in st.session_state:
    st.session_state.names = []
if "last_name" not in st.session_state:
    st.session_state.last_name = None
if "history" not in st.session_state:
    st.session_state.history = []

# Input names
name_input = st.text_area("Enter names (one per line)", height=150)
if st.button("Save Names"):
    names = [name.strip() for name in name_input.split("\n") if name.strip()]
    if len(names) < 2:
        st.error("Please enter at least two names.")
    else:
        st.session_state.names = names
        st.session_state.last_name = None
        st.session_state.history = []
        st.success("Names saved!")

# Display saved names
if st.session_state.names:
    st.subheader("📋 Saved Names")
    st.write(", ".join(st.session_state.names))

    # Pick random name
    if st.button("🎤 Pick Presenter"):
        possible_choices = [
            name for name in st.session_state.names
            if name != st.session_state.last_name
        ]
        if not possible_choices:
            st.warning("Only one name available or no alternatives. Resetting history.")
            possible_choices = st.session_state.names
        chosen = random.choice(possible_choices)
        st.session_state.last_name = chosen
        st.session_state.history.append(chosen)
        st.success(f"🎉 Selected: **{chosen}**")

    # Show history
    if st.session_state.history:
        st.subheader("🕓 History")
        st.write(" → ".join(st.session_state.history))
