#Try to generate an image 
from together import Together
import os
from dotenv import load_dotenv

load_dotenv()

TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")
if not TOGETHER_API_KEY:
    raise ValueError("TOGETHER_API_KEY is not set in the environment variables.")
client = Together()
response = client.images.generate(
    prompt="Generate an image of a serene mountain landscape at sunrise, with a clear sky and a calm lake reflecting the mountains.",
    model="black-forest-labs/FLUX.1-schnell-Free", 
    n=2,
    steps = 2
)

#save the image to a file
# with open('generated_image.png', 'wb') as f:
    # f.write(response.data[0].b64_json.decode('base64'))  # Decoding the base64 image data and writing to file
print(response)
print(response.data[0].b64_json)  # Printing base64 encoded image data