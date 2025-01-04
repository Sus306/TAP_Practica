import mcpi.minecraft as minecraft
import openai
import os
import time

# Load OpenAI API key from environment variable (safer than hardcoding it)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Connect to the Minecraft server
mc = minecraft.Minecraft.create()

# Send a message to the Minecraft chat to indicate that the bot is active
mc.postToChat("Hello! I am OracleBot. Ask me anything!")

# Predefined responses as a fallback (optional)
responses = {
    "how are you?": "I'm doing well, thanks for asking!",
    "what is your name?": "I'm OracleBot, your friendly assistant.",
}

# Function to query ChatGPT and get a response
def get_chatgpt_response(message):
    try:
        # Make a call to OpenAI API to get a response from ChatGPT
        completion = openai.Completion.create(
            engine="text-davinci-003",  # You can adjust this for the latest model
            prompt=message,
            max_tokens=150
        )
        return completion.choices[0].text.strip()
    except Exception as e:
        return f"Error while fetching response: {str(e)}"

# Function to process the received message
def process_chat_message(message):
    message_lower = message.lower()

    # Check if the message has a predefined response
    if message_lower in responses:
        return responses[message_lower]
    else:
        # If no predefined response, query ChatGPT
        return get_chatgpt_response(message)

# Main loop to simulate receiving messages (You will need a Minecraft chat integration here)
while True:
    # In a real scenario, this would be replaced with actual chat reading functionality
    player_message = "What is the meaning of life?"  # Simulating a chat message

    # Get the bot's response
    response = process_chat_message(player_message)

    # Send the response back to the Minecraft chat
    mc.postToChat(response)

    # Sleep for a while before checking for the next message (simulating chat intervals)
    time.sleep(5)
