import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
from Python_scripts.bots.PrimerBot import MinecraftAgent

class InsultBot(MinecraftAgent):

    def command_insultbot(self):
        # Lista de insultos
        insults = [
            "¡Eres más lento que un caracol!",
            "¿De verdad eso es lo mejor que puedes hacer?",
            "¡He visto ovejas más inteligentes que tú!",
            "¿Acaso estás perdido?",
            "¡Tu construcción parece un queso suizo!",
        ]
        # Elegir un insulto aleatorio
        insult = random.choice(insults)
        self.send_message(insult)

    def interactive_chat(self):
        # Responder a comandos en el chat usando reflexión
        self.send_message("Dime 'insultbot' para recibir un insulto")
        while True:
            try:
                chat_events = self.mc.events.pollChatPosts()
                for event in chat_events:
                        if event.message.lower() == "insultbot":
                            self.command_insultbot()
            except StopIteration:
                break

if __name__ == "__main__":
    bot = InsultBot()
    bot.send_message("Hola, soy InsultBot. Estoy listo.")

    # Esperar un momento antes de comenzar
    time.sleep(2)

    # Habilitar interacciones en el chat
    bot.interactive_chat()
