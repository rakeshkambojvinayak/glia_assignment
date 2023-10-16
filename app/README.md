<!-- #region -->
# FastAPI Application Instructions

These instructions guide you on how to build and run a FastAPI application, both with and without Docker.

## Prerequisites for the application without Docker

1. Install all available libraries from the `requirements.txt` file.
2. Run the following command to start the application:
   
   ```bash
   uvicorn app:app --reload
   
3. Run below request api

or 

## Prerequisites for Docker level application

Ensure you have the following prerequisites installed on your system:

- Docker
- A working internet connection

## Application Files

Make sure you have the following files in your project directory:

- `requirements.txt`: Contains the list of required Python libraries.
- `Dockerfile`: Defines the Docker image for the application.
- `app.py`: The main FastAPI application script.

## Build and Run the Docker Image

1. Start Docker engine and open docker comand prompt


2. Build the Docker image using the following command:
docker build -t app .

3. Run the Docker image using the following command:
docker run -p 8000:8000 app

	
## Accessing the API

You can access the FastAPI API to classify news articles into categories using the following steps:

#### Sending a POST Request

To classify a news article, send a POST request to the `/classify` endpoint with the news article text as JSON data.

#### Example using cURL:
<!-- #endregion -->

<!-- #region -->
Request:

curl --location --request POST 'http://127.0.0.1:8000/classify' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text": "tv future in the hands of viewers with home theatre systems, plasma high-definition TVs, and digital video recorders moving into"
}'


Reponse:
    
{
    "label": "Entertainment",
    "confidence": "0.997292"
}

<!-- #endregion -->
