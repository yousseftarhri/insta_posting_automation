import schedule
import time
from content_post import Post
from img_generation import Img_generation

def call_functions():
    img = Img_generation()
    post_img = Post()

    prompt = img.generate_prompt()
    image_url = img.generate_img(prompt)

    container_id = post_img.create_container(image_url)
    post_img.publish_container(container_id)


#Schedule the call_functions method to run every day
schedule.every().day.at("01:00").do(call_functions)
print("Scheduler started, calling functions every day")

# Keep the scheduler running
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep to prevent high CPU usage