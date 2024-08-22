from fastapi import FastAPI
from starlette import requests
from auth import Auth
from joke import Joke
from logger import setup_logger
from middleware import LoggingMiddleware
import os

app = FastAPI()

# ENV variables
LOGGER_MESSAGE_FORMAT = os.getenv("logger_message_format", "%(asctime)s - %(levelname)s - %(message)s - %(filename)s "
                                                           "- %(lineno)d")
LOGGER_DATE_FORMAT = os.getenv("logger_date_format", "%Y-%m-%d %H:%M:%S")

setup_logger(
    log_to_file=True,
    log_file_path='app.log',
    message_format=LOGGER_MESSAGE_FORMAT,
    date_format=LOGGER_DATE_FORMAT
)

app.add_middleware(LoggingMiddleware)


@app.get("/joke")
async def root():
    response = requests.get("https://api.chucknorris.io/jokes/random").json()
    Joke.from_dict(response)
    return Joke.from_dict(response)


app.add_middleware(Auth)
