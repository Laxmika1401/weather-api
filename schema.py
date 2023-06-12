from pydantic import BaseModel

class ReqestBody(BaseModel):
    """
    Represents the request body for retrieving weather information.

    Attributes:
        city (str): The name of the city for which weather information is requested.
        output_type (str): The desired output format of the weather information. Can be 'json' or 'xml'.
    """
    city: str
    output_type: str
