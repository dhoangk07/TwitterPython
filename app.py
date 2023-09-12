import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from tweet import create_and_post_tweet
from telegram import send_error_to_telegram
app = FastAPI()

class Item(BaseModel):
  author: str
  title: str
  technique: str
  location: str
  imageUrl: str
  form: str
  type: str
  school: str
  date: str

@app.post('/row', tags=["Post images to twitter"], status_code=202)
async def twitter(item: Item):
  try:
    object = item.dict()
    print(object)
    create_and_post_tweet(object)
    return 'Post images to twitter successful. Please check :)))'
  except Exception as e:
    send_error_to_telegram(e)
