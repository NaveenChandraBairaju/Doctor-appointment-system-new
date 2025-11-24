# SmartClinic AI Setup Guide

## Enable Real AI Chatbot (Free!)

Your SmartClinic AI chatbot can now use Google's Gemini AI for intelligent responses!

### Step 1: Get Free API Key

1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key

### Step 2: Install Dependencies

```bash
cd doctor-appointment-system-main
pip install -r requirements.txt
```

### Step 3: Configure API Key

Create a `.env` file in the project root:

```bash
# Copy the example file
copy .env.example .env
```

Edit `.env` and add your API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

### Step 4: Restart the Application

```bash
python app.py
```

## What the AI Can Do

The SmartClinic AI assistant can now:

✅ **Answer Medical Questions**
- Explain symptoms and conditions
- Provide general health advice
- Suggest when to see a doctor

✅ **Help with Appointments**
- Guide users through booking process
- Recommend specialists based on symptoms
- Answer questions about doctors

✅ **Provide Health Information**
- First aid guidance
- Medication information (general)
- Preventive care tips

✅ **Emergency Guidance**
- Recognize urgent symptoms
- Provide immediate first aid steps
- Direct to emergency services when needed

## Example Conversations

**User:** "I have a fever and headache for 3 days"
**AI:** "A fever and headache lasting 3 days could indicate various conditions like flu, infection, or other illnesses. I recommend booking an appointment with a General Physician. In the meantime, rest, stay hydrated, and monitor your temperature..."

**User:** "Which doctor should I see for back pain?"
**AI:** "For back pain, I recommend seeing an Orthopedic specialist or a General Physician first. They can assess your condition and provide appropriate treatment or refer you to a specialist if needed..."

**User:** "How do I book an appointment?"
**AI:** "To book an appointment: 1. Click on 'Hospitals' in the menu, 2. Choose a hospital, 3. Select a doctor based on your needs, 4. Click 'Book Appointment' and fill in the details..."

## Without API Key

If you don't add an API key, the chatbot will still work but with a demo message explaining how to enable the full AI features.

## Privacy & Safety

- The AI is configured to be a medical assistant, not a doctor
- It always recommends seeing a real doctor for serious issues
- It never provides specific diagnoses or prescriptions
- All conversations are processed securely through Google's Gemini API

## Troubleshooting

**Error: "Module not found"**
- Run: `pip install -r requirements.txt`

**AI not responding**
- Check your `.env` file has the correct API key
- Verify the key is valid at https://makersuite.google.com/app/apikey
- Restart the application

**Rate limit errors**
- Free tier has limits (60 requests per minute)
- Wait a moment and try again
- Consider upgrading if needed

## Cost

Google Gemini API is **FREE** for:
- 60 requests per minute
- 1,500 requests per day
- Perfect for small to medium clinics!

Enjoy your intelligent SmartClinic AI! 🤖🏥
