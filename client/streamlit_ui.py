import streamlit as st
import asyncio
import websockets

st.title("LLM to Speech")
user_prompt = st.text_input("Enter your question:")
# Sends user prompt to the WebSocket server and receives audio bytes in response.
if st.button("Send"):
    async def send_and_receive():
        uri = "ws://localhost:8000/ws"
        async with websockets.connect(uri) as websocket:
            await websocket.send(user_prompt)
            audio = await websocket.recv()
            return audio

    audio_bytes = asyncio.run(send_and_receive()) #Runs send_and_receive async function and blocks until it is complete.
    
    if audio_bytes:
        if isinstance(audio_bytes, str):
            st.error(f"Unexpected string received instead of audio bytes:\n{audio_bytes}")
        else:
            audio_path = "/Users/aarthithirumavalavan/Desktop/Job_related_UK/EngineeredArts/speech.mp3"
            with open(audio_path, "wb") as f:
                f.write(audio_bytes)
            st.audio(audio_path, format="audio/mp3")
