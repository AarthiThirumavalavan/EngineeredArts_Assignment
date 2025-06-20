import asyncio
import websockets
import os


URI = "ws://localhost:8000/ws"

TEST_QUERIES = [
    "What does Engineered Arts do?",
    "What is a humanoid robot?",
    "Who invented the first robot and when?",
    "How is AI used in robotics, explain in simple and short terms.",
    "Tell me how robots will shape the future."
]

OUTPUT_DIR = "/Users/aarthithirumavalavan/Desktop/Job_related_UK/EngineeredArts/test_audio_outputs/"

async def run_test_query(query, index):
    """
    Connects to the WebSocket server, sends a query, and saves the audio response.
    """
    print(f"Test Query: {index + 1}: \"{query}\"")
    try:
        async with websockets.connect(URI) as websocket:
            await websocket.send(query)
            audio_data = await websocket.recv()

            if isinstance(audio_data, bytes):
                if not os.path.exists(OUTPUT_DIR):
                    os.makedirs(OUTPUT_DIR)
                file_path = os.path.join(OUTPUT_DIR, f"test_output_{index + 1}.mp3")
                with open(file_path, "wb") as f:
                    f.write(audio_data)
                print(f"SUCCESS: Audio response received and saved to {file_path}\n")
            else:
                print(f"FAILURE: Received a string response (expected bytes): {audio_data}\n")
    except Exception as e:
        print(f"Exception encountered: \"{query}\": {e}\n")


async def main():
    for i, query in enumerate(TEST_QUERIES):
        await run_test_query(query, i)

if __name__ == "__main__":
    print("Starting WebSocket client tests...\n")
    asyncio.run(main())
    print("All tests completed.")