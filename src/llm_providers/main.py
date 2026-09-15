from openai import OpenAI
from dotenv import load_dotenv
from config.config import Settings
import os

settgings = Settings()

client = OpenAI(api_key=os.getenv('GROQ_API_KEY'),base_url=os.getenv('BASE_URL'))

response = client.responses.create(model=os.getenv('MODEL_NAME'),input="my name is abram how are you ")



print(response.output_text)
