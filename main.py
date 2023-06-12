from fastapi import FastAPI, Response, HTTPException
from schema import ReqestBody
from api_integration import WeatherService

app = FastAPI(title="Weather_API")


@app.post("/getCurrentWeather")
async def weather_api(data: ReqestBody):
    """
    Retrieves weather information from the WeatherService based on the provided request data.

    Args:
        data (ReqestBody): An object containing the request data including the city and desired output format.

    Returns:
        dict or Response: A dictionary containing weather information in JSON format if the output_type is 'json',
                          or a Response object containing weather information in XML format if the output_type is 'xml'.

    Raises:
        HTTPException: Raises an HTTPException with status code 400 and an appropriate error message if there are any issues,
                       such as an invalid output format or no matching location found.
    """
    data.output_type = data.output_type.casefold()
    weather_obj = WeatherService(data.city, data.output_type)
    weather_info = weather_obj.get_info()

    if weather_info:
        if data.output_type == "json":
            return weather_info
        elif data.output_type == "xml":
            return Response(content=weather_info, media_type="application/xml")
        else:
            raise HTTPException(status_code=400, detail="Invalid output_format")
    else:
        raise HTTPException(status_code=400, detail="No matching location found")
