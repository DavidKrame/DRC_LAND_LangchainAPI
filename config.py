from dotenv import load_dotenv
import os

load_dotenv()

# OpenAI and Supabase configurations
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SUPABASE_URI = os.getenv("SUPABASE")
