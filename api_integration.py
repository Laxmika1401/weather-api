from http.client import HTTPResponse
import os
import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv

load_dotenv()

class WeatherService:
    """
    A class that interacts with a weather API to retrieve weather information for a given city.

    Args:
        city (str): The name of the city for which weather information is requested.
        data_format (str): The desired format of the weather information. Can be 'json' or 'xml'.

    Methods:
        get_info(): Retrieves the weather information for the specified city in the requested format.

    Attributes:
        city (str): The name of the city for which weather information is requested.
        data_format (str): The desired format of the weather information.

    """

    def __init__(self, city: str, data_format: str):
        """
        Initializes a WeatherService instance.

        Args:
            city (str): The name of the city for which weather information is requested.
            data_format (str): The desired format of the weather information. Can be 'json' or 'xml'.
        """
        self.city = city
        self.data_format = data_format

    def get_info(self):
        """
        Retrieves the weather information for the specified city in the requested format.

        Returns:
            dict or str: A dictionary containing weather information in JSON format if the data_format is 'json',
                        or an XML string containing weather information if the data_format is 'xml'.
                        If the data_format is neither 'json' nor 'xml', returns a string indicating that
                        the data format is not applicable.
            None: Returns None if there is an error in retrieving the weather information.
        """
       
        url = "https://weatherapi-com.p.rapidapi.com/current.json"

        querystring = {"q":self.city}
        headers = {
            "X-RapidAPI-Key": os.getenv('API-KEY'),
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        print("Response", response)
        json_data = response.json()
        
        if "error" in json_data:
            return None
        
        response_data = {
            "Weather": str(json_data["current"]["temp_c"])+" C",
            "Latitude": json_data["location"]["lat"],
            "Longitude": json_data["location"]["lon"],
            "City": json_data["location"]["name"] + " " + json_data["location"]["country"],
        }

        if self.data_format == "json":
            return response_data
        
        if self.data_format == 'xml':
            xml_data = """
            <?xml version="1.0" encoding="UTF-8" ?>
            <root>
            <Temperature>{0}</Temperature>
            <City>{1}</City>
            <Latitude>{2}</Latitude>
            <Longitude>{3}</Longitude>
            </root>
            """.format(
                response_data["Weather"],
                response_data["City"],
                response_data["Latitude"],
                response_data["Longitude"],
            )
            return xml_data
        else:
            return "Not applicable data format"
    