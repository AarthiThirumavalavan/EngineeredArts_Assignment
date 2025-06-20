from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# Load API key .env file
api_key_from_env = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key_from_env)

def get_text_response(user_prompt):
    """
    Gets a text response from the OpenAI LLM for a given user prompt.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a question-answering assistant. Provide a concise and accurate answer to the user's question."},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in get_text_response: {e}") 
        raise # Re-raise to be caught by websocket handler

def get_speech_output(llm_output):
    """
    Converts the LLM's text output into speech audio bytes using OpenAI TTS.
    """
    try:
        with client.audio.speech.with_streaming_response.create(
            model="tts-1",  
            voice= "alloy",  #voice model
            input=llm_output
        ) as response:
            audio_bytes = response.read() # Read all bytes from the stream
        return audio_bytes
    except Exception as e:
        print(f"Error in get_speech_output: {e}")
        raise # Re-raise to be caught by websocket handler