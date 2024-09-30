import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class Img_generation:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.openai_api_key)


    def generate_prompt(self):
        prompt = [{"role": "system", "content": """Generate a prompt about building and house niche"""}]
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.7,
            messages=prompt
        )
        print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    def generate_img(self,prompt):
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        print(image_url)
        return image_url

