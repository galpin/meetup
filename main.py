import os
from dataclasses import dataclass
from urllib.parse import urlencode

import streamlit as st
from dotenv import load_dotenv


@dataclass(frozen=True)
class StartPoint:
    name: str
    address: str


gmaps_api_key = os.getenv("GMAPS_API_KEY")
start_points = [
    StartPoint(name="🐬", address="Leytone Underground Station"),
    StartPoint(name="🏎️", address="St Pancras International"),
]
location_suffix = "London, UK"


def google_map(origin: str, destination: str):
    params = {
        "key": gmaps_api_key,
        "origin": f"{origin} {location_suffix}",
        "destination": f"{destination} {location_suffix}",
        "mode": "transit",
    }
    url = f"https://www.google.com/maps/embed/v1/directions?{urlencode(params)}"
    st.markdown(
        f'<iframe width="100%" height="450" loading="lazy" src="{url}" />',
        unsafe_allow_html=True,
    )


def directions(name: str, origin: str, destination: str):
    st.write(f"## {name}")
    google_map(origin, destination)


def app():
    st.set_page_config(page_title="🐬🏎️ meet up")
    with st.form(key="search"):
        destination = st.text_input("Enter a place to meet:")
        go_button = st.form_submit_button("Go")
    if not destination or not go_button:
        return
    for start in start_points:
        directions(start.name, start.address, destination)


if __name__ == "__main__":
    load_dotenv()
    app()
