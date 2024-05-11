import streamlit as st
from itinerary import generate_itinerary

# Set page title and background
st.set_page_config(page_title="Wanderlust Itinerary Planner", page_icon="✈️", layout="wide")

# Header with title and quote
st.title("Wanderlust Itinerary Planner 🌍✈️")
st.markdown("> Adventure awaits where the WiFi is weak!")

# User input section
st.sidebar.header("Enter Details")
num_persons = st.sidebar.slider("Number of Persons", 1, 30, 1)
destination = st.sidebar.text_input("Destination", "Paris, France")
num_days = st.sidebar.number_input("Number of Days", min_value=1)

preferences = st.sidebar.multiselect("Preferences", ["Food", "Shopping", "History", "Culture", "Nature", "Adventure", "Nightlife","Architecture"])

# Itinerary generation
itinerary = f"**Hello traveller! 🌟 This is your itinerary:**\n\n"
itinerary += f"- **Destination:** {destination}\n"
itinerary += f"- **Number of Persons:** {num_persons}\n"
itinerary += f"- **Number of Days:** {num_days}\n"
itinerary += f"- **Preferences:** {', '.join(preferences)}\n"

# Display the itinerary
st.markdown(itinerary)


# Background image
st.markdown(
    """
    <style>
        .my-button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if st.button("Generate Itinerary"):
    with st.spinner("Generating Itinerary..."):
        try:
            generated_itinerary = generate_itinerary(num_persons,destination,num_days,preferences)  # Call your function to generate the itinerary
            st.success("Itinerary Generated!")
            st.text(generated_itinerary)  # Display the generated itinerary
        except Exception as e:
            st.error(f"Error generating itinerary: {e}")
