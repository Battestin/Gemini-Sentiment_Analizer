# Sentiment Analyzer

Python tool that processes product reviews with Google Gemini 1.5 Flash to generate concise sentiment summaries, highlighting overall sentiment plus key strengths and weaknesses.

## 🚀 How to Run

1. Clone the repo  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API key:  
   ```
   GEMINI_API_KEY=your_google_api_key_here
   ```

4. Prepare review text files in the `data` folder, named like `reviews-<product_name>.txt`.

5. Run the script:  
   ```bash
   python sentiment_analyzer.py
   ```

## 🧠 What it Does

- Loads product reviews from text files  
- Summarizes reviews in up to 50 words  
- Assigns overall sentiment: Positive, Negative, or Neutral  
- Lists 3 strengths and 3 weaknesses from reviews  
- Saves analysis results as text files

## ⚠️ Notes

- Paths to data files are hardcoded; adjust if needed  
- Model fallback included on errors (retries with flash model)  
- Designed for quick sentiment insights, validate outputs for critical use

## 📄 License

MIT
