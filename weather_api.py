from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')

# Configuration
API_KEY = "635da69330600c094e7c30f498c64e90"
DEFAULT_CITY = "London"


def get_weather_data(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Weather API Error: {e}")
        return None


@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    city = DEFAULT_CITY

    if request.method == 'POST':
        city = request.form.get('city', DEFAULT_CITY).strip()
        if city:
            weather_data = get_weather_data(city)

    return render_template('weather.html', weather=weather_data, city=city)


if __name__ == '__main__':
    # Create required folders if they don't exist
    os.makedirs('static', exist_ok=True)
    os.makedirs('templates', exist_ok=True)

    app.run(debug=True, port=5000)