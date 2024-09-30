import os
import requests
from dotenv import load_dotenv

load_dotenv()


class Post:

    def __init__(self):
        self.access_token = os.getenv('access_token')
        self.ig_user_id = os.getenv("ig_user_id")


    def create_container(self, image_url):

        url = f"https://graph.facebook.com/{self.ig_user_id}/media"
        caption = "#hello"

        payload = {
            "image_url": image_url,
            "caption": caption,
            "access_token": self.access_token
        }

        response = requests.post(url, data=payload)

        if response.status_code == 200:
            print("Container created successfully:", response.json())
            return response.json()['id']
        else:
            print("Failed to create the container:", response.status_code, response.text)

    def publish_container(self,creation_id):

        # URL for publishing media
        url = f"https://graph.facebook.com/{self.ig_user_id}/media_publish"


        payload = {
            "creation_id": creation_id,
            "access_token": self.access_token
        }

        response = requests.post(url, data=payload)

        if response.status_code == 200:
            print("Media published successfully:", response.json())
        else:
            print("Failed to publish media:", response.status_code, response.text)

