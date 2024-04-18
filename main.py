from fastapi import FastAPI
import logging
from random import randint
from pydantic import BaseModel
from opentelemetry import trace
from opentelemetry import metrics

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/")
async def roll_dice():
    result = str(roll())
    logger.warning("Anonymous player is rolling the dice: %s", result)
    return result


def roll():
    return randint(1, 6)


