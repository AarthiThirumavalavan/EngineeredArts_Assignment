# LLM to Speech Conversion Application

An application that takes a user's text question, sends it to an OpenAI Language Model (LLM), generates answer, and then converts the LLM's text response into speech output, which is played back to the user in a Streamlit UI.

-----------------------------------------------------------------------------------------------------
## Main parts of the application:
-----------------------------------------------------------------------------------------------------

1.  **FastAPI WebSocket Server**: Handles requests from the client, interacts with the OpenAI API for text generation and speech conversion.
2.  **Streamlit Client**: Provides a UI for users to input their questions and hear the response as audio.

------------------------------------------------------------------------------------------------------
## Application flow chart
------------------------------------------------------------------------------------------------------
<img width="383" alt="Screenshot 2025-06-20 at 15 20 12" src="https://github.com/user-attachments/assets/239811b7-0109-4e95-b331-7b8e667e9a03" />

------------------------------------------------------------------------------------------------------
## Project Structure
------------------------------------------------------------------------------------------------------

```
├── app/
│   ├── llm_utils.py       # Utilities for LLM call and Speech conversion
│   └── websocket_server.py # FastAPI WebSocket server function
├── client/
│   └── streamlit_ui.py    # Streamlit UI function
├── run_server.sh          # Script to start the FastAPI server
└── README.md              # Project structure and instructions on how to run
└── .env                   # To store API key
└── requirements.txt       # List of libraries required for the project to run
```
------------------------------------------------------------------------------------------------------
## Streamlit UI Page
------------------------------------------------------------------------------------------------------

<img width="1078" alt="Screenshot 2025-06-20 at 14 57 35" src="https://github.com/user-attachments/assets/029b4d9a-13fd-49a1-8039-aea57d2db9c1" />

------------------------------------------------------------------------------------------------------
## Installation
------------------------------------------------------------------------------------------------------

1.  **How to start the server**:
    * In a bash terminal run the following commmand:
        bash ./run_server.sh.
    * You will see an output :  
        Uvicorn running on http://127.0.0.1:8000
    * This indicates the server process has started and is running.

2. **How to run the application**:
    * In another terminal, run the following command:
        streamlit run client/streamlit_ui.py
    * This starts the streamilt UI for user interface in the browser.
    * Type a question in the text box and press 'Submit'
    * The application will communicate with the server, get the LLM's response, convert it to speech.
    * This audio is played directly on the audio player in the UI.
    * It is also available as an mp3 file in the directory. 

3. **How to test the application**:
    * You can run 'python test.py' in a terminal to test the 5 queries I have written. 
    * This will generate audio files as output which are saved to 'test_audio_outputs' folder.
    * Alternatively, you can test the end-to-end application by running the streamlit application with your own query.
    This will provide the audio response on the UI itself.


