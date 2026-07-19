# Weather API Client (CLI)

A command-line Weather API Client built with Python that allows users to search the current weather of any city using the OpenWeather API.

The application stores search history in a JSON file, logs user activities, and demonstrates modular Python programming.

##  Features

-  Search current weather by city name
-  Display:
  - Temperature
  - Feels Like Temperature
  - Humidity
  - Wind Speed
  - Atmospheric Pressure
  - Weather Description
-  Save search history locally
-  View previous searches
-  Clear search history
-  Log application activities
-  Secure API key using `.env`

---

##  Technologies Used

- Python 3
- OpenWeather API
- Requests
- Python-dotenv
- JSON
- Logging

---

##  Project Structure

weather_client/
│
├── app.py              # Main application and menu
├── weather.py          # Weather API logic
├── storage.py          # Read/Write search history
├── config.py           # Load API key from .env
├── exceptions.py       # User input handling
├── logger.py           # Logging configuration
├── history.json        # Search history
├── requirements.txt
├── README.md
├── .env
└── .gitignore
## Installation

### Clone the repository

bash
git clone https://github.com/YOUR_USERNAME/weather-api-client.git

Move into the project directory.

bash
cd weather-api-client

Create a virtual environment.

Windows:
bash
python -m venv .venv

Activate it.

Windows:
bash
.venv\Scripts\activate

Install dependencies.

bash
pip install -r requirements.txt

##  API Setup

Create a `.env` file inside the project folder.

API_KEY=YOUR_OPENWEATHER_API_KEY

You can get your free API key from:

https://openweathermap.org/

## Run the Project

bash
python app.py

## Example

-----------------------------
 Welcome to Weather Client
-----------------------------

1 Search Weather
2 View Search History
3 Clear History
4 Exit

Enter your choice: 1

Enter city name:
Islamabad

Temperature: 35°C
Feels Like: 37°C
Humidity: 42%
Wind Speed: 2.6 m/s
Pressure: 1008 hPa
Description: Clear Sky

## What I Learned

- Working with REST APIs
- Sending HTTP requests using Requests
- Parsing JSON responses
- Using environment variables
- Logging application events
- Organizing Python projects
- Reading and writing JSON files
- Error handling

## Future Improvements

- 5-Day Weather Forecast
- Search by GPS Coordinates
- Weather Icons
- Colored Terminal Output
- Better Search History
- Export History to CSV
- Unit Testing with Pytest
- Caching Previous Searches


##  Author
Rehmat Ullah

AI Graduate | Python Developer | Future AI SaaS Founder

