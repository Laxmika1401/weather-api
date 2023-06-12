import os
from fastapi.testclient import TestClient
from dotenv import load_dotenv

from .main import app

client = TestClient(app)

def test_to_get_weather_info():
    response = client.post(
        "/getCurrentWeather",
        headers = {
            "X-RapidAPI-Key": os.getenv('API-KEY'),
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        },
        json={"city": "Bhilwara", "output_type": "json"},
    )
    assert response.status_code == 200
    assert response.json() == {
        {
            "Weather": "41.2 C",
            "Latitude": 25.35,
            "Longitude": 74.63,
            "City": "Bhilwara India"
        }
    }
