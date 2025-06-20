from fastapi import FastAPI, WebSocket
from app.llm_utils import get_text_response, get_speech_output

app = FastAPI() #Initialize FastAPI framework for setting up websocket server.

@app.websocket("/ws") #defines websocket route at /ws
async def websocket_endpoint(websocket: WebSocket): #async function to handle incoming websocket connections.
    """
    Handles incoming WebSocket connections, processes user prompts, and returns speech audio.
    """
    await websocket.accept() #accepts incoming websokcet connection.
    try:
        while True:
            user_prompt = await websocket.receive_text()
            llm_output = get_text_response(user_prompt)
            speech_output = get_speech_output(llm_output)
            await websocket.send_bytes(speech_output)
    except Exception as e:
        await websocket.send_text(f"Error: {str(e)}")