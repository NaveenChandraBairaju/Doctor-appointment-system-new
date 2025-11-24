# How to Enable ChatGPT-like AI Chatbot

Your chatbot currently uses a rule-based system. To make it work like ChatGPT/Gemini (understanding ANY question naturally), follow these steps:

## 🔑 Get Google Gemini API Key (FREE)

### Step 1: Go to Google AI Studio
Visit: https://makersuite.google.com/app/apikey

### Step 2: Sign in with Google Account
- Use your Gmail account
- Accept terms and conditions

### Step 3: Create API Key
1. Click "Create API Key"
2. Select "Create API key in new project" (or use existing)
3. Copy the API key (starts with "AIza...")

### Step 4: Add API Key to Your Project
1. Open file: `ai_chat.py`
2. Find line 8: `API_KEY = 'AIzaSy...'`
3. Replace with your new API key
4. Save the file

### Step 5: Restart Server
- Stop the Flask server (Ctrl+C)
- Start again: `python app.py`
- You should see: "✓ Gemini AI initialized successfully!"

## ✅ What You'll Get

Once Gemini AI is enabled, your chatbot will:

✨ **Understand Natural Language:**
- "my friend has injury in hand bleeding" → Understands and gives first aid
- "amar has motions" → Understands it's diarrhea
- "feeling tired all day" → Understands fatigue
- ANY way of asking → AI understands!

✨ **Intelligent Responses:**
- Context-aware answers
- Personalized advice
- Natural conversation
- Handles complex questions

✨ **Better Than Keywords:**
- No need for exact words
- Understands intent
- Handles typos
- Multi-language support

## 🆓 Free Tier Limits

Google Gemini API Free Tier:
- 60 requests per minute
- Completely FREE
- No credit card required
- Perfect for your project!

## 🔧 Troubleshooting

**If API key doesn't work:**
1. Make sure you copied the entire key
2. Check if key is enabled in Google Cloud Console
3. Wait a few minutes after creating (activation time)
4. Try creating a new key

**Current Status:**
- Your chatbot works with comprehensive rule-based system
- Covers 100+ medical conditions
- Knows all website features
- But Gemini AI will make it MUCH smarter!

## 📝 Note

Even without Gemini API, your current chatbot is very comprehensive and covers:
- All common medical conditions
- Injuries, wounds, bleeding
- Chronic diseases
- Mental health
- Women's health
- Complete website knowledge

But with Gemini, it becomes truly intelligent like ChatGPT! 🚀
