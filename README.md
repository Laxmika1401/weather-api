# Weather API Integration Project

This project aims to integrate a weather API into a FastAPI application. The application retrieves weather information from the WeatherService based on the provided request data, such as the city and desired output format. It returns the weather information in JSON format if the output type is 'json' or in XML format if the output type is 'xml'.

## Installation

1. Clone the repository:


2. Navigate to the project directory:


3. Create a virtual environment (optional but recommended):


4. Install the dependencies:


5. Set up the API key:

- Sign up for an account at the weather API provider's website.
- Obtain an API key for accessing the weather data.
- Open the `.env` file and set the `API_KEY` variable to your API key.

## Usage

1. Start the FastAPI server:


2. Open your browser and navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to access the Swagger UI. The Swagger UI provides an interactive interface for testing the API endpoints.

3. Explore the available endpoints:

- `/getCurrentWeather` (POST): Retrieves weather information based on the provided request data.
  - Request Body:
    ```
    {
      "city": "string",
      "output_type": "string"
    }
    ```
  - Response:
    - If the output type is "json", the response will be a JSON object containing weather information.
    - If the output type is "xml", the response will be an XML response object containing weather information.

## API Documentation

The API documentation is generated using Swagger UI and can be accessed by navigating to [http://localhost:8000/docs](http://localhost:8000/docs) when the FastAPI server is running. The documentation provides detailed information about the available endpoints, their request/response formats, and allows you to interactively test the API.

## Testing

To run the test cases for the weather API integration project, use the following command:


The test cases are located in the `tests` directory and cover various scenarios, including successful retrieval, invalid output format, no matching location found, case-insensitivity, special characters in city name, and empty city name.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on the project repository.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for personal or commercial purposes.
