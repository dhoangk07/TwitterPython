from auth import get_twitter_conn_v1, get_twitter_conn_v2
import requests
import json
from telegram import send_to_telegram, send_error_to_telegram

client_v1 = get_twitter_conn_v1()
client_v2 = get_twitter_conn_v2()

def download_image(image_url):
  response = requests.get(image_url)
  image_data = response.content
  with open('wga.jpg', 'wb') as f:
    f.write(image_data)

def create_and_post_tweet(object):
  try:
    image_url = object['imageUrl']
    author = object['author']
    date = object['date']
    title = object['title']
    technique = object['technique']
    location = object['location']
    raw_author = author.replace(' ', '').replace('.', '').replace(',', '')
    hash_tag = f'#{raw_author} \n#oilpainting \n#ArtLovers \n#RenaissancePainting'
    tweet = f'Author: {author} \nTitle: {title} \nDate: {date} \n{hash_tag}'
    download_image(image_url)
    media = client_v1.simple_upload(filename='hu.jpg')
    client_v2.create_tweet(text=tweet, media_ids=[media.media_id])
    send_to_telegram(tweet)
    return 'Post Image to Twitter successful'
  except Exception as e:
    send_error_to_telegram(e)
