import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = "gemini-1.5-flash"

def load_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except IOError as e:
        print(f"Error loading file: {e}")

def save_file(file_name, content):
    try:
        with open(file_name, 'w', encoding="utf-8") as file:
            file.write(content)
    except IOError as e:
        print(f"Error saving file: {e}")

product_name = "Organic cotton t-shirts"

user_prompt = load_file(f"Alura\Gemini e Python criando ferramentas com a API\Gemini - Sentiment analysis tool\\data\\reviews-{product_name}.txt")

print(f"Starting sentiment analysis for the product: {product_name}")

llm = genai.GenerativeModel(
    model_name=model,
    system_instruction="""
        You are a sentiment analyzer for product reviews.
        Write a paragraph of up to 50 words summarizing the reviews and
        then assign the overall sentiment for the product.
        Also identify 3 strengths and 3 weaknesses found in the reviews.

        # Output Format

        Product Name:
        Review Summary:
        Overall Sentiment: [use only Positive, Negative or Neutral here]
        Strengths: list with three bullets
        Weaknesses: list with three bullets
    """
)

response = llm.generate_content(user_prompt)
response_text = response.text

save_file(f"Alura\Gemini e Python criando ferramentas com a API\Gemini - Sentiment analysis tool\\data\\sentiment analysis-{product_name}.txt", response_text)