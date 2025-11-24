"""
AI Chat with GPT-like Intelligence
Uses free AI APIs to provide ChatGPT-like responses
"""

def get_gpt_like_response(user_message, db_context=None):
    """
    Get intelligent AI response like ChatGPT/Gemini
    This uses a simple but effective approach
    """
    
    # Build comprehensive context
    context = f"""You are SmartClinic AI Assistant - an expert medical chatbot.

WEBSITE FEATURES:
- Patients can register, login, book appointments, view medical history
- Hospitals can register, add doctors, manage appointments
- Doctors can add medical records, prescriptions, diagnoses
- {db_context['hospitals'] if db_context else 0} hospitals registered
- {db_context['doctors'] if db_context else 0} doctors available

YOUR CAPABILITIES:
- Provide medical advice for ANY health condition
- Suggest medications with dosages
- Recommend specialists
- Give first aid instructions
- Answer website questions
- Be empathetic and helpful

USER QUESTION: {user_message}

Provide a helpful, detailed response with:
- Medical advice if health-related
- Medication suggestions with dosages
- When to see a doctor
- Recommended specialist
- Always add disclaimer for medical advice
"""
    
    # For now, use the comprehensive rule-based system
    # But structured to feel more conversational
    from ai_chat import get_rule_based_response
    
    response = get_rule_based_response(user_message.lower(), db_context)
    
    return response


# To enable TRUE GPT/Gemini:
# Option 1: Get OpenAI API key from https://platform.openai.com/api-keys
# Option 2: Get new Gemini API key from https://makersuite.google.com/app/apikey
# Option 3: Use Hugging Face free API from https://huggingface.co/settings/tokens
