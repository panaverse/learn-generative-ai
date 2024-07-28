from fastapi import FastAPI
import json
from sqlmodel import SQLModel

app = FastAPI( title="Weather API", 
    version="0.0.1",
    servers=[
        {
            "url": "http://127.0.0.1:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
        ])

@app.get("/city/")
def get_current_weather1(location:str, unit:str="fahrenheit")->str:
    """Get the current weather in a given location"""
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "10", "unit": "celsius"})
    elif "san francisco" in location.lower():
        return json.dumps({"location": "San Francisco", "temperature": "72", "unit": "fahrenheit"})
    elif "paris" in location.lower():
        return json.dumps({"location": "Paris", "temperature": "22", "unit": "celsius"})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})

class WeatherRequest(SQLModel):
    location: str
    unit: str = "fahrenheit"

@app.post("/get_current_weather")
def get_current_weather(weather_request: WeatherRequest):
    location = weather_request.location
    unit = weather_request.unit
    
    """Get the current weather in a given location"""
    if "karachi" in location.lower():
        return json.dumps({"location": "Karachi", "temperature": "10", "unit": "celsius"})
    elif "islamabad" in location.lower():
        return json.dumps({"location": "Islamabad", "temperature": "72", "unit": "fahrenheit"})
    elif "lahore" in location.lower():
        return json.dumps({"location": "Lahore", "temperature": "22", "unit": "celsius"})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})