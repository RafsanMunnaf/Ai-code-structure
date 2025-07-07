# the code you will be writting here will be production grade...
# first write in local_ai.py to write development code then turn it into function based /class based to exchange data in json format.
import requests
from django.contrib.auth import get_user_model
from chat.models import Message
from django.conf import settings


def get_or_create_bot_user():
    User = get_user_model()
    bot, _ = User.objects.get_or_create(
        username="AI_Bot",
        defaults={
            "email": "bot@example.com",
            "password": User.objects.make_random_password()
        }
    )
    return bot



AI_URL = settings.AI_API_URL
AI_MODEL = settings.AI_MODEL_NAME
AI_STREAM = settings.AI_STREAMING


def generate_response_from_chat(chat, user, user_input):
    # Save user message
    Message.objects.create(chat=chat, sender=user, content=user_input)

    # Get last 10 messages for context
    messages = Message.objects.filter(chat=chat).order_by('-timestamp')[:10][::-1]

    # Format prompt
    prompt = "\n".join([
        f"User: {m.content}" if m.sender == user else f"Assistant: {m.content}"
        for m in messages
    ]) + f"\nUser: {user_input}\nAssistant:"

    # Call Ollama API
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        if response.status_code != 200:
            error_message = response.json().get("error", "Unknown error")
            return f"AI response failed: {error_message}", prompt

        ai_reply = response.json()["response"]

        # Save AI reply
        Message.objects.create(
            chat=chat,
            sender=get_or_create_bot_user(),
            content=ai_reply
        )

        return ai_reply, prompt + ai_reply

    except requests.exceptions.RequestException as e:
        return f"Request to AI failed: {str(e)}", prompt