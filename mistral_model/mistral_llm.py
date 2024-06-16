from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

def run_mistral(user_message, model="mistral-medium"):
    client = MistralClient(api_key=api_key)
    messages = [
        ChatMessage(role="user", content=user_message)
    ]
    chat_response = client.chat(
        model=model,
        messages=messages
    )
    return (chat_response.choices[0].message.content)


def user_message(inquiry):
    user_message = (
        f'''
You are a chemistry bot. Your task is to explain a specific term in chemistry and create a summary about it.

# Term: 
{inquiry}

# Instructions: 
Provide a detailed explanation of the chosen term. Include its definition, key characteristics, and its application in chemical processes.

## Summary:
Create a brief summary of the term, highlighting its main points and ideas.

## Examples:
Provide several examples of how the term is used in chemistry practice or scientific research.

## Sources:
List the main sources of information used to compile the summary.

## Important:
Ensure all information is formatted according to Markdown rules.

        '''
    )
    return user_message
