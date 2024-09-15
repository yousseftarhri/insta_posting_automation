import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class Img_generation:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.openai_api_key)


    def generate_img(self):
        response = self.client.images.generate(
            model="dall-e-3",
            prompt="A moroccan house",
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        print(image_url)



img = Img_generation()
img.generate_img()