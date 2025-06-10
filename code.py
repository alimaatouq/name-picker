import streamlit as st
import random
import os

st.set_page_config(page_title="Presenter Picker", page_icon="🎤")
st.title("🎤 Random Presenter Picker (With Photos)")

# Define names and image file mappings
people = {
    "Ali M": "images/ali_m.jpg",
    "Ali S": "images/ali_s.jpg",
    "Samer": "images/samer.jpg",
    "Aazim": "images/aazim.jpg",
    "Sidra": "images/sidra.jpg",
}

names = list(people.keys())

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

# Dropdown to manually select the last presenter
last_presenter = st.selectbox("👤 Who presented last?", ["None"] + names)
last_presenter = None if last_presenter == "None" else last_presenter

# Pick button
if st.button("🎲 Pick Next Presenter"):
    possible_choices = [name for name in names if name != last_presenter]
    if not possible_choices:
        st.warning("Only one name available. Everyone else has already presented.")
    else:
        chosen = random.choice(possible_choices)
        st.success(f"🎉 Selected: **{chosen}**")
        st.session_state.history.append((last_presenter, chosen))

        # Show image
        image_path = people.get(chosen)
        if image_path and os.path.exists(image_path):
            st.image(image_path, caption=chosen, use_column_width=True)
        else:
            st.info("📷 No image available for this person.")

# Show history
if st.session_state.history:
    st.subheader("🕓 Pick History")
    for i, (last, current) in enumerate(st.session_state.history, 1):
        st.write(f"{i}. Last: {last or 'None'} → Now: {current}")
