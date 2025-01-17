import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time
from typing import Callable, Any

# Base class for all agents
class Agent:
    def __init__(self, name: str):
        self.name = name
        self.mc = minecraft.Minecraft.create()

    def post_message(self, message: str):
        self.mc.postToChat(f"[{self.name}] {message}")

    def get_position(self):
        return self.mc.player.getTilePos()

    def set_block(self, x: int, y: int, z: int, block_id: int):
        self.mc.setBlock(x, y, z, block_id)

    def get_block(self, x: int, y: int, z: int):
        return self.mc.getBlock(x, y, z)

# OracleBot: answers questions using a predefined list or an external LLM
class OracleBotLlista(Agent):
    def __init__(self, name: str):
        super().__init__(name)
        # Define a basic knowledge base
        self.knowledge_base = {
            "how to build": "To build in Minecraft, gather resources, select a flat area, and start placing blocks creatively!",
            "diamonds": "Diamonds are usually found between layers 5 and 12. Mine carefully with an iron or better pickaxe.",
            "monsters": "Monsters spawn in dark places. Light up your area with torches to stay safe.",
            "redstone": "Redstone is used to create circuits. Try using it to make doors, traps, or automated farms!",
        }
        self.default_responses = [
            "I don't know the answer to that, but try exploring!",
            "Hmm, that's a tough one. Maybe experiment and see what works!",
            "I'm not sure. Can you ask differently?",
        ]

    def match_question(self, question: str) -> str:
        """Match the question to the knowledge base or return a default response."""
        for keyword, response in self.knowledge_base.items():
            if keyword in question.lower():
                return response
        return random.choice(self.default_responses)

    def answer_question(self, question: str):
        """Answer the question by finding a match in the knowledge base."""
        answer = self.match_question(question)
        self.post_message(f"Q: {question} | A: {answer}")

    def listen_for_questions(self):
        last_chat = ""
        while True:
            chat_events = self.mc.events.pollChatPosts()
            for event in chat_events:
                if event.message != last_chat:  # Avoid repeated responses
                    last_chat = event.message
                    self.answer_question(last_chat)

# Main function demonstrating the bots, runs continuously
def main():
    oracle_bot = OracleBotLlista("OracleBot")
    # Run OracleBot in a separate thread to listen for questions
    import threading
    threading.Thread(target=oracle_bot.listen_for_questions, daemon=True).start()

    while True:
        # Demonstrate each bot periodically
        time.sleep(2)  # Wait before detonating

if __name__ == "__main__":
    main()
