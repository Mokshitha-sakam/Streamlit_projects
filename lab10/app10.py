
import streamlit as st
import requests

st.set_page_config(
    page_title="Lab 10 - API Integration",
    page_icon="🌦️",
    layout="centered"
)

st.title("Lab 10: API Integration")
st.subheader("Weather Information App")

st.write("Enter a city name to get current weather information.")

city = st.text_input("Enter City Name", "Chennai")

if st.button("Get Weather"):
    if city.strip():
        try:
            url = f"https://wttr.in/{city}?format=j1"
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                weather = data["current_condition"][0]

                st.success(f"Weather Details for {city}")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Temperature",
                        str(weather["temp_C"]) + " °C"
                    )

                with col2:
                    st.metric(
                        "Feels Like",
                        str(weather["FeelsLikeC"]) + " °C"
                    )

                st.write(
                    "Weather Condition:",
                    weather["weatherDesc"][0]["value"]
                )

                st.write("Humidity:", str(weather["humidity"]) + "%")
                st.write("Wind Speed:", str(weather["windspeedKmph"]) + " km/h")

                with st.expander("View JSON Response"):
                    st.json(data)

            else:
                st.error("Unable to fetch weather information.")

        except requests.exceptions.RequestException:
            st.error("API request failed. Check your internet connection.")

        except (KeyError, IndexError, ValueError):
            st.error("Unable to process the API response.")

    else:
        st.warning("Please enter a city name.")
