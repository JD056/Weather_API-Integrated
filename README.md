🌦️ Weather App (Flask + OpenWeatherMap)
A simple web app built with Flask that fetches and displays current weather data for any city using the OpenWeatherMap API.

🚀 Features
Search weather by city name

Displays temperature, weather condition, and more

Uses Flask for backend and HTML templates for frontend

🔧 Requirements
Python 3.x

Flask

requests

Install dependencies:

bash
Copy
Edit
pip install flask requests
▶️ How to Run
Clone this repository.

Replace the API_KEY in weather_api.py with your own from OpenWeatherMap.

Run the app:

bash
Copy
Edit
python weather_api.py
Open http://localhost:5000 in your browser.

📝 Folder Structure
cpp
Copy
Edit
├── weather_api.py
├── templates/
│   └── weather.html
├── static/
📌 Note
Make sure you create the templates and static folders with appropriate files (e.g., weather.html).
