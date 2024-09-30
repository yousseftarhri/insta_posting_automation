# insta_posting_automation

This repository contains an automated bot that generates AI images based on prompts and posts them to a platform daily at a scheduled time. The bot leverages two key components: image generation and posting functionality.

## Features
- **Image Generation**: Automatically generates images based on dynamically created prompts.
- **Automated Posting**: Posts the generated images to a platform on a scheduled basis (daily at 01:00).
- **Scheduler**: Uses a scheduler to ensure the bot runs and posts without manual intervention.

## Prerequisites

Ensure that you have the following installed:

- Python 3.x

To install the required packages, run:

```bash
pip install -r requirements.txt
```
### Project Structure
- **content_post.py**: Contains the Post class, responsible for handling the image posting process.
- **img_generation.py**: Contains the Img_generation class, which generates the prompt and corresponding image.
- **main.py**: Main script that brings the functionality together, scheduling the image generation and posting.

### Example Workflow
At 01:00 every day:
1. A prompt is generated.
2. An image is created using the prompt.
3. The image is posted to the platform (**Instagram**).

### How to Run
Run the script:
```bash
python main.py
```