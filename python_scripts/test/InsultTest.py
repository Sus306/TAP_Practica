import unittest
from unittest.mock import MagicMock
import random
import time
import mcpi.block as block

# Asegúrate de que el archivo de tu clase 'InsultBot' esté importado correctamente.
from bots import InsultBot

class TestInsultBot(unittest.TestCase):
    def setUp(self):
        # Crea una instancia de InsultBot simulada (sin conexión al servidor de Minecraft)
        self.bot = InsultBot()
        self.bot.send_message = MagicMock()
        self.bot.mc.events.pollChatPosts = MagicMock()

    def test_command_insultbot(self):
        # Mock para la función de elección de insultos aleatorios
        random.choice = MagicMock(return_value="¡Eres más lento que un caracol!")
        
        # Ejecutar el comando 'insultbot'
        self.bot.command_insultbot()
        
        # Verificar que send_message fue llamada con el insulto esperado
        self.bot.send_message.assert_called_with("¡Eres más lento que un caracol!")
    
    def test_interactive_chat(self):
        # Simular el mensaje "insultbot" en el chat
        self.bot.mc.events.pollChatPosts.return_value = [MagicMock(message="insultbot")]
        
        # Ejecutar la función interactive_chat (esto debería llamar command_insultbot)
        self.bot.interactive_chat()
        
        # Verificar que send_message fue llamada (esto asegura que el insulto fue enviado)
        self.bot.send_message.assert_called_with("¡Eres más lento que un caracol!")

    def test_random_insult(self):
        # Probar que random.choice elige un insulto correctamente
        insults = [
            "¡Eres más lento que un caracol!",
            "¿De verdad eso es lo mejor que puedes hacer?",
            "¡He visto ovejas más inteligentes que tú!",
            "¿Acaso estás perdido?",
            "¡Tu construcción parece un queso suizo!"
        ]
        
        # Hacer que random.choice elija un valor específico
        random.choice = MagicMock(return_value=insults[0])
        
        # Ejecutar la función y verificar que se elige correctamente
        self.bot.command_insultbot()
        self.bot.send_message.assert_called_with(insults[0])

    def test_sleep(self):
        """Verificar que la función de espera no bloquea el hilo."""
        start_time = time.time()
        self.bot.command_insultbot()
        elapsed_time = time.time() - start_time
        # Verificar que el tiempo de espera es alrededor de 2 segundos
        self.assertGreater(elapsed_time, 1.8)
        self.assertLess(elapsed_time, 2.2)

if __name__ == '__main__':
    unittest.main()